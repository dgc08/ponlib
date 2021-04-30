import os


def read_pon(file, imports: list = []):
    if not hasattr(file, "readlines"):
        raise TypeError("'file' must be a File Object.")
    if len(imports) != 0:
        for i in imports:
            exec ("from "+i+" import *")
            exec ("import "+i)
    filedict = {}
    for line in file.readlines():
        if line.startswith("#imports "):
            con = line.replace("#imports ")
            imports = con.replace(" ","").split(",")
            if len(imports) != 0:
                for i in imports:
                    exec("from " + i + " import *")
                    exec("import " + i)
        if line == "":
            continue
        if line.startswith("#"):
            continue
        if line == "\n":
            continue
        if line == " ":
            continue
        varname = line.split(" ", 1)[0]
        real = varname.split("[", 1)[0]
        if real in filedict and isinstance(filedict[real], list):
            appendlist = eval(line.split(" ", 1)[1])
            rarlist = filedict[real]
            for i in appendlist:
                rarlist.append(i)
            filedict[real] = rarlist
        elif real in filedict and isinstance(filedict[real.split("[", 1)[0]], dict):
            if "[" in varname:
                ke = varname.split("[", 1)[1].replace("]", "").replace(varname, "")
                filedict[real][ke] = eval(line.split(" ", 1)[1])
            else:
                appenddict = eval(line.split(" ", 1)[1])
                rardict = filedict[real]
                rardict.update(appenddict)
                filedict[real] = rardict
        else:
            a = line.split(" ", 1)[1]
            exec ("filedict[real] = "+a)
    return filedict

def write_pon(filename, write_obj, obj_name: str, imports: list = []):
    if len(imports) != 0:
        for i in imports:
            exec ("from "+i+" import *")
            exec ("import "+i)
    with open(filename, "a") as file:
        file.write(obj_name + " " + write_obj.__repr__() + "\n")
def set_imports_pon(filename, imports: list = []):
    with open(filename, "a") as file:
        if len(imports) != 0:
            file.write("#import ")
            s = ""
            for i in imports:
                s += (i+", ")
            s = s[:-1]
            s = s[:-1]
            file.write(s+"\n")
