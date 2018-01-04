import csv
import sys

# colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
D  = '\033[33m' # orange

start_screen = '''
            Dictionary for a little programmer:
        1) search explanation by appellation
        2) add new definition
        3) show all appellations alphabetically
        4) show available definitions by first letter of appellation **
        5) exit
'''

def load_file():
    with open('storage.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        dictionary_main = dict(reader)
        csvfile.close()
        return dictionary_main

def option_one(dictionary_main):
    appellation = input('Choose a word: ').upper()
    if appellation in dictionary_main.keys():
        tuple_divide = dictionary_main[appellation].split("', '")
        print (R+tuple_divide[0][2:]+'\n'*2+tuple_divide[1][:-2])
    else:
        print(R+'Don\'t find appellation !')

def option_two():
    appellation = input ('Type appellation: ').upper()
    definition = input ('Type expllanation: ')
    source = input ('Type a source: ')
    new_def = {}
    new_def[appellation] = (definition,source)

    with open('storage.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in new_def.items():
            writer.writerow([key, value])
            csvfile.close()
            print (R+'New definition added !')

def option_three(dictionary_main):
    sorted_dict = (sorted(dictionary_main))
    for key in sorted_dict:
        print (R+key)

def option_four(dictionary_main):
    letter = input('Type a letter: ').upper()
    if letter.isalpha():
        for key in dictionary_main.keys():
            if key.startswith(letter):
                print (R+key)
    else:
        print (R+'Wrong! Type a letter !')

def option_five():
    print (R+'Good day Sir/Madam')
    sys.exit()


def main():
    while 1:
        print (D+start_screen)
        answer = input('Choose an option: ')
        dictionary_main = load_file()
        if answer == '1':
            option_one(dictionary_main)
        elif answer == '2':
            option_two()
        elif answer == '3':
            option_three(dictionary_main)
        elif answer == '4':
            option_four(dictionary_main)
        elif answer == '5':
            option_five()
        else:
            print (R+'Choose valid number !')
main()
