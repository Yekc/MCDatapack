import mcdatapack.datapack as d
import mcdatapack.commands as c
import time
#TODO: Recipes/loot tables/structures in minecraft namespace

c.new_score(function = "tick", name = "test", criteria = "dummy")
c.increase_score(function = "tick", target = "@a", name = "test", amount = 5)

print(c.get_score("test"))

d.dump(path = "Testing", namespace = "python_datapack", description = "test", pack_format = "6")