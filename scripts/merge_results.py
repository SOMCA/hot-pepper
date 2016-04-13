import argparse
import csv
import re
import sys

from glob import glob

def merge_list(files_content):
    merged = files_content[0]
    for i in range(1, len(files_content)):
        len_merged = len(merged)
        for index, value in enumerate(files_content[i]):
            if index < len_merged:
                merged[index] += value
                merged[index] = merged[index] / 2
            else:
                merged.append(value)
    return merged

def main():
    parser = argparse.ArgumentParser(description='Merge measures from Powertool output')
    parser.add_argument('-p', '--path', type=str, default=None, required=True,
                        help="specify path to your directories")
    parser.add_argument('-d', '--deterministic', type=int,
                        help="Remove the n first values from data")
    parser.add_argument('-s', '--smellcode', type=str, required=True,
                        help="Name of the smell code")
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
            if args.deterministic:
                files_content.append([float(row[0]) for value, row in enumerate(csv_reader) if (not (re.match("^\d+?\.\d+?$", row[0]) is None)) and (value > args.deterministic)])
            else:
                files_content.append([float(row[0]) for value, row in enumerate(csv_reader) if (not (re.match("^\d+?\.\d+?$", row[0]) is None))])

    merged_list = merge_list(files_content)

    with open(args.path + "merged_" + args.smellcode + ".csv", "w") as merged_file:
        for value in merged_list:
            merged_file.write("%s\n" % value)

if __name__ == '__main__':
    main()
