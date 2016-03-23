import argparse
import csv
import re
import statistics
import sys

from glob import glob

def get_stats_from(files_names, files_content, only_mean):
    for i in range(len(files_content)):
        file_content = files_content[i]
        if not only_mean:
            file_name = files_names[i]
            print("FILE : {0}".format(files_names[i]))
            print("\t*MEAN : {0}".format(statistics.mean(file_content)))
            print("\t*MEDIAN : {0}".format(statistics.median(file_content)))
            try:
                print("\t*MOST TYPICAL VALUE : {0}".format(statistics.mode(file_content)))
            except:
                print("2 most typical values!")
            print("\t*STANDARD DEVIATION : {0}".format(statistics.stdev(file_content)))
            print("\t*VARIANCE : {0}".format(statistics.variance(file_content)))
        else:
            print("{0}".format(statistics.mean(file_content)))

def get_global_stats(files_content, only_mean):
    data = []
    for sublist in files_content:
        data = data + sublist
    if not only_mean:
        print("*GLOBAL MEAN : {0}".format(statistics.mean(data)))
        print("*GLOBAL MEDIAN : {0}".format(statistics.median(data)))
        try:
            print("*GLOBAL MOST TYPICAL VALUE : {0}".format(statistics.mode(data)))
        except:
            print("2 most typical values!")
        print("*GLOBAL STANDARD DEVIATION : {0}".format(statistics.stdev(data)))
        print("*GLOBAL VARIANCE : {0}".format(statistics.variance(data)))
    else:
        print("{0}".format(statistics.mean(data)))

def main():
    parser = argparse.ArgumentParser(description='Get stats from Powertool output')
    parser.add_argument('-p', '--path', type=str, default=None, required=True,
                        help="specify path to your directories")
    parser.add_argument('-m', '--mean', action="store_true", default=False,
                        help="Only compute the mean for each test")
    args = parser.parse_args()

    directories = glob(args.path+"*")

    if len(directories) == 0:
        sys.exit(1)

    csv_files = []

    for directory in directories:
        current_files = [x for x in glob(directory + "/*") if ".csv" in x]
        csv_files = csv_files + current_files

    files_content = []

    for csv_file in csv_files:
        with open(csv_file, "r") as csv_content:
            csv_reader = csv.reader(csv_content)
            files_content.append([float(row[0]) for row in csv_reader if not (re.match("^\d+?\.\d+?$", row[0]) is None)])

    only_mean = args.mean if args.mean else False

    get_stats_from(directories, files_content, only_mean)

    get_global_stats(files_content, only_mean)

if __name__ == '__main__':
    main()
