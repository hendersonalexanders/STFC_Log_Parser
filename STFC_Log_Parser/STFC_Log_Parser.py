import csv
import tkinter as tk
from tkinter import filedialog

#File Dialog to get import data....
root = tk.Tk()
root.withdraw()
file_path  = filedialog.askopenfilename();

print (file_path)

with open(file_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if len(row) > 0:
            #Label row of the "battle rounds" content. Can probably use this to make a flexible parser 
            if row[0] == "Round":
                break;
    for row in spamreader:
        print(', '.join(row))