import mcdatapack.datapack as d
import mcdatapack.commands as c
import time
#File to test datapack

c.new_function("test/test")

d.dump(path = "Testing", namespace = "python_datapack", description = "test", pack_format = "6")