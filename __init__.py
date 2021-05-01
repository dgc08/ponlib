from . import ponlib

__version__ = "v1.0.3"

for i in dir(ponlib):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = ponlib."+i)
