"""
Password Generator is a Python app that runs on a terminal. It creates a password based on the amount of characters requested by the user and a password strength of 3 levels.
* Letters only.
* Letters and numbers.
* Letters, numbers and special characters.
"""


def get_password_length():
    """
    Get password length input from the user.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be an integer between 1 to 100.
    The loop will repeatedly request data, until it is valid.
    """
    print(
        "Please enter how many characters you want your password to have.\n"
    )
    print("You should type a number between 1 and 100\n")

    while True:
        try:
            # Requests the password length from the user,
            # Assigns to variable password_length
            # Make input integer
            password_length = int(input("Enter your number here:\n"))
            
            # Check if the password is higher than 100 or lower than 1, if so, raise ValueError
            if password_length > 100 or password_length < 1:
                raise ValueError

            # Check if the user selected 1 or more characters to phrase the result correctly
            if password_length == 1:
                print(f"You selected {password_length} character")
            else:
                print(f"You selected {password_length} characters")
            
            #Returns the password_length
            return password_length

        # Raise ValueError if a character other than a number, higher than 100 or lower than 1 is input by the user
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")


def main():
    """
    Run all program functions
    """
    get_password_length()


print("Welcome to Password Generator")
main()