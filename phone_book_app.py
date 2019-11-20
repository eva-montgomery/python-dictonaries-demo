# Phone Book App
# You will write a command line program to manage a phone book. When you start the phonebook.py program, 
# it will print out a menu and ask the user to enter a choice:

# $ python3 phonebook.py
# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

def print_phonebook():
    if len(phone_book) == 0:
        print("You have no entries.")
    else:
        for count, phone in enumerate(phone_book):
            print(f"{count}: {name}")    

# I neeed a way to add new entries.
def add_entry(entry, item):
    # We receive a new entry, which is a string
    phone_book.append(name)

def delete_entry(entry, item):
    # del todo_list[index]
    try: 
        phone_book.pop(index)
    except IndexError:
        print(" 🐒 Sorry, we couldn't find that that one")

def main():
    menu = """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """

    print(menu)


def get_choice(prompt="Chose one: "):    
    is_valid_choice = True
    choice = 0
    while not is_valid_choice:
        try:
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Please enter a number: ")
    return choice        

def main():
    phone_book = [] 

    is_running = True
    while is_running:
        print(main)
        # What do you want to do (1-5)?
        choice = input("What do you want to do (1-5)? ")
        if choice == "1":
            # If they choose to look up an entry, you will ask them for the person's name, and then look up 
            # the person's phone number by the given name and print it to the screen.
            look_up = input("Please chose the name you want to look up: ")
            print_phonebook(phone_book)
        elif choice == "2":
            # If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
            new_number = input("Please enter the name and number: ")
            add_number(phone_book, add_number)
        elif choice == "3":
            # If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
            index_to_delete = input("Enter the name you want to delete: ")
            delete_entry(phone_book, index_to_delete)
        elif choice == "4":
            # If they choose to list all entries, you will go through all entries in the dictionary 
            # and print each out to the terminal.
            print_phonebook(phone_book)
        elif choice == "5":
            # If they choose to quit, end the program.
            is_running = False
            print("Bye")


main()        







