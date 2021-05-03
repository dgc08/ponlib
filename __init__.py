import ponlib


for i in dir(ponlib):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = ponlib."+i)
try:
    with open("data.pon", "r") as file:
        __version__ = read_pon(file)["version"]
except:
    try:
        with open("ponlib/data.pon", "r") as file:
            __version__ = read_pon(file)["version"]
    except:
        try:
            with open("./data.pon", "r") as file:
                __version__ = read_pon(file)["version"]
        except:
            __version__ = "v1.0.4"
