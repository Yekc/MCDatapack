# mcdatapack
Create minecraft datapacks in python! (Work in progress)

Here is an example of what it (maybe) will look like to use mcdatapack.
```python
import mcdatapack.datapack as d
import mcdatapack.commands as c

c.new_function("myFunction")

c.say(
	function = "myFunction", 
	text = "Hello, there!"
)

d.dump(
	path = "C:\Users\JohnDoe\AppData\Roaming\.minecraft\saves\New World)", 
	namespace = "myDatapack", 
	description = "This is my datapack!", 
	pack_format = "6"
)
```