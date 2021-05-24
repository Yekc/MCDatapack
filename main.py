import mcdatapack.datapack as d
import mcdatapack.commands as c

c.new_advancement("test")
c.advancement("test", "{}")

d.dump(path = "Testing", namespace = "python_datapack", description = "test", pack_format = "6")