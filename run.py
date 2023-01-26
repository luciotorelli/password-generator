import random
import string
import time
import pyfiglet
from colorama import Fore, Style
import os


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
    print(Fore.BLUE + Style.DIM + pyfiglet.figlet_format("Passgen"))
    print(pyfiglet.figlet_format("by Lucio Torelli", font="digital"))
    # Resets Colorama style
    print(Style.RESET_ALL)
    print(
        Fore.YELLOW + Style.DIM + "Hey there! I am passgen, a bot",
        "that will generate a password for you.",
    )
    print(
        Fore.YELLOW + Style.DIM + "Enter the number of characters",
        "you want between 3 and 100 and hit enter.\n",
    )

    while True:
        try:
            # Requests the password length from the user,
            # Assigns to variable password_length
            # Make input integer
            # Make text colored and styled normal for user input
            password_length = int(input(Fore.WHITE + Style.NORMAL))

            # Check if the password is higher than 100
            # or lower than 3, if so, raise ValueError
            if password_length > 100 or password_length < 3:
                raise ValueError

            # Clears terminal
            os.system("cls")
            # Print how many characters user selected.
            print(
                Fore.YELLOW
                + Style.DIM
                + f"Your password will have {password_length} characters"
            )

            # Returns the password_length
            return password_length

        # Raise ValueError if a character other than a number,
        # higher than 100 or lower than 3 is input by the user
        except ValueError:
            print(
                Fore.RED + Style.DIM + "No no no... I said a number between 3 and 100.",
                "Try again and hit enter.",
            )


def get_password_strength():
    """
    Get password strength input from the user.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be an integer between 1 to 3.
    The loop will repeatedly request data, until it is valid.
    """
    print(
        Fore.YELLOW + Style.DIM + "What level of strength should your password have?",
        "I would recommend level 3! :) \n",
    )
    print(Fore.YELLOW + Style.DIM + "Type 1 for Only letters")
    print(Fore.YELLOW + Style.DIM + "Type 2 for Letters and numbers")
    print(Fore.YELLOW + Style.DIM + "Type 3 for Letters, numbers and characters\n")

    while True:
        try:
            # Requests the password strength from the user,
            # Assigns to variable password_strength
            # Make input integer
            password_strength = int(input(Fore.WHITE + Style.NORMAL))

            # Check if the level is higher than 3
            # or lower than 1, if so, raise ValueError
            if password_strength > 3 or password_strength < 1:
                raise ValueError

            # Check strength level selected
            # by user to phrase the result correctly
            if password_strength == 1:
                # Clears terminal
                os.system("cls")
                print(
                    Fore.YELLOW
                    + Style.DIM
                    + f"You selected level {password_strength}, ",
                    "your password will contain only letters",
                )
            elif password_strength == 2:
                # Clears terminal
                os.system("cls")
                print(
                    Fore.YELLOW
                    + Style.DIM
                    + f"You selected level {password_strength}, ",
                    "your password will contain letters and numbers.",
                )
            else:
                # Clears terminal
                os.system("cls")
                print(
                    Fore.YELLOW
                    + Style.DIM
                    + f"You selected level {password_strength}, ",
                    "your password will contain letters,",
                    "numbers and characters.",
                )

            # Returns the password_strength
            return password_strength

        # Raise ValueError if a character other than a number,
        # higher than 3 or lower than 1 is input by the user
        except ValueError:
            print(
                Fore.RED + Style.DIM + "Hey! I said a number between 1 and 3",
                ", try again and hit enter!",
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
    print(Fore.YELLOW + Style.DIM + "Bip bop boop... computing your password...")
    print("...")
    # Pauses the program for 1 second then resumes.
    time.sleep(1)
    print("...")
    # Pauses the program for 1 second then resumes.
    time.sleep(1)
    print("I hope you are still there...")
    print("...")
    # Pauses the program for 1 second then resumes.
    time.sleep(1)

    print("Phew! This was hard. Here is your password:\n")
    # Pauses the program for 1 second then resumes.
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT + password)
    # Resets colorama style
    print(Style.RESET_ALL)


def main():
    """
    Run all program functions
    """
    password_length = get_password_length()
    password_strength = get_password_strength()
    password = generate_password(password_length, password_strength)
    print_password(password)


main()
