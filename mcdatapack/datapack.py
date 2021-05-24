import os
import shutil

#Datapack information
class info:
	namespace = ""
	pack_format = "6"
	description = ""
	path = ""

#Functions
class functions:
	def add(self, attr, val):
		setattr(self, attr, val)
	tick = ""
	load = ""

#Advancements
class advancements:
	def add(self, attr, val):
		setattr(self, attr, val)

#Loot tables
class loot_tables:
	def add(self, attr, val):
		setattr(self, attr, val)

#Recipes
class recipes:
	def add(self, attr, val):
		setattr(self, attr, val)


def dump(path = "", namespace = "", description = "", pack_format = "6"):
	#Clean classes to only contain files
	functions_filtered = [attr for attr in vars(functions) if not attr.startswith("__") and not attr.startswith("add")]
	adv_filtered = [attr for attr in vars(advancements) if not attr.startswith("__") and not attr.startswith("add")]
	loot_filtered = [attr for attr in vars(loot_tables) if not attr.startswith("__") and not attr.startswith("add")]
	recipes_filtered = [attr for attr in vars(recipes) if not attr.startswith("__") and not attr.startswith("add")]

	#Update datapack information
	info.pack_format = pack_format
	info.namespace = namespace
	info.descripton = description
	info.path = path

	#Remove previous instance of datapack
	if os.path.isdir(path + "/" + namespace):
		shutil.rmtree(path + "/" + namespace)

	#Make directories and files
	os.mkdir(path + "/" + namespace)
	os.mkdir(path + "/" + namespace + "/data")
	mcmeta = open(path + "/" + namespace + "/pack.mcmeta", "w")
	mcmeta.write("""{\n"pack": {\n    "pack_format": """ + pack_format + """,\n    "description": \"""" + description + """\"\n  }\n}""")
	mcmeta.close()
	os.mkdir(path + "/" + namespace + "/data/minecraft")
	os.mkdir(path + "/" + namespace + "/data/" + namespace)
	os.mkdir(path + "/" + namespace + "/data/minecraft/tags")
	os.mkdir(path + "/" + namespace + "/data/minecraft/tags/functions")
	tick = open(path + "/" + namespace + "/data/minecraft/tags/functions/tick.json", "w")
	tick.write("""{\n "values": [\n \"""" + namespace + """:tick\"\n ]\n}""")
	tick.close()
	load = open(path + "/" + namespace + "/data/minecraft/tags/functions/load.json", "w")
	load.write("""{\n "values": [\n \"""" + namespace + """:load\"\n ]\n}""")
	load.close()
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/functions")
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/advancements")
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/loot_tables")
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/recipes")

	#-----------------------------------------------------------------------------------------------------------------------

	#Create function files
	for i in functions_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/functions/" + i + ".mcfunction", "w")
		f.write(getattr(functions, i))
		f.close()

	#Create advancement files
	for i in adv_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/advancements/" + i + ".json", "w")
		f.write(getattr(advancements, i))
		f.close()

	#Create loot table files
	for i in loot_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/loot_tables/" + i + ".json", "w")
		f.write(getattr(loot_tables, i))
		f.close()

	#Create recipe files
	for i in recipes_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/recipes/" + i + ".json", "w")
		f.write(getattr(recipes, i))
		f.close()