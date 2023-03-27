contacts = {}
bye = ["good bye", "close", "exit"]

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            print(f"Invalid input: KeyError '{e.args[0]}'")
        except ValueError as e:
            print(f"Invalid input: ValueError '{e.args[0]}'")
        except IndexError as e:
            print(f"Invalid input: IndexError '{e.args[0]}'")
    return inner

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' with phone '{phone}' added.")

@input_error
def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Phone number for contact '{name}' changed.")
    else:
        print(f"Contact '{name}' not found.")

@input_error
def show_phone(name):
    if name in contacts:
        print(f"Phone number for contact '{name}': {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

@input_error
def give_me_all():
    if len(contacts) == 0:
        print('Your contacts are empty')
    for name, phone in contacts.items():
        print(f'names >>> {name} and numbers >>>{phone} of all contacts')

@input_error
def handler(command):
    if command.startswith("add"):
        data = command[len("add "):].split(" ")
        if len(data) == 2:
            add_contact(data[0], data[1])
        else:
            print("Invalid input: add command requires two arguments.")
    elif command.startswith("change"):
        data = command[len("change "):].split(" ")
        if len(data) == 2:
            change_contact(data[0], data[1])
        else:
            print("Invalid input: change command requires two arguments.")
    elif command.startswith("phone"):
        data = command[len("phone "):]
        show_phone(data)
    elif command.startswith("show all"):
        give_me_all()
    else:
        print("Invalid command. Please try again.")

def primitive_bot():
    while True:
        user_input = input('welcome app: ').lower()
        if user_input in bye:
            print("Good bye!")
            break
        else:
            handler(user_input)

if __name__ == "__main__":
    primitive_bot()
    