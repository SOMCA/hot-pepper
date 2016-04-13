import argparse
import csv
import matplotlib.pyplot as plt
import re
import statistics
import sys

from glob import glob

def display(merged_files, limit):
    regex = re.compile(".*merged_([a-zA-Z]+).csv")
    y_content = []
    merged_files.sort(reverse=True)
    for i in range(len(merged_files)):
        current_file = merged_files[i]
        print(current_file)
        current_label = regex.match(current_file).group(1)
        with open(current_file, "r") as csv_content:
            csv_reader = csv.reader(csv_content)
            if limit[1] == -1:
                y_content = [float(row[0]) for row in csv_reader if (not (re.match("^\d+?\.\d+?$", row[0]) is None))]
            else:
                y_content = [float(row[0]) for value, row in enumerate(csv_reader) if (not (re.match("^\d+?\.\d+?$", row[0]) is None) and (value >= limit[0]) and (value < limit[1]))]
            x_content = [i for i in range(len(y_content))]
            plt.plot(x_content, y_content, label=current_label)
            plt.legend()

    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Get stats from Powertool output')
    parser.add_argument('-p', '--path', type=str, default=None, required=True,
                        help="specify path to your directories")
    parser.add_argument('-l', '--limit', type=int, default=[0, -1], nargs = 2,
                        help="limit to plot")
    args = parser.parse_args()
    directories = glob(args.path+"*")

    if len(directories) == 0:
        sys.exit(1)

    csv_files = []

    for directory in directories:
        current_files = [x for x in glob(directory + "/*") if "merged" in x]
        csv_files = csv_files + current_files

    display(csv_files, args.limit)

if __name__ == '__main__':
    main()
