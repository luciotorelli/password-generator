import random
import string
import time
import pyfiglet
from colorama import Fore, Style
import os
import sys

"""Password Generator is a Python app that runs on a terminal.
It creates a password based on the amount of characters requested
by the user and a password strength of 3 levels.
1 Letters only.
2 Letters and numbers.
3 Letters, numbers and special characters.
"""


def get_password_length():
    """
    Get password length input from the user.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be an integer between 3 to 100.
    The loop will repeatedly request data, until it is valid.
    """

    # Uses Colorama and PyFiglet to style the text
    print(Fore.BLUE + pyfiglet.figlet_format("Passgen"))
    print(pyfiglet.figlet_format("by Lucio Torelli", font="digital"))
    # Resets Colorama style
    print(Style.RESET_ALL)
    # Sets text color yellow
    print(Fore.YELLOW +
        "Hey there! I am passgen, a bot that will generate a password for you."
    )
    print("You can type exit or restart at any point during the program run.")
    print(
        "Enter the number of characters "
        + "you want between 3 and 100 and hit enter."
    )

    while True:
        try:
            # Requests the password length from the user,
            # Assigns to variable password_length
            # Make text colored white for user input
            password_length = input(Fore.WHITE)

            # Checks if user wants to restart or exit
            # else, assigns the user input to password_length
            if password_length == "restart" or password_length == "reset":
                restartProgram()
                break
            elif password_length == "exit" or password_length == "close":
                closeProgram()
                break
            else:
                password_length = int(password_length)

            # Check if the password is higher than 100
            # or lower than 3, if so, raise ValueError
            if password_length > 100 or password_length < 3:
                raise ValueError

            # Sends Clear Terminal command based on Operating System
            os.system("cls" if os.name == "nt" else "clear")
            # Print how many characters user selected.
            print(Fore.YELLOW + f"Your password will have {password_length} characters.\n")

            # Returns the password_length
            return password_length

        # Raise ValueError if a character other than a number,
        # higher than 100 or lower than 3 is input by the user
        except ValueError:
            print(Fore.RED +
                "No no no... I said a number between 3 and 100. "
                + "Try again and hit enter.\n"
            )


def get_password_strength():
    """
    Get password strength input from the user.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be an integer between 1 to 3.
    The loop will repeatedly request data, until it is valid.
    """
    print( Fore.YELLOW +
        "What level of strength should your password have? "
        + "I would recommend level 3! :) \n",
    )
    print(Fore.YELLOW + "Type 1 for Only letters")
    print(Fore.YELLOW + "Type 2 for Letters and numbers")
    print(Fore.YELLOW + "Type 3 for Letters, numbers and characters\n")

    while True:
        try:
            # Requests the password strength from the user,
            # Assigns to variable password_strength
            password_strength = input(Fore.WHITE)

            # Checks if user wants to restart or exit
            # else, assigns the user input to password_strength as integer
            if password_strength == "exit" or password_strength == "close":
                closeProgram()
                break
            elif password_strength == "restart" or password_strength == "reset":
                restartProgram()
                break
            else:
                password_strength = int(password_strength)

            # Check if the level is higher than 3
            # or lower than 1, if so, raise ValueError
            if password_strength > 3 or password_strength < 1:
                raise ValueError

            # Check strength level selected
            # by user to phrase the result correctly
            if (
                password_strength == 1
                or password_strength == 2
                or password_strength == 3
            ):
                # Sends Clear Terminal command based on Operating System
                os.system("cls" if os.name == "nt" else "clear")
                print(Fore.YELLOW + f"You selected level {password_strength}\n")

            # Returns the password_strength
            return password_strength

        # Raise ValueError if a character other than a number,
        # higher than 3 or lower than 1 is input by the user
        except ValueError:
            print(Fore.RED +
                "Hey! I said a number between 1 and 3" + ", try again and hit enter!\n"
            )


def generate_password(password_length, password_strength):
    """
    Generates a password based on the
    length and strength requested by the user.
    """

    # If user selects strength level 1
    if password_strength == 1:
        password = ""
        i = 0
        # Adds a random letter to the password
        # until the password_length is reached.
        while i < password_length:
            password = password + random.choice(string.ascii_letters)
            i += 1
        return password

    # If user selects strength level 2
    if password_strength == 2:
        password = ""
        i = 0
        # Adds a random letter or a random integer
        # to the password until the password_length is reached.
        # If the iterable is even, adds a letter. Else, adds an integer.
        while i < password_length:
            if i % 2:
                password = password + random.choice(string.ascii_letters)
            else:
                password = password + str(random.randint(0, 9))
            i += 1
        # Shuffles the password randomly
        password = "".join(random.sample(password, len(password)))

        return password

    # If user selects strength level 1
    if password_strength == 3:
        password = ""
        # Creates a list of special characters,
        # string.punctuation could be used instead
        # if you don't want to specify the special characters.
        special_characters = ("$", "#", "@", "!", "%", "^", "&", "*")
        i = 0
        # Adds a random letter, integer or character
        # to the password until the password_length is reached.
        # If the iterable is even, adds a letter.
        # If it's divisible by 3, adds a special character.
        # Else, adds an integer.
        while i < password_length:
            if i % 2:
                password = password + random.choice(string.ascii_letters)
            elif i % 3 == 0:
                password = password + random.choice(special_characters)
            else:
                password = password + str(random.randint(0, 9))
            i += 1
        # Shuffles the password randomly
        password = "".join(random.sample(password, len(password)))

        return password


def print_password(password):
    """
    Prints the password on the console for the user.
    """
    print(Fore.YELLOW + "Bip bop boop... computing your password\n")
    time.sleep(0.2)
    print("...\n")
    print("I hope you are still there...\n")
    time.sleep(0.2)
    print("...\n")
    time.sleep(0.2)
    print("Phew! This was hard. Here is your password:\n")

    print(Fore.YELLOW + Style.BRIGHT)
    print(password)

    print(Fore.YELLOW + Style.NORMAL)
    print("\nWould you like to restart the program? Type yes or no.\n")

    while True:
        try:
            # Requests user decision to stop the program or,
            # to restart it.
            # Make text colored white for user input
            restart = input(Fore.WHITE)

            # Check if the user decided to restart
            # or to close the program
            if (
                restart == "yes"
                or restart == "y"
                or restart == "Yes"
                or restart == "restart"
            ):
                restartProgram()
            elif (
                restart == "no"
                or restart == "n"
                or restart == "No"
                or restart == "close"
            ):
                closeProgram()
            else:
                raise ValueError
            # Returns to stop while loop
            return

        # If the user inputs anything other than
        # yes or no, prints error.
        except ValueError:
            print(
                Fore.RED + "I can't recognize this command.",
                "Try yes or no and hit enter.",
            )

def restartProgram():
    """
    Resets the style, clears the terminal and restart the program
    """
    print(Style.RESET_ALL)
    os.system("cls" if os.name == "nt" else "clear")
    os.system('python3 "run.py"')


def closeProgram():
    """
    Sets terminal to Yellow, prints a warning message,
    clear the terminal and close the program
    """
    print(Fore.YELLOW + "\nThe program will be closed...")
    print(Style.RESET_ALL)
    time.sleep(0.5)
    sys.exit(0)


def main():
    """
    Run all program functions
    """
    password_length = get_password_length()
    password_strength = get_password_strength()
    password = generate_password(password_length, password_strength)
    print_password(password)


main()