import argparse
import os
import subprocess
import sys
import threading
import time

from subprocess import call
from datetime import datetime
from yoctoammeter import YoctoDevice
from cstatistics import CStatistics

gc_app = "PAPRIKA_gccall.apk"

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
		p = subprocess.Popen(["calabash-android", "run", app], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + "\n")
		f.flush()
	elif not feature and scenario:
		p = subprocess.Popen(["calabash-android", "run", app, "--tags", scenario], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + " --tags " + scenario + "\n")
		f.flush()
	elif feature and not scenario:
		p = subprocess.Popen(["calabash-android", "run", app, feature], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + " " + feature + "\n")
		f.flush()
	elif feature and scenario:
		p = subprocess.Popen(["calabash-android", "run", app, feature, "--tags", scenario], shell=False,stdout=f)
		f.write("COMMAND : calabash-android run " + app + " " + feature + " --tags " + scenario + "\n")
		f.flush()
	p.wait()
	f.flush()
	stop_event.set()
	f.write("\n****** STOP : "+str(datetime.now()) + "\n")
	f.flush()

def launch_gc_app():
	# The application "PAPRIKA_gccall.apk" must be installed on the Android smartphone!
	gc_call = subprocess.Popen(["adb","shell","am","start","-n","paprika.io.gccall/.MainActivity"], shell=False)
	gc_call.wait()

def clear_cache_file(app):
	# Clear cache files at the ending
	call(["adb","shell","pm","clear",app])

def force_stop_app(app):
	# Force the application which launch the garbage collector to stop
	p = subprocess.Popen(["adb","shell","am","force-stop", app], shell=False)
	p.wait()

def get_new_output(output, app, refactored, instance):
	# Output name for non-refactored application
	return ("/".join([output, "/{0}_test_{1}.csv".format(app.split("/")[-1], instance)])) if (not refactored) else ("/".join([output, "/{0}_test_R{1}_{2}.csv".format(app.split("/")[-1], refactored, instance)]))

def main():

	args = parse_arguments()

	if args.scenario and not (args.scenario[0] == "@"):
		print("/!\ [WARNING] /!\ \n===> The scenario must have the '@' sign!")
		sys.exit(1)

	execution_time_output = "%s/%s" % (args.output, "execution_time.txt")

	print("EXECUTION TIME OUTPUT %s" % execution_time_output)

	os.command("touch %s" % execution_time_output)
	os.command("echo > %s" % execution_time_output)

	for x in range(args.begin, args.begin + args.nbr):
		"""
			Test nbr times the app and the energy consumption
		"""

		# Force the device to clear logs
		subprocess.Popen(["adb", "logcat", "-c"], shell=False)

		# Output name to store data
		current_output = get_new_output(args.output, args.app, args.refactored, x)

		force_stop_app(args.app)

		# Call the garbage collector to launch
		if args.gc:
			launch_gc_app()
			force_stop_app(gc_app)

		# Wait 10 seconds to avoid biases caused with the garbage collector application launch
		time.sleep(10)

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

		print(CStatistics([y for x, y in yocto_device._values]))

		os.command("adb logcat | grep EXEC >> %s" % execution_time_output)

	print("DONE")

	clear_cache_file(app)

if __name__ == '__main__':
	main()
