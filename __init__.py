__version__ = '1.0.1'


def read_pton(file):
    if not hasattr(file, "readlines"):
        raise TypeError("'file' must be a File Object.")
    filedict = {}
    for line in file.readlines():
        if line == "":
            continue
        if line.startswith("#"):
            continue
        if line == "\n":
            continue
        if line == " ":
            continue
        varname = line.split("=", 1)[0]
        real = varname.split("[", 1)[0]
        if real in filedict and isinstance(filedict[real], list):
            appendlist = eval(line.split("=", 1)[1])
            rarlist = filedict[real]
            for i in appendlist:
                rarlist.append(i)
            filedict[real] = rarlist
        elif real in filedict and isinstance(filedict[real.split("[", 1)[0]], dict):
            if "[" in varname:
                ke = varname.split("[", 1)[1].replace("]", "").replace(varname, "")
                filedict[real][ke] = eval(line.split("=", 1)[1])
            else:
                appenddict = eval(line.split("=", 1)[1])
                rardict = filedict[real]
                rardict.update(appenddict)
                filedict[real] = rardict
        else:
            filedict[real] = eval(line.split("=", 1)[1])
    return filedict


def write_pton(filename, write_obj, obj_name: str):
    with open(filename, "a") as file:
        file.write(obj_name + " " + write_obj.__repr__() + "\n")


class TestClass:
    def __repr__(self):
        return str(type(self).__name__) + "()"
    def __str__(self):
        return "A TestClass Object"


if __name__ == "__main__":
    with open("example.pton", "r") as fl:
        print(read_pton(fl))
    print()
    lst = [1, 2, 3]
    dct = {"moin": "hallo"}
    obj = TestClass()
    write_pton("write_example.pton", lst, "lst")
    write_pton("write_example.pton", dct, "dct")
    write_pton("write_example.pton", obj, "obj")
    with open("write_example.pton", "r") as fl:
        print(read_pton(fl))
