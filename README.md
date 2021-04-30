# Python Object Notation (pon)
The Python Object Notation is an easy to read format like for Python.<br>
This Programm reads and writes `.pon` files. A example `.pon` file
`example.pon`

    s "This is a string."
    s "This overwrites the string.
    whatsthat "This is an other string."
    
    #One-line comments are supported to!
    
    lst ["This", "is", "a", "list."]
    lst ["This", "will be", "appended", "on lst."]
    dct {"This":"is an dictionary"}
    dct {"Whats that":"is an other entry of the dictionary"}
    
    dct["This"] "is the value of This"

## ponlib.read_pon()
The `ponlib.read_pon(file)` function will return<br>
`{'s': 'This overwrites the string.', 'whatsthat': 'This is an other string.', 'lst': ['This', 'is', 'a', 'list.', 'This', 'will be', 'appended', "on 'lst'."], 'dct': {'This': 'is an dictionary', 'Whats that': 'is an other entry of the dictionary', '"This"': "is the value of 'This'"}}`<br>
If 'file' is the file object of 'example.pon'. <br>The `read_pon()` function returns a namespace dictionary.
## ponlib.write_pon()
If you want to add for example the list  `otherList = [1,2,3]` to `example.pon`, you must call `ponlib.write_pon("example.pon", otherList, "otherList")`
## The `imports` parameter
If you want to store objects from other packages, you must put the package name in the list `imports`.
