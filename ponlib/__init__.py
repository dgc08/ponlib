from . import funcs


for i in dir(funcs):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = funcs."+i)