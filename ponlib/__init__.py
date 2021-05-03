from . import funcs
from . import functionalities
import sys


for i in dir(funcs):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = funcs."+i)

for i in dir(functionalities):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = functionalities."+i)

try:
    with open("data.pon", "r") as file:
        local_version = read_pon(file)["version"]
except:
    try:
        with open("ponlib/data.pon", "r") as file:
            local_version = read_pon(file)["version"]
    except:
        with open("./data.pon", "r") as file:
            local_version = read_pon(file)["version"]

try:
    args =  sys.argv[1]
except IndexError:
    args = ""
if args == "--version":
    print("Local version: " + local_version)
    check_updates()
if args == "--example":
    from . import example