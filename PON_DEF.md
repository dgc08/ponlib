# Definition of the PON-Format
## The PON Format
In the PON format you can store objects of any
## Strings
In a `.pton` file, you claim strings like this  
`[variable name] "String"`  
If a string variable is defined twice, the value of the variable would be overwritten:   

    s "s is a string, this would be overwritten"
    s "This is the real value of s"`

## Lists
This is a list:

	lst ["First item", "Second item"]
	lst ["Third item"]

If a list is  defined twice, the second content would be appended.
## Dictionarys
Dictionarys are like lists. Here are two examples:

	dict {"cars": 17, "houses": 4}
	dict {"people": 30}
	dict {"roadname":"Example Road}
	theDict {"a Road": {"cars": 17, "houses": 4, #
	"people": 30, "roadname":"Example Road
## Other types and custom classes
Other types and custom classes will work too, but if you define them twice it would be overwritten.
## The /imports-statement
If you use custom classes, you must add a /import statement to import them from their module or package.
An example:

	/import datetime
	datetimeobject datetime.datetime(year=2021, month=4, day=30)
## The /get-statement
With the `/get`-statement you can get variables of other `.pon` files. An example:  
`pon2.pon`

	var2 "This is the variable to get."

`pon1.pon`

	/get pon2.pon:var2

If you read `pon1.pon` now, you will fin `var2` there.

## Call Python functions
You can use the functions of an imported python package too. An example:

	/imports random
	random random.random()

This will return something different every time!
## Ignore a new line
if you put a '#' at the end of a line, the new line will be ignored. Example:

	s "This is #
	only one line and one string."