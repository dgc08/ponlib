from funcs import read_pon, write_pon
from datetime import datetime


if __name__ == "__main__":
    with open("example.pon", "r") as fl:
        print(read_pon(fl, ["datetime"]))
    print()
    lst = [1, 2, 3]
    dct = {"hello":"hi"}
    obj = datetime(year=2021, month=4, day=30)
    write_pon("write_example.pon", lst, "lst", ["datetime"])
    write_pon("write_example.pon", dct, "dct", ["datetime"])
    write_pon("write_example.pon", obj, "obj", ["datetime"])
    with open("write_example.pon", "r") as fl:
        print(read_pon(fl, ["datetime"]))
