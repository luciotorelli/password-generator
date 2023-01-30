"""
Imports module
    random
        this module implements pseudo-random number generators
        for various distributions. It is used in this project to
        generate random integers, strings and characters.
    string
        Python String module contains some constants,
        utility function and classes for string manipulation.
        It is used in this project to manipulate the password.
    time
        this module provides various time-related functions.
        It is used in this project to sleep the program while
        the bot is typing the final messages.
    pyfiglet
        pyfiglet is a full port of FIGlet into pure python.
        It takes ASCII text and renders it in ASCII art fonts. It is used in
        this project to display the first message.
    colorama
        Makes ANSI escape character sequences
        (for producing colored terminal text and cursor positioning).
        It is used in this project to differentiate errors, bot messages
        and user input.
    os
        This module provides a portable way of using
        operating system dependent functionality.
        It is used in this project to clear the terminal in-between functions.
    sys
        This module provides access to some variables used or maintained by
        the interpreter and to functions that interact strongly with the
        interpreter.
        It is used in this project to call sys.exit() to close the program.
"""

import random
import string
import time
import pyfiglet
from colorama import Fore, Style
import os
import sys


def get_password_length():
    """Gets password length from a user input.

    Runs a while loop to collect valid data from the user
    via the terminal, which must be an integer between 3 and 100.
    The loop will repeatedly request data until it is valid.

    Returns
    -------
    password_length
        the length the password will have as an integer number.
    """

    # Uses Colorama and PyFiglet to style the app logo
    print(Fore.BLUE + pyfiglet.figlet_format("Passgen"))
    print(pyfiglet.figlet_format("by Lucio Torelli", font="digital"))
    # Resets Colorama style
    print(Style.RESET_ALL)
    # Sets text color yellow and prints a welcome message
    print(
        Fore.YELLOW
        + "Hey there! I am passgen, a bot that will"
        + " generate a password for you."
    )
    print(
        "If you want to exit or restart the program"
        + " you can type exit or restart\nat any point."
    )
    print(
        "Enter the number of characters "
        + "you want between 3 and 100 and hit enter."
    )

    while True:
        try:
            password_length = input(Fore.WHITE)

            # Checks if user wants to restart or exit
            # else, assigns the user input to password_length as an integer
            if password_length == "restart" or password_length == "reset":
                restart_program()
                break
            elif password_length == "exit" or password_length == "close":
                close_program()
                break
            else:
                password_length = int(password_length)

            if password_length > 100 or password_length < 3:
                raise ValueError

            # Sends clear terminal command based on Operating System
            os.system("cls" if os.name == "nt" else "clear")
            print(
                Fore.YELLOW
                + f"Your password will have {password_length} characters.\n"
            )

            return password_length

        except ValueError:
            print(
                Fore.RED
                + "No no no... I said a number between 3 and 100. "
                + "Try again and hit enter.\n"
            )


def get_password_strength():
    """Gets password length from a user input.

    Runs a while loop to collect valid data from the user
    via the terminal, which must be an integer between 1 and 3.
    The loop will repeatedly request data until it is valid.

    Returns
    -------
    password_strength
        the strength level the password will have as an integer number.
    """

    print(
        Fore.YELLOW
        + "What level of strength should your password have? "
        + "I would recommend level 3! :)\n",
    )
    print(Fore.YELLOW + "Type 1 for letters only.")
    print(Fore.YELLOW + "Type 2 for letters and numbers.")
    print(Fore.YELLOW + "Type 3 for letters, numbers and characters.\n")

    while True:
        try:
            password_strength = input(Fore.WHITE)

            # Checks if user wants to restart or exit
            # else, assigns the user input to password_strength as an integer
            if password_strength == "exit" or password_strength == "close":
                close_program()
                break
            elif (
                password_strength == "restart" or password_strength == "reset"
            ):
                restart_program()
                break
            else:
                password_strength = int(password_strength)

            if password_strength > 3 or password_strength < 1:
                raise ValueError

            if (
                password_strength == 1
                or password_strength == 2
                or password_strength == 3
            ):
                # Sends clear terminal command based on Operating System
                os.system("cls" if os.name == "nt" else "clear")
                print(
                    Fore.YELLOW
                    + f"You selected strength level {password_strength}.\n"
                )

            return password_strength

        except ValueError:
            print(
                Fore.RED
                + "Hey! I said a number between 1 and 3"
                + ", try again and hit enter!\n"
            )


def get_special_characters():
    """Gets a list of special characters.

    Runs a while loop to collect valid data from the user
    via the terminal, which must be custom or default.
    The loop will repeatedly request data until it is valid.

    Returns
    -------
    special_characters
        a list of special characters to be considered when randomizing
        the password.
    """

    print(
        Fore.YELLOW + "Please note this list of characters will be used to",
        "randomize the password\n"
        + "but not all of them may be included in the password.",
    )
    print(Fore.YELLOW + "Default List: $#@!%^&*")
    print(
        Fore.YELLOW
        + "Would you like to use the default list or type a custom list?"
        + "\nType default or custom."
    )

    while True:
        try:
            list_type = input(Fore.WHITE)

            # Checks if user wants to restart, exit
            # or to assign a list type of custom or default
            # else, raises ValueError
            if list_type == "exit" or list_type == "close":
                close_program()
            elif list_type == "restart" or list_type == "reset":
                restart_program()
                break
            elif list_type == "default" or list_type == "Default":
                special_characters = (
                    "$", "#", "@", "!", "%", "^", "&", "*")
            elif list_type == "custom" or list_type == "Custom":
                special_characters = get_custom_special_characters()
            else:
                raise ValueError

            return special_characters

        except ValueError:
            print(
                Fore.RED
                + "Not quite! You need to type default or custom"
                + ", try again and hit enter!\n"
            )


def get_custom_special_characters():
    """Gets a list of custom special characters.

    Runs a while loop to collect valid data from the user
    via the terminal, which must be a valid special character list.
    The loop will repeatedly request data until it is valid.

    Returns
    -------
    special_characters
        a list of special characters to be considered when randomizing
        the password.
    """

    print(
        Fore.YELLOW
        + "Type your special character list, "
        + "do not space or separate characters."
    )
    print(Fore.YELLOW + "Special characters supported: !\"#$%&'()*+,-./:;"
          + "<=>?@[]^_`{|}~\\")

    while True:
        try:
            user_characters = input(Fore.WHITE)
            # Assigns every punctuation available
            # on string.punctuation to special_characters as a list
            special_characters = list(string.punctuation)

            # Checks if user wants to restart or exit
            if user_characters == "exit" or user_characters == "close":
                close_program()
                break
            elif user_characters == "restart" or user_characters == "reset":
                restart_program()
                break

            # Check if user entered an empty input
            if user_characters == "":
                raise ValueError

            # Converts to a set to ensure no duplicates
            # then converts it to a list
            custom_special_characters = list(set(user_characters))

            # Checks if user typed a valid special character list then
            # returns special_characters else, raises ValueError
            if all(
                character in special_characters
                for character in custom_special_characters
            ):
                special_characters = custom_special_characters
                print(
                    Fore.YELLOW
                    + f"You selected the characters: "
                    + ("".join(special_characters))
                )
                return special_characters
            else:
                raise ValueError

        except ValueError:
            print(
                Fore.RED
                + "Nope! You need to type special characters such as !@%^",
                ", try again and hit enter!\n",
            )


def generate_password(password_length, password_strength):
    """Generates a password

    Uses the requested password_length
    and password_strength to generate a randomized password.
    If password_strength level 3 is selected, it will also use
    a list of special characters.

    Parameters
    ----------
    password_length : integer
        the length the password will have as an integer number.
    password_strength : integer
        the strength level the password will have as an integer number.

    Returns
    -------
    password
        a randomized password based on the user requirements.
    """

    if password_strength == 1:
        password = ""
        i = 0
        # Adds a random letter to the password
        # until the password_length is reached.
        while i < password_length:
            password = password + random.choice(string.ascii_letters)
            i += 1
        return password

    if password_strength == 2:
        password = ""
        i = 0
        # Until the password_length is reached
        # adds a letter to the password if the iterable is even.
        # Else, adds an integer to the password.
        while i < password_length:
            if i % 2:
                password = password + \
                    random.choice(string.ascii_letters)
            else:
                password = password + str(random.randint(0, 9))
            i += 1
        # Shuffles the password randomly
        password = "".join(random.sample(password, len(password)))

        return password

    if password_strength == 3:
        password = ""

        i = 0
        # Adds a random letter, integer or character
        # to the password until the password_length is reached.
        # If the iterable is even, adds a letter.
        # If it's divisible by 3, adds a special character.
        # Else, adds an integer.

        special_characters = get_special_characters()
        while i < password_length:
            if i % 2:
                password = password + \
                    random.choice(string.ascii_letters)
            elif i % 3 == 0:
                password = password + \
                    random.choice(special_characters)
            else:
                password = password + str(random.randint(0, 9))
            i += 1
        # Shuffles the password randomly
        password = "".join(random.sample(password, len(password)))

        return password


def print_password(password):
    """Prints the password to the console.

    Parameters
    ----------
    password : string
        a randomized password based on the user requirements.
    """

    print(Fore.YELLOW + "Bip bop boop... computing your password.\n")
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
            restart = input(Fore.WHITE)

            # Check if the user wants to restart
            # or to close the program
            if (
                restart == "yes"
                or restart == "y"
                or restart == "Yes"
                or restart == "restart"
            ):
                restart_program()
            elif (
                restart == "no"
                or restart == "n"
                or restart == "No"
                or restart == "close"
                or restart == "exit"
            ):
                close_program()
            else:
                raise ValueError
            # Returns to stop while loop
            return

        except ValueError:
            print(
                Fore.RED + "I can't recognize this command.",
                "Try yes or no and hit enter.",
            )


def restart_program():
    """Restarts the program

    Resets the style and
    clears the terminal before restarting
    the program.
    """

    print(Style.RESET_ALL)
    os.system("cls" if os.name == "nt" else "clear")
    os.system('python3 "run.py"')


def close_program():
    """Closes the program

    Sets terminal to yellow, prints a warning message,
    clears the terminal and closes the program.
    """

    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.YELLOW + "\nThe program is now closed.")
    sys.exit()


def main():
    """Runs all program functions

    Sends clear terminal command based on Operating System
    before running all functions.
    """

    os.system("cls" if os.name == "nt" else "clear")

    password_length = get_password_length()
    password_strength = get_password_strength()
    password = generate_password(password_length, password_strength)
    print_password(password)


main()
