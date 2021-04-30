from funcs import read_pton, write_pton
from datetime import datetime


if __name__ == "__main__":
    with open("example.pton", "r") as fl:
        print(read_pton(fl, ["datetime"]))
    print()
    lst = [1, 2, 3]
    dct = {"hello":"hi"}
    obj = datetime(year=2021, month=4, day=30)
    write_pton("write_example.pton", lst, "lst", ["datetime"])
    write_pton("write_example.pton", dct, "dct", ["datetime"])
    write_pton("write_example.pton", obj, "obj", ["datetime"])
    with open("write_example.pton", "r") as fl:
        print(read_pton(fl, ["datetime"]))
