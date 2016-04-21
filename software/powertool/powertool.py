import argparse

from time import sleep

from yoctoammeter import YoctoDevice
from csv_export import CSVExport

def main():

    args = argparse

    yocto_device = YoctoDevice()

    print(yocto_device)

    yocto_device.run()

    sleep(5)

    yocto_device.stopMeasure()

    csv_obj = CSVExport("mytest.csv")

    csv_obj.export_data(yocto_device._values)


if __name__ == '__main__':
    main()
