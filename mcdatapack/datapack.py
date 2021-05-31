import os
import shutil

#Datapack information
class info:
	namespace = ""
	pack_format = "6"
	description = ""
	path = ""

#Scores
class scores:
	def add(self, attr, val):
		setattr(self, attr, val)

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

#Tags
class tags:
	def add(self, attr, val):
		setattr(self, attr, val)

#Predicates
class predicates:
	def add(self, attr, val):
		setattr(self, attr, val)

#Structures
class structures:
	def add(self, attr, val):
		setattr(self, attr, val)

#Dimensions
class dimensions:
	def add(self, attr, val):
		setattr(self, attr, val)

#Default Loot tables
class def_loot_tables:
	def add(self, attr, val):
		setattr(self, attr, val)

#Default Recipes
class def_recipes:
	def add(self, attr, val):
		setattr(self, attr, val)

#Default Structures
class def_structures:
	def add(self, attr, val):
		setattr(self, attr, val)


def dump(path = "", namespace = "", description = "", pack_format = "6"):
	#Clean classes to only contain files
	functions_filtered = [attr for attr in vars(functions) if not attr.startswith("__") and not attr.startswith("add")]
	adv_filtered = [attr for attr in vars(advancements) if not attr.startswith("__") and not attr.startswith("add")]
	loot_filtered = [attr for attr in vars(loot_tables) if not attr.startswith("__") and not attr.startswith("add")]
	recipes_filtered = [attr for attr in vars(recipes) if not attr.startswith("__") and not attr.startswith("add")]
	tags_filtered = [attr for attr in vars(tags) if not attr.startswith("__") and not attr.startswith("add")]
	pred_filtered = [attr for attr in vars(predicates) if not attr.startswith("__") and not attr.startswith("add")]
	struct_filtered = [attr for attr in vars(structures) if not attr.startswith("__") and not attr.startswith("add")]
	dim_filtered = [attr for attr in vars(dimensions) if not attr.startswith("__") and not attr.startswith("add")]
	def_loot_filtered = [attr for attr in vars(def_loot_tables) if not attr.startswith("__") and not attr.startswith("add")]
	def_recipes_filtered = [attr for attr in vars(def_recipes) if not attr.startswith("__") and not attr.startswith("add")]
	def_struct_filtered = [attr for attr in vars(def_structures) if not attr.startswith("__") and not attr.startswith("add")]

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
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/tags")
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/predicates")
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/structures")
	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/dimensions")
	os.mkdir(path + "/" + namespace + "/data/minecraft/loot_tables")
	os.mkdir(path + "/" + namespace + "/data/minecraft/recipes")
	os.mkdir(path + "/" + namespace + "/data/minecraft/structures")

	#-----------------------------------------------------------------------------------------------------------------------

	#Create function files
	for i in functions_filtered:
		if "/" in i:
			isplit = i.split("/")
			os.mkdir(path + "/" + namespace + "/data/" + namespace + "/functions/" + isplit[0])
			f = open(path + "/" + namespace + "/data/" + namespace + "/functions/" + isplit[0] + "/" + isplit[1] + ".mcfunction", "w")
		else:
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

	#Create tag files
	for i in tags_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/tags/" + i + ".json", "w")
		f.write(getattr(tags, i))
		f.close()

	#Create predicate files
	for i in pred_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/predicates/" + i + ".json", "w")
		f.write(getattr(predicates, i))
		f.close()

	#Create structure files
	for i in struct_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/structures/" + i + ".json", "w")
		f.write(getattr(structures, i))
		f.close()

	#Create dimension files
	for i in dim_filtered:
		f = open(path + "/" + namespace + "/data/" + namespace + "/dimensions/" + i + ".json", "w")
		f.write(getattr(dimensions, i))
		f.close()

		#Create default loot table files
	for i in def_loot_filtered:
		f = open(path + "/" + namespace + "/data/" + "minecraft" + "/loot_tables/" + i + ".json", "w")
		f.write(getattr(def_loot_tables, i))
		f.close()

	#Create default recipe files
	for i in def_recipes_filtered:
		f = open(path + "/" + namespace + "/data/" + "minecraft" + "/recipes/" + i + ".json", "w")
		f.write(getattr(def_recipes, i))
		f.close()

	#Create structure files
	for i in def_struct_filtered:
		f = open(path + "/" + namespace + "/data/" + "minecraft" + "/structures/" + i + ".json", "w")
		f.write(getattr(def_structures, i))
		f.close()