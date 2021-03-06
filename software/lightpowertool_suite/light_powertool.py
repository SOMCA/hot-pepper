import argparse

from classes.cstatistics import CStatistics
from classes.export_data.csv_export import CSVExport
from classes.export_data.json_export import JSONExport
from time import sleep
from classes.yoctoammeter import YoctoDevice


def main():
    r"""
    Main program of LightPowertool.

    LightPowertool is a software to measure automatically the energy\
     consumption of devices, using the Yoctopuce ammeter.
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--framerate", type=str, default="50/s",
                        help="Give to the main program the framerate.")
    parser.add_argument("-n", "--network", action="store_true",
                        help="Use the network to send your data\
                        - local server like LightPowertoolServer")
    parser.add_argument("-o", "--output", type=str,
                        help="Give an output file name\
                         to store measured values.")
    parser.add_argument("-c", "--csv", action="store_true",
                        help="Export to CSV file")
    parser.add_argument("-j", "--json", action="store_true",
                        help="Export to JSON file")
    parser.add_argument("-s", "--statistics", action="store_true",
                        help="Ask to output basic statistics\
                         (mean, median, pvariance,...) on measured values.")
    parser.add_argument("-t", "--time", type=int, default=60,
                        help="Due time to measure data.")
    args = parser.parse_args()

    # Get the yocto device
    yocto_device = YoctoDevice(args.framerate, network=args.network)
    print(yocto_device)

    yocto_device.run()
    sleep(args.time)
    yocto_device.stopMeasure()

    # if args.output:
    #     if args.csv:
    #         CSVExport(args.output)\
    #         .export_data((value for value in yocto_device._values))
    #     elif args.json:
    #         JSONExport(args.output)\
    #         .export((value for value in yocto_device._values))

    if args.statistics:
        measures = [y for x, y in yocto_device._values]
        print(CStatistics(measures))

if __name__ == '__main__':
    main()
