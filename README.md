# Python Object Notation (PON)
## Installation
Install the package with  
`git clone https://github.com/dgc08/ponlib/`
## The functions
### ponlib.read_pon()
#### The parameters
`ponlib.read_pon()` has two parameters:  
`file` and  
`imports`
`file` is a file object. Its the `.pon` file to read.  
`imports` is a list. The script will import the packages in this list additionaly to the imports defined in the `.pon` file.
#### Example
If you call `ponlib.read_pon(file)` with [example.pon](https://github.com/dgc08/ponlib/blob/master/ponlib/example.pon) as a file object it will returns  
`{'s': 'This overwrites the string.', 'whatsthat': 'This is an other string.', 'lst': ['This', 'is', 'a', 'list.', 'This', 'will be', 'appended', "on 'lst'."], 'dct': {'This': 'is an dictionary', 'Whats that': 'is an other entry of the dictionary', '"This"': "is the value of 'This'"}}`<br>
## The Object Notation
The Python Object Notation is an easy to read format like for Python.<br>
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
If you want to store objects from other packages, you must put the package name in the list `imports`.
