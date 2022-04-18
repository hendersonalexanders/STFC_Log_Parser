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
            
    roundcount = 1
    for row in spamreader:
        if len(row) > 0:
            if len(bat.rounds) < int(row[0]):
                round = bto.Round([], roundcount)
                round.round_nbr = roundcount
                bat.rounds.append(round)
                roundcount += 1
            elif (row[2] == "Attack"):
                damage_instance = bto.DamageInstance(int(row[14]), int(row[13]), int(row[12]), int(row[15]), row[21], row[3], row[11])
                #i hate the zero indexing fix, but whatever, can fix it later
                bat.rounds[int(row[0]) - 1].dmg_instance.append(damage_instance)
            elif (row[2] == "Shield Depleted"):
                damage_instance = bto.DamageInstance(0, 0, 0, 0, row[21], row[3], row[11])
                #i hate the zero indexing fix, but whatever, can fix it later
                bat.rounds[int(row[0]) - 1].dmg_instance.append(damage_instance)
            elif (row[2] == "Combatant Destroyed"):
                damage_instance = bto.DamageInstance(0, 0, 0, 0, row[21], row[3], row[11])
                #i hate the zero indexing fix, but whatever, can fix it later
                bat.rounds[int(row[0]) - 1].dmg_instance.append(damage_instance)

    bat.populate_player_list()
    print (bat.players)

    printHullDict = bat.total_hull_damage_per_player() 
    printShieldDict = bat.total_shield_damage_per_player() 
    printMitDamage = bat.total_mitigated_damage_per_player()
    printCritCount = bat.total_crits_per_player()
    printMitPct = bat.avg_mit_percent_per_player()


    for player in bat.players:
        print (f"{player}'s stats: ")
        if player in printHullDict:
            tempDmg = printHullDict[player]
            print (f"   hull damage: {tempDmg:,}")
        if player in printShieldDict:
            tempDmg = printShieldDict[player]
            print (f"   shield damage: {tempDmg:,}")
        if player in printMitDamage:
            tempDmg = printMitDamage[player]
            print (f"   total damage: {tempDmg:,}")
        if player in printCritCount:
            tempCrit = printCritCount[player]
            print (f"   total critical hits: {tempCrit:,}")
        if player in printMitPct:
            tempMit = printMitPct[player]
            print (f"   average mit percent: {tempMit:.2f}")

        
        tempRoundMit = "Per-round mitigation: "
        for round in bat.rounds:
            mitPerPlayer = round.mitigation_percentage_per_player()
            if player in mitPerPlayer:
                mitNumber = mitPerPlayer[player]
                tempRoundMit = tempRoundMit + f", {round.round_nbr}: " + f"{mitNumber:.2f}"

        print(tempRoundMit)

        print("==============================================================")
        