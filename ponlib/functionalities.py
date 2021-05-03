import os

from . import funcs
import re
import requests

for i in dir(funcs):
    if not i.startswith("__") and not i.endswith("__"):
        exec (i+" = funcs."+i)
try:
    with open("data.pon", "r") as file:
        local_version = read_pon(file)["version"]
except:
    try:
        with open("ponlib/data.pon", "r") as file:
            local_version = read_pon(file)["version"]
    except:
        with open("./data.pon", "r") as file:
            local_version = read_pon(file)["version"]

def check_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/dgc08/ponlib/master/__init__.py")
        a = str(re.findall('__version__ = "(.*)"', r.text))
        remote_version = a.replace("[", "").replace("]", "").replace("'", "")

        if remote_version != local_version:
            return "Your local version is different to the actual verion!\n" + \
                  f"You are running version {local_version}. Version {remote_version} is available at https://github.com/dgc08/ponlib/"

    except Exception as error:
        return f"A problem occured while checking for an update: {error}"
