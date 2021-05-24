import mcdatapack.datapack as d
from termcolor import colored

#---------- CREATE FILES

#Create a new function
def new_function(name):
	d.functions.add(d.functions, name, "")

#Create a new advancement
def new_advancement(name):
	d.advancements.add(d.advancements, name, "")

#Create a new loot table
def new_loot_table(name):
	d.loot_tables.add(d.loot_tables, name, "")

#---------- RAW COMMANDS

#Create a raw command
def command(function = "", command = ""):
	try:
		exec("d.functions." + function + " += \"" + command + "\\n\"")
	except:
		print(colored("Function \"" + function + "\" is not defined.", "red"))

#---------- DEFAULT COMMANDS

#Create a say command
def say(function = "", text = ""):
	try:
		exec("d.functions." + function + " += \"say " + text + "\"")
	except:
		print(colored("Function \"" + function + "\" is not defined.", "red"))

#---------- ADVANCEMENTS

#Create advancement
def advancement(advancement = "", json = "{}"):
	try:
		exec("d.advancements." + advancement + " += \"" + json + "\"")
	except:
		print(colored("Advancement \"" + advancement + "\" is not defined.", "red"))

#---------- LOOT TABLES

#Create loot table
def loot_table(loot_table = "", json = "{}"):
	try:
		exec("d.loot_tables." + loot_table + " += \"" + json + "\"")
	except:
		print(colored("Loot table \"" + loot_table + "\" is not defined.", "red"))