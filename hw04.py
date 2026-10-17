# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# -----------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Ask for text until the secret word or dog is found """
    while True:
       # Get a sentence from the user
        sentence = input("Give me a sentence: ")
       
       #Check the secret word first
        if secret_word in sentence:
            print("You used the secret word!")
            return
        
        
       #Check for dog with either specified capitalization
        elif "dog" in sentence or "Dog" in sentence:
           print('You used the word "dog" or the word "Dog"!')
           return
        
        
        #Repeat if neither word is found
        else:
           print("Try again")



# Task 2
def check_greater():
    """Compare two integers until they are different. """
    while True:
        # Get two integers from the user
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))
        
        # Compare the two integers
        if first > second:
            print("First is Greater")
            return
        elif second > first:
            print("Second is Greater")
            return
        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """Print odd multiples of 3 from 1 to 40, excluding multiples of 5."""
    for number in range(1, 41):
        # Skip even numbers
        if number % 2 == 0:
            continue

        # Skip numbers that are not multiples of 3
        if number % 3 != 0:
            continue

        # Skip multiples of 5
        if number % 5 == 0:
            continue

        # Print numbers that pass all three conditions
        print(number)

# Task 4.a
def my_for_loop():
    """Classify each character in a valid string as a vowel or consonant."""
    word = input("Give me a string: ")

    # Check the length and whether the string contains spaces
    if len(word) < 2 or len(word) > 5 or " " in word:
        print("bad word")
        return

    # Check each character in the string
    for letter in word:
        if letter in "aeiouAEIOU":
            print("letter", letter, "is a vowel")
        else:
            print("letter", letter, "is a consonant")

# Task 4.b
def my_while_loop():
    """Repeat the menu until the user chooses b or c."""
    while True:
        # Ask the user to choose an option
        choice = input("Choose one option: a, b, or c: ")

        if choice == "a":
            continue
        elif choice == "b":
            print("Goodbye")
            return
        elif choice == "c":
            sys.exit()
        else:
            print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
