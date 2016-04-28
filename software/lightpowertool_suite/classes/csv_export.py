import csv

class CSVExport(object):
    """docstring for CSVExport"""
    def __init__(self, filename):
        super(CSVExport, self).__init__()
        self._filename = filename

    def export_data(self, data):
        print("Beginning exportation of data...")
        with open(self._filename, "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            for single_data in data:
                csvwriter.writerow(list(single_data))
        print("---" + self._filename + ".csv created! ---")
