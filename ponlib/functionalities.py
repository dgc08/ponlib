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


class VersionError(Exception):
    pass


def check_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/dgc08/ponlib/master/__init__.py")
        r_pre = requests.get("https://raw.githubusercontent.com/dgc08/ponlib/developement/__init__.py")
        a = str(re.findall('__version__ = "(.*)"', r.text))
        b = str(re.findall('__version__ = "(.*)"', r_pre.text))
        remote_version = a.replace("[", "").replace("]", "").replace("'", "")
        r_pre = b.replace("[", "").replace("]", "").replace("'", "")
        local = local_version
        if remote_version != local and "pre" not in local:
            print( "Your local version is different to the actual stable build!\n" + \
                  f"You are running version {local}. The actual stable build {remote_version} is available at https://github.com/dgc08/ponlib/")
        elif r_pre != local and "pre" in local:
            if r_pre.split("-")[0] == remote_version:
                print( "You are using an old pre-release from the next stable build!\n" + \
                       f"You are running version {local}. The actual pre-release {r_pre} is available at https://github.com/dgc08/ponlib/tree/developement.\n"+
                       f"The actual stable build {remote_version} is available at https://github.com/dgc08/ponlib/")
            if r_pre.split("-")[0] != remote_version:
                print( "You are using an old pre-release from an old stable build!\n IT IS REALLY IMPORTANT THAT YOU UPGRADE NOW!" + \
                       f"You are running version {local}. The actual pre-release {r_pre} is available at https://github.com/dgc08/ponlib/tree/developement.\n" + \
                       f"The actual stable build {remote_version} is available at https://github.com/dgc08/ponlib/")
        elif remote_version == local:
            print( "You are using the actual stable build!\n" + \
                    f"The actual pre-release {r_pre} is available at https://github.com/dgc08/ponlib/tree/developement.\n" + \
                    f"The actual stable build {remote_version} is available at https://github.com/dgc08/ponlib/")
        elif r_pre == local:
            print("You are using the actual pre-release!\n" + \
                f"The actual pre-release {r_pre} is available at https://github.com/dgc08/ponlib/tree/developement.\n" + \
                f"The actual stable build {remote_version} is available at https://github.com/dgc08/ponlib/")
        else:
            print( "Could not identify the verion.")
            raise VersionError("Could not identify the verion.")
    except Exception as error:
        print( f"A problem occured while checking for an update: {error}")
