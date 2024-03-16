import os
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)

source = f'{current_directory}/phonebook_origin.txt'
f_arrival = f'{current_directory}/phonebook_final.txt'

def create_entry():
    s = input('Type a surname to be added to the phonebook: ')
    n = input('Type a name to be added to the phonebook: ')
    p = input('Type a patronym to be added to the phonebook: ')
    ph = input('Type a phone number to be added to the phonebook: ')
    c = input('Type a city to be added to the phonebook: ')
    line = f'{s} {n} {p} {ph}\n{c}\n\n'
    return line

# take an entry from the file 
def relocate_entry(source, n):
    with open(source, 'r', encoding = 'UTF-8') as f:
        line_read = f.read().strip().split('\n\n')
        if n <= len(line_read):
            return line_read[n-1] + '\n\n', len(line_read)
        else:
            return None, None

choice = int(input('''If you\'re going to filfull a phonebook, type 1,
if you\'re going to transfer data to ab  new phonebook, type 2: '''))
if choice == 1:
    # fill a phonebook
    with open(source, 'a', encoding = 'UTF-8') as f:
        f.write(create_entry())
elif choice == 2:
    # put the entry read into another file
    n = int(input('Type a line number which you want to relocate: '))
    f_source, n_exist = relocate_entry(source, n)
    if f_source:
        with open(f_arrival, 'a', encoding = 'UTF-8') as f:
            f.write(f_source)
    else:
        print(f'The phonebook has less lines then number {n}.')
else:
    print('You typed neither 1 nor 2. Bye!')