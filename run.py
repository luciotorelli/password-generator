import random
import string
import time

"""
Password Generator is a Python app that runs on a terminal. It creates a password based on the amount of characters requested by the user and a password strength of 3 levels.
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
    
    print("Hey there! I am passgen, a very basic bot that will generate a password for you.")
    print(
        "Please enter how many characters you want your password to have, select a number between 3 and 100.\n"
    )

    while True:
        try:
            # Requests the password length from the user,
            # Assigns to variable password_length
            # Make input integer
            password_length = int(input("Enter your number here and hit enter:\n"))
            
            # Check if the password is higher than 100 or lower than 3, if so, raise ValueError
            if password_length > 100 or password_length < 3:
                raise ValueError

            # Check if the user selected 1 or more characters to phrase the result correctly
            if password_length == 1:
                print(f"You selected {password_length} character")
            else:
                print(f"You selected {password_length} characters")
            
            #Returns the password_length
            return password_length

        # Raise ValueError if a character other than a number, higher than 100 or lower than 3 is input by the user
        except ValueError:
            print("No no no... I said a number between 3 and 100. Try again and hit enter.")


def get_password_strength():
    """
    Get password strength input from the user.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be an integer between 1 to 3.
    The loop will repeatedly request data, until it is valid.
    """
    print(
        "What level of strength should your password have? For most security I would recommend level 3! :) \n"
    )
    print("Level 1: Only letters")
    print("Level 2: Letters and numbers")
    print("Level 3: Letters, numbers and characters")
    
    print("You should type a number between 1 to 3.\n")

    while True:
        try:
            # Requests the password strength from the user,
            # Assigns to variable password_strength
            # Make input integer
            password_strength = int(input("Enter your level here:\n"))
            
            # Check if the level is higher than 3 or lower than 1, if so, raise ValueError
            if password_strength > 3 or password_strength < 1:
                raise ValueError
            
            # Check strength level selected by user to phrase the result correctly
            if password_strength == 1:
                print(f"You selected level {password_strength}, your password will contain only letters")
            elif password_strength == 2:
                print(f"You selected level {password_strength}, your password will contain letters and numbers.")
            else:
                print(f"You selected level {password_strength}, your password will contain letters, numbers and characters.")    
            
            #Returns the password_strength
            return password_strength

        # Raise ValueError if a character other than a number, higher than 3 or lower than 1 is input by the user
        except ValueError:
            print("Hey! I said a number between 1 and 3, try again and hit enter!")

def generate_password(password_length, password_strength):
    """
    Generates a password based on the length and strength requested by the user. 
    """
    
    # If user selects strength level 1
    if (password_strength == 1):
        password = ""
        i = 0
        # Adds a random letter to the password until the password_length is reached. 
        while (i < password_length ):
            password = password + random.choice(string.ascii_letters)
            i += 1
        return password

    # If user selects strength level 2
    if (password_strength == 2):
        password = ""
        i = 0
        # Adds a random letter or a random integer to the password until the password_length is reached.
        # If the iterable is even, adds a letter. Else, adds an integer. 
        while (i < password_length):
            if (i % 2):
                password = password + random.choice(string.ascii_letters)
            else:
                password = password + str(random.randint(0,9))
            i += 1
        #Shuffles the password randomly
        password = ''.join(random.sample(password, len(password)))
        
        return password
    
    # If user selects strength level 1            
    if (password_strength == 3):
        password = ""
        # Creates a list of special characters, string.punctuation could be used instead if you don't want to specify the special characters.
        special_characters = ('$', '#', '@', '!','%','^','&','*')
        i = 0
        # Adds a random letter, integer or character to the password until the password_length is reached.
        # If the iterable is even, adds a letter. If it's divisible by 3, adds a special character. Else, adds an integer. 
        while (i < password_length):
            if (i % 2):
                password = password + random.choice(string.ascii_letters)
            elif(i % 3 == 0):
                password = password + random.choice(special_characters)
            else:
                password = password + str(random.randint(0,9))
            i += 1
        #Shuffles the password randomly    
        password = ''.join(random.sample(password, len(password)))
        
        return password        

def print_password(password):
    print(f"Bip bop boop... computing your password...")
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(3)
    print(f"I hope you are still there, working hard on this...")
    print("...")
    time.sleep(4)
    
    print(f"Phew! This was hard. Here is your password:\n")
    print("_______________________")
    print(password)
    print("_______________________")

def main():
    """
    Run all program functions
    """
    password_length = get_password_length()
    password_strength = get_password_strength()
    password = generate_password(password_length, password_strength)
    print_password(password)

main()