# Husain Rizvi

# SDEV 300 - Lab 1 - Voter Registration Application

"""This program determines whether you are eligible to vote"""

# Start of first_name() function definition

def first_name():

    """The first_name() function prompts user for their first name
    and validates the user input"""

    # Creating first_name() function to prompt user for their first name

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through first name prompt

        # Prompting user for their first name and storing in fname variable

        fname = input("What is your first name?")

        # Calling string_validation() function to ensure user input is validated

        if string_validation(fname):

            # Calling string_validation() function in if statement for input validation

            return fname  # Returning user input in fname variable

        print("Error - please enter alphabet characters only.")

# Start of last_name() function definition

def last_name():

    """The last_name() function prompts user for their last name
    and validates user input"""

    # Creating last_name() function to prompt user for their last name

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through last name prompt

        # Prompting user for their last name and storing in lname variable

        lname = input("What is your last name?")

        # Calling string_validation() function in if statement for input validation

        if string_validation(lname):

            return lname  # Returning user input

        print("Error - please enter alphabet characters only.")

# Start of age_prompt() function definition

def age_prompt():

    """The age_prompt() function prompts user for their age
    and validates user input"""

    # Creating age_prompt() function to prompt user for their age

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through age prompt

        # Asking user for their age and storing in age1 variable

        age1 = input("What is your age?")

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(age1):

            # Creating age variable and converting age1 variable from a string into an int

            age = int(age1)

            # If age is less than 120 and greater than or equal to 18 user will continue

            if 120 > age >= 18:

                return age  # Returning user input in age variable

            # If age is less than 18 or greater than 120, then user is not eligible

            # Else, they are not eligible for registration

            print("You are not eligible for registration.")  # Message

            return "Quit"

        print("Error - please enter numeric characters only.")

# Start of citizenship_prompt() function definition

def citizenship_prompt():

    """The citizenship_prompt() function prompts user for their U.S. citizenship
    and validates user input"""

    # Creating citizenship_prompt() function to ask if user is a U.S. citizen

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through citizenship prompt

        # Asking user if they are a U.S. citizen and storing input in citizenship variable

        citizenship = input("Are you a U.S. Citizen? (Enter 'yes' or 'no')")

        # Calling string_validation() function to ensure input is only alphabet characters

        if string_validation(citizenship):

            # Calling string_validation() function in if statement for input validation

            citizenship = citizenship.upper()

            # Using upper() function to convert input to upper case

            # If they are U.S. citizens, they will continue with registration

            if citizenship == "YES":

                # Confirmation message

                return "U.S. citizen"

                # If they are not U.S. citizens, they are ineligible for registration

            if citizenship == "NO":

                # If statement allows prompt to continuously repeat if user input is invalid

                # Displaying exit message

                print("Not a U.S. citizen. Can't register for voting without a U.S. citizenship.")

                return "Quit"

        print("Error - please enter alphabet characters only.")

# Start of state_prompt() function definition

def state_prompt():

    """The state_prompt() function prompts user for the state they live in
    and validates user input"""

    # Creating state_prompt() function to ask what state user lives in

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through state prompt

        # Prompting user for their state and storing input in state variable

        state = input("What state do you live? (Use two letter abbreviation)")

        # Calling string_validation() function in if statement for input validation
        # Calling len() function for input string length validation

        if string_validation(state) and len(state) == 2:

            return state    # Returning user input and storing input in state variable

        print("Error - please enter alphabet characters only.")

# Start of zipcode_prompt() function definition

def zipcode_prompt():

    """The zipcode_prompt() function prompts user for their zipcode
    and validates user input"""

    # Creating zipcode_prompt() function to ask user for their zipcode

    running = True  # Creating running boolean variable for while loop condition

    while running:  # Start of while loop to loop through zipcode prompt

        # While loop allows user to be continuously prompted if user input is invalid

        # Calling exit_prompt() function to prompt user for registration continuation

        # Prompting user for their zipcode and storing value in zipcode variable

        zipcode = input("What is your zipcode?")

        # Using len() function to check if user input is 5 numbers long

        if len(zipcode) == 5:   # Input length validation (Zipcodes can only be 5 numbers long)

            # Returning user input and converting zipcode variable into an integer

            return int(zipcode)

# Start of exit_prompt() function definition

def exit_prompt():

    """The exit_prompt() function gives the user the option to
    continue with registration or terminate the registration application"""

    # Creating exit_prompt() function to prompt user for registration continuation

    running = True  # Creating running boolean variable for while loop condition

    # The while loop is used to continuously ask the prompt if user input is invalid

    while running:  # Start of while loop for input validation

        # Asking user if they want to continue with the registration application
        # Storing user input in answer variable

        answer = input("Do you want to continue with the voter registration? (Enter 'yes' or 'no')")

        # Using upper() function to convert user input to upper case

        answer = answer.upper()

        if answer == "YES":     # If user enters yes, continue with registration
            return True

        # If answer is not "YES" or "NO", user will be continuously prompted until a YES or NO

        if answer == "NO":    # If user enters no, end registration application
            return False

# Start of string_validation() function definition

def string_validation(string):

    """The string_validation() function validates string input
    using isalpha() function to ensure input is only alphabet characters"""

    # Creating string_validation() function with string argument to validate string input

    # Using isalpha() function to ensure input is only alphabet characters

    if not string.isalpha():

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

# Start of main function definition

def main():

    """The main() function is the start of the voter registration application.
    All other functions are called in this function to prompt the user
    for registration questions and evaluate user's registration status."""

    print("******************************************************")     # Header

    print("Welcome to the Python Voter Registration Application.")  # Welcome message

    # Creating an empty list called applications for inputting voter registration applications
    # Allows us to ensure all registration questions are completed

    application = []

    running = True  # While loop conditional boolean variable running

    while running:  # Start of while loop for voter registration application

        # Calling exit_prompt() function to prompt user for continuation

        if not exit_prompt():

            # If exit_prompt() function is False (User says no), displays exit message

            print("Exiting the voter registration program...")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop

        # If exit_prompt() function is True (User wants to continue), prompt user for first name

        fname = first_name()

        # Calling first_name() function to prompt user for their first name
        # Storing first_name() value in fname variable

        # Adding the first name to the end of the list using the append() function

        application.append(fname)

        # Calling exit_prompt() function to prompt user for continuation

        if not exit_prompt():

            # If exit_prompt() function is False (User says no), displays exit message

            print("Exiting the voter registration program...")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop

        # Else If exit_prompt() function is True (User wants to continue), prompt user for last name

        lname = last_name()

        # Calling last_name() function to prompt user for their last name
        # Storing last_name() value in lname variable

        # Adding the last name to the end of the list using the append() function

        application.append(lname)

        # Calling exit_prompt() function to prompt user for continuation

        if not exit_prompt():

            # If exit_prompt() function is False (User says no), displays exit message

            print("Exiting the voter registration program...")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop

        # Else If exit_prompt() function is True (User wants to continue), prompt user for age

        age = age_prompt()  # Calling age_prompt() function to prompt user for their age

        if age == "Quit":

            break

        # Adding the age to the end of the list using the append() function

        application.append(age)

        # Calling exit_prompt() function to prompt user for continuation

        if not exit_prompt():

            # If exit_prompt() function is False (User says no), displays exit message

            print("Exiting the voter registration program...")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop

        # If exit_prompt() function is True (User wants to continue), prompt user for citizenship

        # Calling citizenship_prompt() function to prompt user for their citizenship
        # Storing value in citizenship variable

        citizenship = citizenship_prompt()

        if citizenship == "Quit":

            break

        # Adding the citizenship to the end of the list using the append() function

        application.append(citizenship)

        # Calling exit_prompt() function to prompt user for continuation

        if not exit_prompt():
            # If exit_prompt() function is False (User says no), displays exit message

            print("Exiting the voter registration program...")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop

        # If exit_prompt() function is True (User wants to continue), prompt user for their state

        # Calling state_prompt() function to prompt user for their state they live in
        # Storing value in state variable

        state = state_prompt()

        # Adding the state to the end of the list using the append() function

        application.append(state)

        # Calling exit_prompt() function to prompt user for continuation

        if not exit_prompt():
            # If exit_prompt() function is False (User says no), displays exit message

            print("Exiting the voter registration program...")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop

        # If exit_prompt() function is True (User wants to continue), prompt user for their zipcode

        # Calling zipcode_prompt() function to prompt user for their zipcode
        # Storing value in zipcode variable

        zipcode = zipcode_prompt()

        # Adding the zipcode to the end of the list using the append() function

        application.append(zipcode)

        # Using the len() to ensure application has all 6 values submitted for registration

        if len(application) == 6:

            # Thank you message

            print("Thanks for registering to vote. Here is the information we received:")

            # Using formatting to display user's first and last name

            print(f'Name (first and last): {fname} {lname}')

            print(f'Age: {age}')    # Using formatting to display user's entered age

            # Using formatting to display users U.S. citizenship

            print(f'U.S. Citizen: {citizenship}')

            # Using formatting to display the state the user lives in

            print(f'State: {state.upper()}')

            # Using upper() function to make state abbreviation properly capitalized

            print(f'Zipcode: {zipcode}')    # Using formatting to display user's entered zipcode

            # Thank you message

            print("Thanks for trying the Voter Registration Application. "
                  "Your voter registration card should be shipped within 3 weeks.")

            # Closing header

            print("******************************************************"
                  "**************************************************************")

            break   # Using a break statement to stop the execution of a looping statement

        # If application does not contain 6 values then the user is ineligible to vote

        break   # Using a break statement to stop the execution of a looping statement


# Calling main method

if __name__ == "__main__":

    main()  # Calling main method
