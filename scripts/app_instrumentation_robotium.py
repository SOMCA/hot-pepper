import argparse
import subprocess
import threading
import time

from subprocess import call
from datetime import datetime

def threaded_test(stop_event, nb, app):
	"""
		To test the threadable application scenario
		f -> file to output logs
	"""
	f = open("test"+str(nb)+".log",'w')
	f.write("****** START : "+str(datetime.now()) + "\n")
	f.flush()
	i = 0
	p = subprocess.Popen(["adb","shell","am","instrument","-w","{0}.test/android.test.InstrumentationTestRunner".format(app)], shell=False,stdout=f)
	p.wait()
	f.flush()
	stop_event.set()
	f.write("\n****** STOP : "+str(datetime.now()) + "\n")
	f.flush()

def launch_powertool(stop_event, output_path):
	"""
		To launch Powertool for each instance of threaded_test
	"""
	p = subprocess.Popen(["powertool", "-b", "-d", "yocto", "-o", output_path], shell=False)
	p.wait()
	stop_event.set()

def main():

	parser = argparse.ArgumentParser(description='Get stats from Powertool output')
	parser.add_argument('-a', '--app', type=str, required=True, help="the package name of the application to study")
	parser.add_argument('-b', '--begin', type=int, default=1, help="The beginning to run tests")
	parser.add_argument('-n', '--nbr', type=int, default=31, help="Number of tests to run")
	parser.add_argument('-o', '--output', type=str, default=None, required=True, help="specify output path")
	parser.add_argument('-r', '--refactored', type=str, default=None, help="specify if the application is refactored")
	args = parser.parse_args()

	# Clear cache files, at the beginning
	call(["adb","shell","pm","clear",args.app])

	for x in range(args.begin, args.begin+args.nbr):
		"""
			Test 60 times the app and the energy consumption
		"""

		current_output = args.output

		if not args.refactored:
			current_output += "/{0}_test_{1}.csv".format(args.app, x)
		else:
			current_output += "/{0}_test_R{1}_{2}.csv".format(args.app, args.refactored, x)

		p = subprocess.Popen(["adb","shell","am","force-stop",args.app], shell=False)
		p.wait()

		thread_stop= threading.Event()

		ttest = threading.Thread(target = threaded_test, args=(thread_stop,x,args.app))
		tpower = threading.Thread(target = launch_powertool, args=(thread_stop,current_output))
		ttest.start()
		tpower.start()

		ttest.join()
		tpower.join()

		time.sleep(7)
		# Reset all consumer choices
		call(["adb","shell","pm","clear",args.app])

	print("DONE")

	# Clear cache files at the ending
	call(["adb","shell","pm","clear",args.app])

if __name__ == '__main__':
	main()
