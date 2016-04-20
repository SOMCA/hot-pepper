import csv
import matplotlib.pyplot as plt
import os
import re

for dir in os.listdir():
    if not 'merged' in dir:
        current_path = os.getcwd()
        files = os.listdir(current_path + "/" + dir)
        for g_file in files:
            with open(current_path + "/" + dir + "/" + g_file, "r") as csv_f:
                csv_content = csv.reader(csv_f)
                y_content = [float(row[0]) for row in csv_content if (not (re.match("^\d+?\.\d+?$", row[0]) is None))]
                len_content = len(y_content)
                x_content = [i for i in range(len_content)]
                plt.plot(x_content, y_content, label=dir)
                plt.legend()

plt.show()
            
