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
    with open('storage1.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        dictionary_main = {}
        for row in reader:
            dictionary_main[row[0]] = (row[1], row[2])
        return dictionary_main

def search_by_app(dictionary_main):
    appellation = input('Choose a word: ').upper()
    if appellation in dictionary_main:
        tuple_divide = dictionary_main[appellation]
        print (R+'Explanation: '+tuple_divide[0]+'\n'+'Source: '+tuple_divide[1])
    else:
        print(R+'Don\'t find appellation !')

def add_def(dict_update):
    appellation = input ('Type appellation: ').upper()
    definition = input ('Type explanation: ')
    source = input ('Type a source: ')
    dict_update[appellation] = (definition, source)

    with open('storage1.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([appellation, definition, source])
        print (R+'New definition added !')

def show_app_alphabetically(dictionary_main):
    sorted_dict = (sorted(dictionary_main))
    for key in sorted_dict:
        print (R+key)

def search_app_by_letter(dictionary_main):
    letter = input('Type a letter: ').upper()
    if letter.isalpha():
        for key in dictionary_main.keys():
            if key.startswith(letter):
                print (R+key)
    else:
        print (R+'Wrong! Type a letter !')

def end_program():
    print (R+'Good day Sir/Madam')
    sys.exit()


def main():
    dictionary_main = load_file()
    while 1:
        print (D+start_screen)
        answer = input('Choose an option: ')
        if answer == '1':
            search_by_app(dictionary_main)
        elif answer == '2':
            add_def(dictionary_main)
        elif answer == '3':
            show_app_alphabetically(dictionary_main)
        elif answer == '4':
            search_app_by_letter(dictionary_main)
        elif answer == '5':
            end_program()
        else:
            print (R+'Choose valid number !')
main()
