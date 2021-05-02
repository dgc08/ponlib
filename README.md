# Python Object Notation (PON)
## Installation
Install the package with  
`git clone https://github.com/dgc08/ponlib/`  
  

[![Open in Google Cloud Shell](https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/dgc08/ponlib&tutorial=README.md)
(run ponlib/example.py)
## The functions
### ponlib.read_pon()
#### The parameters
`ponlib.read_pon()` reads all objects of a `.pon` file.  
`ponlib.read_pon()` has two parameters:  
`file` is a file object. Its the `.pon` file to read.  
`imports` is a list. The script will import the packages in this list additionaly to the imports defined in the `.pon` file.
#### Example
If you call `ponlib.read_pon(file)` with [example.pon](https://github.com/dgc08/ponlib/blob/master/ponlib/example.pon) as a file object it will returns  
`{'s': 'This overwrites the string.', 'whatsthat': 'This is an other string.', 'lst': ['This', 'is', 'a', 'list.', 'This', 'will be', 'appended', "on 'lst'."], 'dct': {'This': 'is a dictionary', 'Whats that': 'is an other entry of the dictionary', '"This"': "is the value of 'This'"}}`  

### ponlib.write_pon()

#### The parameters
`ponlib.write_pon` writes a object in a `.pon` file  
`ponlib.write_pon` has four parameters:  

	filename:    string/list, the name of the file to write
	object:      The object or the list of objects to write
	object_name: string/list, the name/-s of the object/-s to save in the `.pon` file
	imports:     list, imports that are needed to write the object

#### Example
If you want to add for example the list  `otherList = [1,2,3]` to `example.pon`, you must call `ponlib.write_pon("example.pon", otherList, "otherList")`

### ponlib.set_imports_pon
#### The parameters
`ponlib.set_imports_pon` define the imports direct inthe `.pon` file.  
`ponlib.set_imports_pon` has two parameters:

	filename:    string, the name of the file to write
	imports:     The imports to define

#### Example
`set_imports_pon("write_example.pon", ["datetime"])` tells the interpreter that it is necessary to import the `datetime`-package.
## The Object Notation
The Python Object Notation is an easy to read format like for Python.  
The detailed definition of the `.pon` is in the file [PON_DEF-md](https://github.com/dgc08/ponlib/blob/master/PON_DEF.md)
`example.pon`

    s "This is a string."
    s "This overwrites the string.
    whatsthat "This is an other string."
    
    #One-line comments are supported to!
    
    lst ["This", "is", "a", "list."]
    lst ["This", "will be", "appended", "on lst."]
    dct {"This":"is a dictionary"}
    dct {"Whats that":"is an other entry of the dictionary"}
    
    dct["This"] "is the value of This"


### The `imports` parameter
If you want to store objects from other packages, you must put the package name in the list `imports`. Example:

	#imports datetime, numpy

This comment tells the interpreter that it is necessary to import datetime and numpy.
## The license
This project is under the [Chronos License](https://github.com/Team-Chronos/chronos-data/blob/main/ChronosLicense.md). The additional the license iformations are in the [LICENSE.md](https://github.com/dgc08/ponlib/blob/master/LICENSE.md) file.
