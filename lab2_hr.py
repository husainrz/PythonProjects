# Husain Rizvi

# SDEV 300 - Lab 2 - Math and Secret Generation

"""This program is a menu-driven application that provides users
with the ability to perform several math and security related functions."""

import string   # importing string library
import secrets  # importing secrets library
import datetime     # importing datetime library
from datetime import date   # importing date from datetime library
import math     # importing math library

# Creating constants for menu options

SEC_PWD = 1     # First choice (Generate Secure Password)
PERCENTAGE_CALC = 2     # Second choice (Calculate and Format a Percentage)
DAYS_CALC = 3    # Third choice (How many days from today until July 4, 2025?)
LAW_COSINES = 4     # Fourth choice (Use the Law of Cosines to calculate the leg of a triangle)
VOLUME_CALC = 5     # Fifth choice (Calculate the volume of a Right Circular Cylinder)
EXIT_PROGRAM = 6    # Sixth choice (Exit program)

# Start of sec_password() function definition

def sec_password():

    # 1. Generate Secure Password

    """The sec_password() function prompts the user for their desired
     length of the password to be created and generates a secure password."""

    # Prompting the user for their desired length of the password
    # Storing user input in length1 variable

    length1 = input("\nWhat length should the password be? (How many characters?): \n")

    # Calling int_validation() function to ensure user input is only numeric characters

    if int_validation(length1):

        # Creating length variable and converting length1 variable from a string into an int

        length = int(length1)

        # Creating characters variable that includes all the string letters,
        # all the string digits, and all the string punctuation characters

        characters = string.ascii_letters + string.digits + string.punctuation

        # Creating password variable and using secrets.choice to return a
        # randomly-chosen element from a non-empty sequence (characters)

        # Using for loop and the range() function to ensure user's desired length
        # is the actual length for the generated password

        password = ''.join(secrets.choice(characters) for i in range(length))

        # Displaying user's secure password

        print(f'Secure Password: {password}')

# Start of get_numerator() function definition

def get_numerator():

    """The get_numerator() function prompts user for a numerator
    and returns the user's input through a while loop to ensure
    user input is valid."""

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through numerator prompt

        # Prompting user for a numerator and storing in numerator1 variable

        numerator1 = input("Please enter the numerator you would "
                           "wish to use to calculate the percentage: ")

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(numerator1):

            # Creating numerator variable and converting numerator1
            # variable from a string into an int

            numerator = int(numerator1)

            return numerator    # Returning user input in numerator variable

# Start of get_denominator() function definition

def get_denominator():

    """The get_denominator() function prompts user for a denominator
    and returns the user's input through a while loop to ensure
    user input is valid."""

    running = True   # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through denominator prompt

        # Prompting user for a denominator and storing in denominator1 variable

        denominator1 = input("Please enter the denominator you would "
                             "wish to use to calculate the percentage: ")

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(denominator1):

            # Creating denominator variable and converting denominator1
            # variable from a string into an int

            denominator = int(denominator1)

            return denominator    # Returning user input in denominator variable

# Start of dec_format() function definition

def dec_format():

    """The dec_format() function prompts user for the number of decimal points
    for formatting the percentage and returns the user's input through a
    while loop to ensure user input is valid."""

    running = True     # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through dec_format prompt

        # Prompting user for the number of decimal points for formatting the percentage
        # Storing user input into dec_format1 variable

        dec_format1 = input("Please enter the number of decimal points "
                            "for formatting the percentage: ")

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(dec_format1):

            # Creating dec_format2 variable and converting dec_format1
            # variable from a string into an int

            dec_format2 = int(dec_format1)

            return dec_format2   # Returning user input in dec_format2 variable

# Start of percentage_calc() function definition

def percentage_calc():

    # 2. Calculate and Format a Percentage

    """The percentage_calc() function prompts the user for their desired
    numerator, denominator, and number of decimal points for formatting
    the percentage and then calculates, formats, and displays the percentage."""

    # Calling the get_numerator() and get_denominator() functions to calculate
    # the percentage, dividing get_numerator() value with get_denominator() value
    # and then multiplying the result by 100 and storing the value in the percentage variable

    percentage = (get_numerator() / get_denominator()) * 100

    # Using the round() function to format the function and round it to the value of
    # the dec_format() function, which is the number the user chose and storing
    # the new value in the updated percentage variable

    percentage = round(percentage, dec_format())

    # Displaying the calculated percentage

    print(f'Calculated percentage: {percentage}%')

# Start of days_calc() function definition

def days_calc():

    # 3. How many days from today until July 4, 2025?

    """The days_calc() function calculates and outputs the number of days
    from today until July 4th, 2025."""

    year = 2025     # Creating year variable with value of 2025

    month = 7   # Creating month variable with value of 7

    day = 4     # Creating day variable with value of 4

    # Using datetime.date(year, month, day) to store the desired
    # date into the until_date variable

    until_date = datetime.date(year, month, day)

    # Using the class method date.today() to return the current local date
    # And storing the date in the today variable

    today = date.today()

    # Calculating the number of days from today until July 4th, 2025
    # by subtracting until_date with today and storing the value in days_until variable

    days_until = until_date - today

    # Outputting the calculated number of days until July 4th, 2025

    print(days_until)

# Start of law_cosines() function definition

def law_cosines():

    # 4. Use the Law of Cosines to calculate the leg of a triangle.

    """The law_cosines() function uses the law of cosines to
    calculate the leg of a triangle. The triangle that we are
    using has side 'a' equal to 8, side 'b' equal to 11, and side 'c'
    is what we are solving for. The angle for C is 37 degrees radians."""

    # Formula for the Law of Cosines is c^2 = a^2 + b^2 - 2ab*cos(C)
    # For this problem, a = 8, b = 11, and C = 37, and we are solving for c

    side_a = 8   # Creating variable side_a for side 'a' that is equal to 8
    side_b = 11  # Creating variable side_b for side 'b' that is equal to 11

    # Calculating the value of cos(C), which is cos(37)
    # Using math cos() trigonometric function to return the cosine of 37 radians
    # Using math radians() angular conversion  function to convert angle C (37)
    # from degrees to radians

    cosine = math.cos(math.radians(37))

    # Calculating the value of side c
    # Using math pow(x, y) power function to return x raised to the power y (a^2 & b^2)
    # We solve the function here and input the value in side_c2, which is (c^2)

    side_c2 = math.pow(side_a, 2) + math.pow(side_b, 2) - (2 * side_a * side_b * cosine)

    # Since side_c2 is essentially c^2 we would need to get the square root of side_c2 to find c
    # Using math sqrt() function to return the square root of side_c2 and storing value in side_c

    side_c = math.sqrt(side_c2)

    # Displaying the value of side_c and formatting it to two decimal points

    print(f'The calculated value of the leg of the triangle (c) is {side_c:.2f}')

# Start of get_radius() function definition

def get_radius():

    """The get_radius() function prompts user for a radius of the
    right circular cylinder and returns the user's input through
    a while loop to ensure user input is valid."""

    running = True   # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through radius prompt

        # Prompting user for a radius for the right circular cylinder
        # Storing user input in radius1 variable

        radius1 = input("Please enter a radius for the right circular cylinder: ")

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(radius1):

            # Creating radius variable and converting radius1 variable from a string into an int

            radius = int(radius1)

            return radius    # Returning user input in radius variable

# Start of get_height() function definition

def get_height():

    """The get_height() function prompts user for a height of the
    right circular cylinder and returns the user's input through
    a while loop to ensure user input is valid."""

    running = True   # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through height prompt

        # Prompting user for a height for the right circular cylinder
        # Storing user input in height1 variable

        height1 = input("Please enter a height for the right circular cylinder: ")

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(height1):

            # Creating height variable and converting height1 variable from a string into an int

            height = int(height1)

            return height    # Returning user input in height variable

# Start of volume_calc() function definition

def volume_calc():

    # 5. Calculate the volume of a Right Circular Cylinder

    """The volume_calc() function prompts the user for the radius and height
    of a right circular cylinder and then calculates and displays the volume"""

    # Volume Formula: V = (Base Area) x Height
    # For a circular cylinder the base area is (pi)r^2 (where r is radius):
    # Volume of Circular Cylinder = ( (pi)r^2 ) x Height

    # Calling get_radius() function to prompt user for a radius of the cylinder
    # Storing user input in radius variable

    radius = get_radius()

    # Calling get_height() function to prompt user for a height of the cylinder
    # Storing user input in height variable

    height = get_height()

    # Calculating the volume of the right circular cylinder
    # Using math.pi to get the constant pi
    # Using math power(x, y) function to return radius squared (r^2)
    # We solve the function here and input the value in volume

    volume = (math.pi * math.pow(radius, 2)) * height

    # Displaying the volume and formatting it to two decimal points

    print(f'The volume of the right circular cylinder is {volume:.2f}')

# Start of string_validation() function definition

def string_validation(string1):

    """The string_validation() function validates string input
    using isalpha() function to ensure input is only alphabet characters"""

    # Creating string_validation() function with string argument to validate string input

    # Using isalpha() function to ensure input is only alphabet characters

    if not string1.isalpha():

        # If string inputted does not have any alphabet characters

        return False    # Returns False if there's no alphabet characters

    return True     # Returns True if there's only alphabet characters

# Start of int_validation() function definition for integers

def int_validation(int):

    """The int_validation() function validates int input
    using isnumeric() function to ensure input is only numeric characters"""

    # Creating int_validation() function that takes an int as an argument to validate int input

    if not int.isnumeric():     # If int inputted does not have any numeric characters

        return False    # Returns False if there's no numeric characters

    return True     # Returns True if there's only numeric characters

# Start of display_menu() function definition

def display_menu():

    """The display_menu() function displays the menu for the user's options
    and prompts user for their choice while validating their input"""

    # 1. Generate Secure Password
    # 2. Calculate and Format a Percentage
    # 3. How many days from today until July 4, 2025?
    # 4. Use the Law of Cosines to calculate the leg of a triangle.
    # 5. Calculate the volume of a Right Circular Cylinder
    # 6. Exit program

    print("\nThe following menu options below are to provide you"
          " the ability to perform several math and security related functions.\n")

    print("1. Generate Secure Password")    # Option 1

    print("2. Calculate and Format a Percentage")   # Option 2

    print("3. How many days from today until July 4, 2025?")    # Option 3

    print("4. Use the Law of Cosines to calculate the leg of a triangle.")  # Option 4

    print("5. Calculate the volume of a Right Circular Cylinder")   # Option 5

    print("6. Exit program\n")    # Option 6

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through user input validation

        # Prompting the user for their choice and storing answer in choice1 variable
        # Converting user input to an int

        choice1 = input('Enter your choice: ')

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(choice1):

            # Creating choice variable and converting choice1 variable from a string into an int

            choice = int(choice1)

            return choice    # Returning user input in choice variable

# Start of main() function definition

def main():

    """The main() function is the start of the program interacting with the user.
    All other functions are called in this function to display the menu for the user
    to choose an option and perform the corresponding tasks that the user chooses."""

    # This menu-driven application provides users with the ability to perform
    # several math and security related functions.

    print("**********************************************************")  # Header

    print("Welcome to the Python Math and Secret Generation Program!")  # Welcome message

    choice = 0      # Creating the variable choice to control the loop and store user's choice

    # Creating a while loop with the condition that the user's choice is not exit program

    while choice != EXIT_PROGRAM:   # Start of while loop

        # Calling the display_menu() function to display the menu
        # And storing user input value inside choice variable

        choice = display_menu()

        if choice == SEC_PWD:   # If user's choice is option 1

            # Calling sec_password() function

            sec_password()

        if choice == PERCENTAGE_CALC:     # If user choice is option 2

            # Calling the percentage_calc() function

            percentage_calc()

        if choice == DAYS_CALC:   # If user choice is option 3

            # Calling the days_calc() function

            days_calc()

        if choice == LAW_COSINES:     # If user choice is option 4

            # Calling the law_cosines() function

            law_cosines()

        if choice == VOLUME_CALC:     # If user choice is option 5

            # Calling the volume_calc() function

            volume_calc()

        if choice == EXIT_PROGRAM:    # If user choice is option 5

            # Thank you and goodbye message

            print("\nThanks for trying the Math and Secret Generation Program!"
                  " Take care!")

            # Using a break statement to stop the execution of the while loop

            break

# Calling main method

if __name__ == "__main__":

    main()  # Calling main method
