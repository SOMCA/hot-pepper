import argparse
import subprocess
import sys
import threading
import time

from subprocess import call
from datetime import datetime

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

def launch_powertool(stop_event, output_path):
	"""
		To launch Powertool for each instance of threaded_test
	"""
	p = subprocess.Popen(["powertool", "-d", "yocto", "-o", output_path], shell=False)
	p.wait()
	stop_event.set()

def main():

	parser = argparse.ArgumentParser(description='Get stats from Powertool output')
	parser.add_argument('-a', '--app', type=str, required=True, help="the package name of the application to study")
	parser.add_argument('-b', '--begin', type=int, default=1, help="The beginning to run tests")
	parser.add_argument('-f', '--feature', type=str, default=None, help="Specify the feature to run")
	parser.add_argument('-n', '--nbr', type=int, default=31, help="Number of tests to run")
	parser.add_argument('-o', '--output', type=str, default=None, required=True, help="Specify output path")
	parser.add_argument('-r', '--refactored', type=str, default=None, help="Specify if the application is refactored")
	parser.add_argument('-s', '--scenario', type=str, default=None, help="Specify the scenario to run")
	args = parser.parse_args()

	if args.scenario and not (args.scenario[0] == "@"):
		print("The scenario must have the '@' sign!")
		sys.exit()

	for x in range(args.begin, args.begin + args.nbr):
		"""
			Test nbr times the app and the energy consumption
		"""

		current_output = args.output

		if not args.refactored:
			current_output += "/{0}_test_{1}.csv".format(args.app.split("/")[-1], x)
		else:
			current_output += "/{0}_test_R{1}_{2}.csv".format(args.app, args.refactored, x)

		p = subprocess.Popen(["adb","shell","am","force-stop",args.app], shell=False)
		p.wait()

		thread_stop= threading.Event()

		ttest = threading.Thread(target = threaded_test, args=(thread_stop,x,args.app,args.feature,args.scenario))
		tpower = threading.Thread(target = launch_powertool, args=(thread_stop,current_output))
		ttest.start()
		tpower.start()

		ttest.join()
		tpower.join()

		time.sleep(5)

	print("DONE")

	# Clear cache files at the ending
	call(["adb","shell","pm","clear",args.app])

if __name__ == '__main__':
	main()
