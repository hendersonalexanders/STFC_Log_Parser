import csv
import BattleObjects as bto
import tkinter as tk
from tkinter import filedialog

#File Dialog to get import data....
root = tk.Tk()
root.withdraw()
file_path  = filedialog.askopenfilename();

print (file_path)

with open(file_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    bat = bto.Battle()

    for row in spamreader:
        if len(row) > 0:
            #Label row of the "battle rounds" content. Can probably use this to make a flexible parser 
            if row[0] == "Round":
                break;

    for row in spamreader:

        if len(row) > 0:
            if len(bat.rounds) < int(row[0]):
                round = bto.Round()
                bat.rounds.append(round)
            elif (row[2] == "Attack"):
                damage_instance = bto.DamageInstance(int(row[14]), int(row[13]), int(row[12]), int(row[15]), row[20], row[3])
                #i hate the zero indexing fix, but whatever, can fix it later
                bat.rounds[int(row[0]) - 1].dmg_instance.append(damage_instance)
            elif (row[2] == "Shield Depleted"):
                damage_instance = bto.DamageInstance(0, 0, 0, 0, row[20], row[3])
                #i hate the zero indexing fix, but whatever, can fix it later
                bat.rounds[int(row[0]) - 1].dmg_instance.append(damage_instance)



    print (f"Total damage to hulls: {bat.total_hull_damage():,}")

    printDict = bat.total_hull_damage_per_player() 

    for player in printDict:
        tempDmg = printDict[player]
        print (f"{player}'s damage to hulls: {tempDmg:,}")