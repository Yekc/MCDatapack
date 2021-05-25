# mcdatapack
Create minecraft datapacks in python! (Work in progress)

This will be a python package that simplifies the creation of minecraft datapacks.
Here is an example of what it would look like to use mcdatapack.
```python
import mcdatapack.datapack as d
import mcdatapack.commands as c

#Create a function called myFunction
c.new_function("myFunction")

#Add "say Hello, there!" to myFunction
c.say(
	function = "myFunction", 
	text = "Hello, there!"
)

#Create the datapack to the world "New World"
d.dump(
	path = "C:/Users/JohnDoe/AppData/Roaming/.minecraft/saves/New World/datapacks)", 
	namespace = "myDatapack", 
	description = "This is my datapack!", 
	pack_format = "6"
)
```
This creates a datapack that says "Hello, there!" to you if you type `/function myDatapack:myFunction`.

---
## Commands
To create commands, you first have to create a function to put them in (unless you are putting them in the `tick` or `load` functions). 

To create functions, use `commands.new_function(name)`.  
After you create a function, to add commands use `commands.command(function = "", command = "")`.  

There are also some functions for specific commands, for example `commands.say(function = "", text = "")` for the `say <text>` command.

---

Here is a list of all of the functions for specific commands and how to use them.  
- say(function = "", text = "") = `say <text>`
- new_score(function = "", objective = "", criteria = "") = `scoreboard objectives add <objective> <criteria>`
- increase_score(function = "", target = "", objective = "", amount = 0, updatescore = False) = `scoreboard players add <target> <objective> <amount>`
  - updatescore defines if it will update `get_score` to the new value of the objective.
- decrease_score(function = "", target = "", objective = "", amount = 0, updatescore = False) = `scoreboard players remove <target> <objective> <amount>`
  - updatescore defines if it will update `get_score` to the new value of the objective.
- set_score(function = "", target = "", objective = "", value = 0, updatescore = False) = `scoreboard players set <target> <objective> <value>`
  - updatescore defines if it will update `get_score` to the new value of the objective.
- get_score(objective = "")
  - Gets the value of a score (if the score was changed and had `updatescore = True`)
- give_adv(function = "", target = "", advancement = "") = `advancement grant <target> <advancement>`
- take_adv(function = "", target = "", advancement = "") = `advancement revoke <target> <advancement>`

---
## Creating files
To create files such as recipe or function files, you have to use a function to create them.  
Here are the functions you need for every type of file:
- `new_function(name)`
  - Create a new function file
- `new_advancement(name, json = "")`
  - Create a new advancement
- `new_recipe(name, json = "")`
  - Create a new recipe
- `new_loot_table(name, json = "")`
  - Create a new loot table
- `new_tag(name, json = "")`
  - Create a new tag
- `new_predicate(name, json = "")`
  - Create a new predicate
- `new_structure(name, json = "")`
  - Create a new structure
- `new_dimension(name, json = "")`
  - Create a new dimension

---
## Create the datapack files
To create the datapack files, use the `datapack.dump(path = "", namespace = "", description = "", pack_format = "")` function.

---
## Other stuff you can do
You can get information about a datapack by using `datapack.info.(namespace/description/pack_format/path)`  
You can also get the contents of any type of file by checking the datapack module.
For example, if you have a function named "test", you can check its contents using `datapack.functions.test`.