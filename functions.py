info = """Hello!
I'm a contact book assistant bot. I can create and modify entries in the contact book.
I can execute the following commands:
"hello" or "help" - show information about myself (enter "help" or "hello");
"add" - add a contact record (enter "add contact_name contact_phone");
"change" - change the contact record (enter "change existing_contact_name new_contact_phone");
"phone" - show the phone number of the contact (enter "phone existing_contact_name");
"show all" - show all entries in the contact book (enter "show all");
"good bye", "close", "exit" - I complete the work (enter "good bye" or "close" or "exit")."""


def decor(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Sorry, wrong command. Look \"help\" and try again"

    return wrapper


contacts = {}


@decor
def add(*args):
    name = args[0]
    phone = args[1]
    if name in contacts:
        return "The name {name} already exist. You have enter a unique name"
    else:
        contacts[name] = phone
        return f"This is ADD command\nName {name}, phone {phone}"

@decor
def change(*args):
    name = args[0]
    phone = args[1]
    if name in contacts:
        contacts[name] = phone
        return f"This is CHANGE command\nName {name}, new phone {phone}"
    else:
        return f"There is no contact with the name {name}"


def show_phone(*args):
    name = args[0]
    if name in contacts:
        return f"This is SHOW PHONE command\nThe phone for name {name} is {contacts[name]}"
    else:
        return f"There is no contact with the name {name}"


def show_all(*args):
    new_string = ""
    print("This is SHOW ALL command")
    if contacts:
        for name, phone in contacts.items():
            new_string += f"name {name}, phone number {phone}\n"
        return new_string
    else:
        return "The Contact Book is empty"


def greatings(*args):
    return info


def help(*args):
    return info


COMMANDS = {add: "add", change: "change", show_phone: "phone", show_all: "show all", greatings: "hello", help: "help"}


def command_parser(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split(" ")
    return None, None
