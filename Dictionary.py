import csv
import sys

definitions = {
    'FUNCTION': ('''A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.''', '''https://www.tutorialspoint.com/python/python_functions.htm'''),
    'PARAMETER': ('''A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept.''' ,'''https://docs.python.org/3.3/glossary.html#term-parameter'''),
    'VARIABLE': ('''Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.''', '''https://www.tutorialspoint.com/python/python_variable_types.htm'''),
    'ARGUMENT': ('''Value passed to a function (or method) when calling the function.''', '''https://docs.python.org/3/glossary.html#term-argument'''),
    'DICTIONARY': ('''An associative array, where arbitrary keys are mapped to values.''', '''https://docs.python.org/3.3/glossary.html#term-parameter'''),
    'TUPLE': ('''A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.''', '''https://www.tutorialspoint.com/python/python_tuples.htm'''),
    'MODULE': ('''A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.''', '''https://www.tutorialspoint.com/python/python_modules.htm'''),
    'ASCII TABLE': ('''Is a character encoding standard. ASCII encodes 128 specified characters. The characters encoded are numbers 0 to 9, lowercase letters a to z, uppercase letters A to Z, basic punctuation symbols, control codes that originated with Teletype machines and a space.''', ''' https://en.wikipedia.org/wiki/ASCII'''),
    'LIST': ('''The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.''', '''https://www.tutorialspoint.com/python/python_lists.htm'''),
    'STRING': ('''Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes. Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable.''', '''https://www.tutorialspoint.com/python/python_strings.htm'''),
    'IDLE': ('''An Integrated Development Environment for Python. IDLE is a basic editor and interpreter environment which ships with the standard distribution of Python.''', '''https://docs.python.org/3.3/glossary.html#term-parameter'''),
    'IMMUTABLE': ('''An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.''', '''https://docs.python.org/3.3/glossary.html#term-parameter'''),
    'LAMBDA': ('''An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [arguments]: expression''', '''https://docs.python.org/3.3/glossary.html#term-parameter'''),
    'OBJECT': ('''Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.''', '''https://docs.python.org/3.3/glossary.html#term-parameter'''),
    'SLICE': ('''An object usually containing a portion of a sequence. A slice is created using the subscript notation, [] with colons between numbers when several are given, such as in variable_name[1:3:5]. The bracket (subscript) notation uses slice objects internally.''', '''https://docs.python.org/3.3/glossary.html#term-parameter''')
}
'''
with open('storage.csv', "w") as csvfile:
    writer = csv.writer(csvfile)

    for key, value in definitions.items():     # Save csv 'w' or 'a'
        writer.writerow([key, value])
    csvfile.close()


with open('storage.csv') as csvfile:
        reader = csv.reader(csvfile)
        definitions_main = dict(reader)
        csvfile.close()                         # Load csv
'''

################################################################################

# colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange

while 1:

# Menu screen
    print(G+ '''
    Dictionary for a little programmer:
    1) search expllanation by appellation,
    2) add new definition,
    3) show all appellations alphabetically,
    4) show available definitions by first letter of appellation,
    5) exit''')

    option = input(O+"\n\n Choose an option: ")  # Enter option

    if option == "1":
        with open('storage.csv') as csvfile:
            reader = csv.reader(csvfile)
            definitions_main = dict(reader)   #load CSV
            csvfile.close()
            answer = str(input("Type appellation: ")).upper()
            if answer in definitions_main.keys():               # Search by key
                print(definitions_main.get(answer.strip()))

            else:
                print(R+ "Don't find appellation.")

    elif option == "2":
        new_appellation = str(input("Type appellation: ")).upper()
        new_expllanation = str(input("Type expllanation: "))
        new_source = str(input("Type a source: "))
        new_def = {}
        new_def[new_appellation] = (new_expllanation, new_source)

        with open('storage.csv', "a") as csvfile:  #add 'a'   # Save new definition in csv
            writer = csv.writer(csvfile)
            for key, value in new_def.items():
                writer.writerow([key, value])
                csvfile.close()
            print("New definition added.")

    elif option == "3":
        with open('storage.csv') as csvfile:
            reader = csv.reader(csvfile)
            definitions_main = dict(reader)    # Display keys alphabetically
            csvfile.close()
            print(sorted(definitions_main))

    elif option == "4":
        letter = str(input("Type first letter of appellation: ")).upper()
        with open('storage.csv') as csvfile:
            reader = csv.reader(csvfile)
            definitions_main = dict(reader)
            csvfile.close()
            for key in definitions_main.keys():
                if key.startswith(letter):
                    print(key)

    elif option == "5":
        print(W+"\nGood day sir")
        break                                     # End program

    else:
        print(R+ "Wrong! Wrong! Wrong!")
