import argparse
import os
import time
import sys

from adb_utils import launch_monkey_event,\
                      enable_usb_charging,\
                      call_command,\
                      enable_simiasque
from lightpowertool_suite.classes.yoctoammeter import YoctoDevice
from lightpowertool_suite.classes.cstatistics import CStatistics
from lightpowertool_suite.classes.export_data.csv_export import CSVExport


def main():
    parser = argparse.ArgumentParser(description="An instrumentation script\
                                     for Android Monkey")
    parser.add_argument('-a', '--apk',
                        type=str,
                        required=True,
                        help="The APK file")
    parser.add_argument('-n', '--nbr',
                        type=int,
                        default=31,
                        help="Number of tests to run")
    parser.add_argument("-o", "--output",
                        type=str,
                        required=True,
                        help="Output directory to save results")
    parser.add_argument("-p", "--package",
                        type=str,
                        required=True,
                        help="The package to launch")
    parser.add_argument('-r', '--refactored',
                        type=str,
                        default=None,
                        help="Specify if the application is refactored")
    parser.add_argument('-s', '--seed',
                        type=str,
                        required=True,
                        default=None,
                        help="The seed for Android Monkey")
    parser.add_argument('-t', '--tag',
                        type=str,
                        required=True,
                        help="A tag for output (like CALCULATOR or FACEBOOK")
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help="Verbose mode")

    args = parser.parse_args()

    os.system("adb root")

    enable_usb_charging(False)

    print("Disabling charging: OK!")

    print("Enabling Simiasque...")

    enable_simiasque(True)

    time.sleep(5)

    for instance in range(args.nbr):

        command = call_command("uninstall", args.package)

        command.wait()

        print("* Instance %d/%d" % (instance, args.nbr))

        print("* Reinstalling the application")

        install = call_command("install", args.apk)

        install.wait()

        current_output = get_new_output(args.output,
                                        args.package,
                                        args.refactored,
                                        instance)

        yocto_device = None

        try:
            yocto_device = YoctoDevice("75/s", True)
            if args.verbose:
                print(yocto_device)
        except Exception as yocto_exception:
            print(yocto_exception)
            sys.exit(1)

        measure_time_start = time.time()

        (_, monkey_thread) = launch_monkey_event(args.package,
                                                 seed=args.seed,
                                                 events="500000",
                                                 throttle="0")

        yocto_device.run()

        monkey_thread.communicate()

        print("\t Monkey has finished his job...")

        yocto_device.stopMeasure()

        CSVExport(current_output).export_data((value for value in
                                               yocto_device._values))

        print(CStatistics([y for x, y in yocto_device._values]))
        print("\t Scenarios Time : %s" % (time.time() - measure_time_start))

        print("\t Saved in %s" % current_output)

        time.sleep(20)

    enable_usb_charging(True)

    print("Process is finished!")

    print("Disabling Simiasque...")

    enable_simiasque(False)

    print("See directory %s for your results..." % args.output)


def get_new_output(output, app, refactored, instance):
    # Output name for non-refactored application
    return ("/".join([output, "/{0}_test_{1}.csv"
                      .format(app.split("/")[-1], instance)])) if\
                       (not refactored) else\
                       ("/".join([output, "/{0}_test_R{1}_{2}.csv"
                                  .format(app.split("/")[-1],
                                          refactored,
                                          instance)]))

if __name__ == "__main__":
    main()
