#!/usr/bin/python3
# creating table 


import prettytable as pt

table = pt.PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align = "c", valign="t")
table.add_column("Type", ["Electric", "Water", "Fire"], align='l', valign = "b")
print(table)
