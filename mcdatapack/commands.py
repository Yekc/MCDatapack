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

#Create a new recipe
def new_recipe(name):
	d.recipes.add(d.recipes, name, "")

#Create a new tag
def new_tag(name):
	d.tags.add(d.tags, name, "")

#Create a new predicate
def new_predicate(name):
	d.predicates.add(d.predicates, name, "")

#Create a new structure
def new_structure(name):
	d.structures.add(d.structures, name, "")

#Create a new dimension
def new_dimension(name):
	d.dimensions.add(d.dimensions, name, "")

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

#---------- RECIPES

#Create recipe
def recipe(recipe = "", json = "{}"):
	try:
		exec("d.recipes." + recipe + " += \"" + json + "\"")
	except:
		print(colored("Recipe \"" + recipe + "\" is not defined.", "red"))

#---------- TAGS

#Create tag
def tag(tag = "", json = "{}"):
	try:
		exec("d.tags." + tag + " += \"" + json + "\"")
	except:
		print(colored("Tag \"" + tag + "\" is not defined.", "red"))

#---------- PREDICATES

#Create predicates
def predicate(predicate = "", json = "{}"):
	try:
		exec("d.predicates." + predicate + " += \"" + json + "\"")
	except:
		print(colored("Predicate \"" + predicate + "\" is not defined.", "red"))

#---------- STRUCTURES

#Create structure
def structure(structure = "", json = "{}"):
	try:
		exec("d.structures." + structure + " += \"" + json + "\"")
	except:
		print(colored("Structure \"" + structure + "\" is not defined.", "red"))

#---------- PREDICATES

#Create predicates
def dimension(dimension = "", json = "{}"):
	try:
		exec("d.dimensions." + dimension + " += \"" + json + "\"")
	except:
		print(colored("Dimension \"" + dimension + "\" is not defined.", "red"))