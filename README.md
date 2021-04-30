# Python Object Notation (PTON)
The Python Object Notation is an easy to read format like for Python.<br>
This Programm reads and writes `.pton` files. A example `.pton` file
`example.pton`

    s "This is a string."
    s "This overwrites the string.
    whatsthat "This is an other string."
    
    #One-line comments are supported to!
    
    lst ["This", "is", "a", "list."]
    lst ["This", "will be", "appended", "on lst."]
    dct {"This":"is an dictionary"}
    dct {"Whats that":"is an other entry of the dictionary"}
    
    dct["This"] "is the value of This"

## ptonlib.read_pton()
The `ptonlib.read_pton(file)` function will return<br>
`{'s': 'This overwrites the string.', 'whatsthat': 'This is an other string.', 'lst': ['This', 'is', 'a', 'list.', 'This', 'will be', 'appended', "on 'lst'."], 'dct': {'This': 'is an dictionary', 'Whats that': 'is an other entry of the dictionary', '"This"': "is the value of 'This'"}}`<br>
If 'file' is the file object of 'example.pton'. <br>The `read_pton()` function returns a namespace dictionary.
## ptonlib.write_pton()
If you want to add for example the list  `otherList = [1,2,3]` to `example.pton`, you must call `ptonlib.write_pton("example.pton", otherList, "otherList")`
## The `imports` parameter
If you want to store objects from other packages, you must put the package name in the list `imports`.
