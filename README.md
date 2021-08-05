<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Yekc/mcdatapack">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">mcdatapack</h3>

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

#Create a function called myFunction
new_function("myFunction")

#Add "say Hello, there!" to myFunction
say(
	function = "myFunction", 
	text = "Hello, there!"
)

#Create the datapack to the world "New World"
dump(
	path = "C:/Users/JohnDoe/AppData/Roaming/.minecraft/saves/New World/datapacks)", 
	namespace = "myDatapack", 
	description = "This is my datapack!", 
	pack_format = "6"
)
```
This creates a datapack that says "Hello, there!" to you if you type `/function myDatapack:myFunction`.

---
### README.md work in progress.
