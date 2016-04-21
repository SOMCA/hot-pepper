import argparse

from time import sleep

from yoctoammeter import YoctoDevice
from csv_export import CSVExport

def main():

    #Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--framerate", type=str, default="50/s"
                        help="Give to the main program the framerate.")
    parser.add_argument("-o", "--output", type=str,
                        help="Give an output file name to store measured values.")
    parser.add_argument("-s", "--statistics", action="store_true",
                        help="Ask to output basic statistics (mean, median, pvariance,...) on measured values.")
    parser.add_argument("-t", "--time", type=int, default=60,
                        help="Due time to measure data.")
    parser.parse_args()

    #Get the yocto device
    yocto_device = YoctoDevice(parser.framerate)
    print(yocto_device)

    yocto_device.run()
    sleep(parser.time)
    yocto_device.stopMeasure()

    if parser.output:
        csv_obj = CSVExport(parser.output)

    if parser.statistics:
        csv_obj.export_data(yocto_device._values)

if __name__ == '__main__':
    main()
