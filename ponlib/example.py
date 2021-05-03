from . import funcs
from datetime import datetime
import os

for i in dir(funcs):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = funcs."+i)

def main():
    try:
        with open("ponlib/ponlib/example.pon", "r") as fl:
            print(read_pon(fl))
    except FileNotFoundError:
        try:
            with open("ponlib/ponlib/example.pon", "r") as fl:
                print(read_pon(fl))
        except:
            with open("ponlib/ponlib/example.pon", "r") as fl:
                print(read_pon(fl))
    print()
    lst = [1, 2, 3]
    dct = {"hello":"hi"}
    tpl = (1, 2, 3)
    obj = datetime(year=2021, month=4, day=30)
    set_imports_pon("write_example.pon", ["datetime"])
    write_pon("write_example.pon", [lst, dct, tpl, obj], ["lst", "dct", "tpl", "obj"], ["datetime"])
    with open("write_example.pon", "r") as fl:
        print(read_pon(fl, ["datetime"]))
main()