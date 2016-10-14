import argparse
import os
import subprocess
import sys
import threading
import time
import json

from subprocess import call
from datetime import datetime
from lightpowertool_suite.classes.yoctoammeter import YoctoDevice
from lightpowertool_suite.classes.cstatistics import CStatistics
from lightpowertool_suite.classes.export_data.csv_export import CSVExport

gc_app = "PAPRIKA_gccall.apk"
adb_path = os.environ['ANDROID_HOME']

def parse_arguments():
	parser = argparse.ArgumentParser(description='Get stats from Powertool output')
	parser.add_argument('-a', '--app', type=str, required=True, help="the package name of the application to study")
	parser.add_argument('-b', '--begin', type=int, default=1, help="The beginning to run tests")
	parser.add_argument('-f', '--feature', type=str, default=None, help="Specify the feature to run")
	parser.add_argument('-n', '--nbr', type=int, default=31, help="Number of tests to run")
	parser.add_argument('--gc', action="store_true", help="Launch a phone application to ask to Android to run the garbage collector - before each test")
	parser.add_argument('-o', '--output', type=str, default=None, required=True, help="Specify output path")
	parser.add_argument('-r', '--refactored', type=str, default=None, help="Specify if the application is refactored")
	parser.add_argument('-s', '--scenario', type=str, default=None, help="Specify the scenario to run")
	parser.add_argument('--bu', action="store_true", help="Launch the calabash scenario using the bundle gem manager, sometimes this option is required")
	return parser.parse_args()

def threaded_test(stop_event, nb, app, feature=None, scenario=None):
	"""
		To test the threadable application scenario
		f -> file to output logs
	"""
	f = open("test"+str(nb)+".log",'w')
	f.write("****** START : "+str(datetime.now()) + "\n")
	f.flush()
	i = 0
	p = None
	f.write("APP: " + app + "\t")
	if feature:
		f.write("FEATURE: " + feature + "\t")
	if scenario:
		f.write("SCENARIO: " + scenario)
	f.write("\n")
	f.flush()
	if not feature and not scenario:
		# p = subprocess.Popen(["calabash-android", "run", app], shell=False,stdout=f)
		p = subprocess.Popen(["bundle","exec","calabash-android", "run", app], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + "\n")
		f.flush()
	elif not feature and scenario:
		# p = subprocess.Popen(["calabash-android", "run", app, "--tags", scenario], shell=False,stdout=f)
		p = subprocess.Popen(["bundle","exec","calabash-android", "run", app, "--tags", scenario], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + " --tags " + scenario + "\n")
		f.flush()
	elif feature and not scenario:
		# p = subprocess.Popen(["calabash-android", "run", app, feature], shell=False,stdout=f)
		p = subprocess.Popen(["bundle","exec","calabash-android", "run", app, feature], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + " " + feature + "\n")
		f.flush()
	elif feature and scenario:
		# p = subprocess.Popen(["calabash-android", "run", app, feature, "--tags", scenario], shell=False,stdout=f)
		p = subprocess.Popen(["bundle","exec","calabash-android", "run", app, feature, "--tags", scenario], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + " " + feature + " --tags " + scenario + "\n")
		f.flush()
	p.wait()
	f.flush()
	stop_event.set()
	f.write("\n****** STOP : "+str(datetime.now()) + "\n")
	f.flush()

def launch_gc_app():
	# The application "PAPRIKA_gccall.apk" must be installed on the Android smartphone!
	gc_call = subprocess.Popen([adb_path+"/platform-tools/adb","shell","am","start","-n","paprika.io.gccall/.MainActivity"], shell=False)
	gc_call.wait()

def clear_cache_file(app):
	# Clear cache files at the ending
	call([adb_path+"/platform-tools/adb","shell","pm","clear",app])

def force_stop_app(app):
	# Force the application which launch the garbage collector to stop
	p = subprocess.Popen([adb_path+"/platform-tools/adb","shell","am","force-stop", app], shell=False)
	p.wait()

def get_new_output(output, app, refactored, instance):
	# Output name for non-refactored application
	return ("/".join([output, "/{0}_test_{1}.csv".format(app.split("/")[-1], instance)])) if (not refactored) else ("/".join([output, "/{0}_test_R{1}_{2}.csv".format(app.split("/")[-1], refactored, instance)]))

def main():

	args = parse_arguments()

	if args.scenario and not (args.scenario[0] == "@"):
		print("/!\ [WARNING] /!\ \n===> The scenario must have the '@' sign!")
		sys.exit(1)

	# Disable charging using USB
	os.system("$ANDROID_HOME/platform-tools/adb root")
	time.sleep(1)
	os.system("$ANDROID_HOME/platform-tools/adb shell \"echo 0 > /sys/class/power_supply/usb/device/charge\"")
	# Wait 5 seconds to perform the action
	time.sleep(5)

	execution_time_output = "%s/%s" % (args.output, "execution_time.txt")

	os.system("touch %s" % execution_time_output)
	os.system("echo > %s" % execution_time_output)

	for x in range(args.begin, args.begin + args.nbr):
		"""
			Test nbr times the app and the energy consumption
		"""

		# Force the device to clear data
		subprocess.Popen([adb_path+"/platform-tools/adb", "shell", "rm", "-rf", "/data/data/com.example.antonin.jouet*"], shell=False)

		# Output name to store data
		current_output = get_new_output(args.output, args.app, args.refactored, x)

		force_stop_app(args.app)

		# Call the garbage collector to launch
		if args.gc:
			launch_gc_app()
			force_stop_app(gc_app)

		# Wait 10 seconds to avoid biases caused with the garbage collector application launch
		time.sleep(15)
		measure_time_start = time.time()
		print("OUTPUT: %s" % current_output)

		subprocess.Popen([adb_path+"/platform-tools/adb", "logcat", "-c"], shell=False)

		yocto_device = None

		try:
			# Default framerate is 75/s
			yocto_device = YoctoDevice("75/s", True)
			print(yocto_device)
		except Exception as yocto_exception:
			print(yocto_exception)
			sys.exit(1)

		# Create an event to stop the current thread
		thread_stop = threading.Event()

		# Launch the test
		ttest = threading.Thread(target = threaded_test, args=(thread_stop,x,args.app,args.feature,args.scenario))
		ttest.start()

		# Run the device
		yocto_device.run()

		# Wait tests stops...
		ttest.join()
		# ... and stop the yocto device!
		yocto_device.stopMeasure()

		CSVExport(current_output).export_data((value for value in yocto_device._values))

		print(CStatistics([y for x, y in yocto_device._values]))
		print("Scenarios Time : %s" % (time.time() - measure_time_start))

		os.system("$ANDROID_HOME/platform-tools/adb logcat -d | grep EXEC >> %s" % execution_time_output)

	print("DONE")

	os.system("$ANDROID_HOME/platform-tools/adb shell \"echo 1 > /sys/class/power_supply/usb/device/charge\"")
	# Wait 5 seconds to perform the action
	time.sleep(5)

	clear_cache_file(app)

if __name__ == '__main__':
	main()
