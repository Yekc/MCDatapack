<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Yekc/mcdatapack">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
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


```
