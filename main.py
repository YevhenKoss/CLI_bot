from functions import *

exit_words = ["good bye", "close", "exit"]


def main():
    while True:
        user_input = input(">>>").casefold()
        if user_input in exit_words:
            print("Good bye!")
            break
        command, data = command_parser(user_input)

        if not command:
            print("Sorry, unknown command")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()
