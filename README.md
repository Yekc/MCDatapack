<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Yekc/mcdatapack">
    <img src="images/logo.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">MCDatapack</h3>

  <p align="center">
    Create Minecraft datapacks in Python!
    <br />
    Used by MCD Studio (Work in progress)
    <br />
    <br />
  </p>
</p>

This is an unfinished Python package that simplifies the creation of minecraft datapacks.
Here is an example of what it would look like to use mcdatapack.
```python
from mcdatapack.datapack import *
from mcdatapack.commands import *


#Create a function
new_function("sayhello")
#Add a command to the function you just created
command(
  function = "sayhello", 
  command = "say Hello!"
)


#Create the datapack
dump(
  path = r"C:\Users\JohnDoe\AppData\Roaming\.minecraft\saves\New World\datapacks", 
  namespace = "MyDatapack", 
  description = "My own datapack made in mcdatapack!", 
  pack_format = "7"
)
```
This creates a datapack that says "Hello, there!" to you if you type `/function myDatapack:myFunction`.

---
## Commands

### mcdatapack.datapack
```python
import mcdatapack.datapack as datapack

datapack.info                 # Class that stores information about your datapack. The information is automatically updated when you use the dump() function, so you should not ever have to change it.
datapack.info.namespace       # Namespace of your datapack
datapack.info.pack_format     # Pack format of your datapack
datapack.info.description     # Description of your datapack
datapack.info.path            # The path to your datapack

datapack.scores               # Class that stores every scoreboard objective you create
datapack.functions            # Class that stores every function you make
datapack.advancements         # Class that stores every advancement you make
datapack.loot_tables          # Class that stores every loot table you make
datapack.recipes              # Class that stores every recipe you make
datapack.tags                 # Class that stores every tag you make
datapack.predicates           # Class that stores every predicate you make
datapack.structures           # Class that stores every structure you make
datapack.dimensions           # Class that stores every dimension you make
datapack.def_loot_tables      # Class that stores every default loot table you make (default means they are in the default minecraft namespace and not your custom namespace)
datapack.def_recipes          # Class that stores every default recipe you make (default means they are in the default minecraft namespace and not your custom namespace)
datapack.def_structures       # Class that stores every default structure you make (default means they are in the default minecraft namespace and not your custom namespace)

dump(path = "", namespace = "", description = "", pack_format = "7")       # Function to create the datapack.
```

### mcdatapack.commands
```python
import mcdatapack.commands as commands

commands.new_function(name)             # Function that lets you create a new function
commands.new_advancement(name)          # Function that lets you create a new advancement
commands.new_loot_table(name)           # Function that lets you create a new loot table
commands.new_recipe(name)               # Function that lets you create a new recipe
commands.new_tag(name)                  # Function that lets you create a new tag
commands.new_predicate(name)            # Function that lets you create a new predicate
commands.new_structure(name)            # Function that lets you create a new structure
commands.new_dimension(name)            # Function that lets you create a new dimension

commands.command(function = "", text = "")                                                                      # Function that lets you add text to a function
commands.say(function = "", text = "")                                                                          # Function that lets you add a /say command to a function
commands.new_score(function = "", objective = "", criteria = "")                                                # Function that lets you add a new scoreboard objective
commands.increase_score(function = "", target = "", objective = "", amount = "", updatescore = False)           # Function that lets you increase the value of a score by a specific amount
                                                                                                                # (updatescore lets you update the score in the datapack.scores class)
commands.decrease_score(function = "", target = "", objective = "", amount = "", updatescore = False)           # Function that lets you decrease the value of a score by a specific amount
                                                                                                                # (updatescore lets you update the score in the datapack.scores class)

```
