# mcdatapack
Create minecraft datapacks in python! (Work in progress)

This will be a python package that simplifies the creation of minecraft datapacks.
Here is an example of what it (maybe) will look like to use mcdatapack.
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