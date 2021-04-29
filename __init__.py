def read_pton(file):
    if not hasattr(file, "readlines"):
        raise TypeError("'file' must be a File Object.")
    filedict = {}
    for line in file.readlines():
        if line == "":
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
            filedict[real] = eval(line.split(" ", 1)[1])
    return filedict


def write_pton(filename, obj, obj_name: str):
    with open(filename, "a") as fl:
        fl.write(obj_name+" "+obj.__repr__()+"\n")


if __name__ == "__main__":
    with open("test.pton", "r") as fl:
        print(read_pton(fl))
    print()
    lst = [1,2,3]
    dct = {"moin":"hallo"}
    write_pton("write_test.pton", lst, "lst")
    write_pton("write_test.pton", dct, "dct")
    with open("write_test.pton", "r") as fl:
        print(read_pton(fl))
