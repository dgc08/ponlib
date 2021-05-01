from funcs import read_pon, write_pon, set_imports_pon
from datetime import datetime


if __name__ == "__main__":
    with open("example.pon", "r") as fl:
        print(read_pon(fl))
    print()
    lst = [1, 2, 3]
    dct = {"hello":"hi"}
    tpl = (1, 2, 3)
    obj = datetime(year=2021, month=4, day=30)
    set_imports_pon("write_example.pon", ["datetime"])
    write_pon("write_example.pon", lst, "lst")
    write_pon("write_example.pon", tpl, "tpl")
    write_pon("write_example.pon", dct, "dct")
    write_pon("write_example.pon", obj, "obj")
    with open("write_example.pon", "r") as fl:
        print(read_pon(fl, ["datetime"]))