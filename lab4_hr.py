# Husain Rizvi

# SDEV 300 - Lab 4 - Numpy

"""This program is a menu-driven application that allows the
user to create two, 3x3 matrices and then select from menu
options including, addition, subtraction, matrix multiplication,
and element by element multiplication."""

import re  # importing regular expressions library
import sys  # importing sys library
import numpy as np  # importing numpy library as np

# Creating constants for menu options

ADDITION = 1  # First choice (Addition)
SUBTRACTION = 2  # Second choice (Subtraction)
MATRIX_MULTIPLICATION = 3  # Third choice (Matrix Multiplication)
E_BY_E_MULTIPLICATION = 4  # Fourth choice (Element by element multiplication)

# Start of phone_prompt() function definition

def phone_prompt():

    """The phone_prompt function prompts the user for their
    phone number and validates the users input using the regular expressions
    library"""

    # Creating phone_prompt() function to prompt user for their phone number

    running = True  # Creating running boolean variable for while loop condition

    # The while loop is used to continuously ask the prompt if user input is invalid

    while running:  # Start of while loop for input validation

        # Prompting user for their phone number
        # Storing user input in phone_no variable

        phone_no = input("Enter your phone number (XXX-XXX-XXXX): ")

        # Using re.match() function to validate that user input is a valid phone number
        # Using if statement with the match() function as the condition
        # If user input is a valid phone number, while loop breaks
        # Using r prefix when using re.match() function
        # Using \d escape sequence as it matches any decimal digit [0-9]

        if re.match(r"\d{3}-\d{3}-\d{4}", phone_no):

            break     # Using a break statement to stop the execution of the while loop

            # Else if user input is not a valid phone number

        print("Your phone number is not in correct format. Please re-enter: ")  # Error message

# Start of zipcode_prompt() function definition

def zipcode_prompt():

    """The zipcode_prompt function prompts the user for their
    zipcode+4 and validates the users input using the regular expressions
    library"""

    # Creating zipcode_prompt() function to prompt user for their zipcode+4

    running = True  # Creating running boolean variable for while loop condition

    # The while loop is used to continuously ask the prompt if user input is invalid

    while running:  # Start of while loop for input validation

        # Prompting user for their zipcode+4
        # Storing user input in zipcode variable

        zipcode = input("Enter your zipcode +4 (XXXXX-XXXX): ")

        # Using re.match() function to validate that user input is a valid zipcode+4
        # Using if statement with the match() function as the condition
        # If user input is a valid zipcode+4, while loop breaks
        # Using r prefix when using re.match() function
        # Using \d escape sequence as it matches any decimal digit [0-9]

        if re.match(r"\d{5}-\d{4}", zipcode):

            break  # Using a break statement to stop the execution of the while loop

            # Else if user input is not a valid phone number

        print("Your zipcode is not in correct format. Please re-enter: ")  # Error message

# Start of first_matrix() function definition

def first_matrix():

    """The first_matrix() function prompts the user to enter values
    for their first 3x3 matrix and validates the users input."""

    # Creating first_matrix() function to prompt the user
    # to create their first matrix

    print("\nEnter your first 3x3 matrix: ")    # Prompting user for first matrix

    matrix1 = []    # Creating empty list called matrix1

    for i in range(3):  # Using a for loop for value entries (3x3 matrix)

        # Using input() function to get user input and return a string
        # Using split() function to split the user input into a list of strings
        # Using int() to convert the user input to an integer
        # Using map() function to apply int to each element that the user inputs
        # Using list() to turn the iterator into a list

        values = list(map(int, input().split()))

        # Appending the user input of values for the matrix into matrix1 list

        matrix1.append(values)

    print("\nYour first 3x3 matrix is: ")   # Message for displaying first matrix

    for i in range(3):  # Using a for loop to display row entries (3 rows)

        for j in range(3):  # Using a for loop to display column entries (3 columns)

            # Outputting every row and column element and leaving a space between them

            print(matrix1[i][j], end=" ")

        print()     # Calling print()

    return matrix1  # Returning matrix1 for later calculation

# Start of second_matrix() function definition

def second_matrix():

    """The second_matrix() function prompts the user to enter values
    for their second 3x3 matrix and validates the users input."""

    # Creating second_matrix() function to prompt the user
    # to create their second matrix

    print("\nEnter your second 3x3 matrix: ")  # Prompting user for second matrix

    matrix2 = []  # Creating empty list called matrix2

    for i in range(3):  # Using a for loop for value entries (3x3 matrix)

        # Using input() function to get user input and return a string
        # Using split() function to split the user input into a list of strings
        # Using int() to convert the user input to an integer
        # Using map() function to apply int to each element that the user inputs
        # Using list() to turn the iterator into a list

        values = list(map(int, input().split()))

        # Appending the user input of values for the matrix into matrix2 list

        matrix2.append(values)

    print("\nYour second 3x3 matrix is: ")  # Message for displaying second matrix

    for i in range(3):  # Using a for loop to display row entries

        for j in range(3):  # Using a for loop to display column entries

            # Outputting every row and column element and leaving a space between them

            print(matrix2[i][j], end=" ")

        print()  # Calling print()

    return matrix2  # Returning matrix2 for later calculation

# Start of transpose_matrix() function definition

def transpose_matrix(matrix):

    """The transpose_matrix(matrix) function takes a matrix
    as an argument and then finds and displays the transpose
    of the matrix"""

    # Creating the transpose_matrix() function to find the transpose
    # of a matrix and display it

    # Calling transpose() function on the matrix from the argument
    # Storing transposed matrix in transpose1 variable

    transpose1 = matrix.transpose()

    print("\nThe Transpose is: ")   # Display message

    for i in range(3):  # Using a for loop for row entries (3 rows)

        for j in range(3):  # Using a for loop for column entries (3 columns)

            # Displaying each element of the transpose1 matrix
            # and leaving a space between them

            print(transpose1[i][j], end=" ")

        print()     # Calling print() statement

# Start of row_col_avg() function definition

def row_col_avg(matrix):

    """The row_col_avg(matrix) function takes a matrix
    as an argument and then finds and displays the average
    value for each row and column of a given matrix."""

    # Creating the row_col_avg() function to find the average
    # value for each row and column and displays it

    # Calling numpy mean() function on matrix with axis=1 for the row average

    row_avg = matrix.mean(axis=1)

    # Calling numpy mean() function on matrix with axis=0 for the column average

    col_avg = matrix.mean(axis=0)

    print("\nThe row and column mean values of the results are: ")     # Display message

    # Using a for loop and range() function as it is a 3x3 matrix
    # 3 average values for the 3 rows
    # 3 average values for the 3 columns

    for i in range(3):

        # Using float() to convert the user input to a float
        # Using map() function to apply float to each element in row_avg
        # Using list() to turn the iterator into a list

        row_avg = list(map(float, row_avg))
        col_avg = list(map(float, col_avg))

        # Displaying the 3 average values for the 3 rows

        print(f'\nRow {i+1} mean: {row_avg[i]:.2f}')

        # Displaying the 3 average values for the 3 columns

        print(f'Column {i+1} mean: {col_avg[i]:.2f}')

    print()     # Calling the print() statement

# Start of matrix_addition() function definition

def matrix_addition(matrix1, matrix2):

    """The matrix_addition(matrix1, matrix2) function takes
    two matrices as an argument & then adds the two matrices
    & displays the result. It then calls the transpose_matrix()
    & row_col_avg() functions to find & display the transpose
    of the matrix & the average value for each row & column."""

    # Creating matrix_addition() function to add two matrices
    # and display the result. Also to find and display the transpose
    # as well as the average value for each row and column.

    # Calling np.array() function to create an array from the matrix1 matrix
    # Storing values in matrix_one variable

    matrix_one = np.array(matrix1)

    # Calling np.array() function to create an array from the matrix2 matrix
    # Storing values in matrix_two variable

    matrix_two = np.array(matrix2)

    # Calling np.add() function to add the matrix_one and matrix_two matrices
    # Storing resulting matrix in sum1 variable

    sum1 = np.add(matrix_one, matrix_two)

    print("\nYou selected Addition. The results are: ")      # Display message

    for i in range(3):  # Using a for loop for row entries (3 rows)

        for j in range(3):      # Using a for loop for row entries (3 columns)

            # Displaying each element of the resulting sum1 matrix
            # and leaving a space between them

            print(sum1[i][j], end=" ")

        print()     # Calling the print() statement

    # Calling np.array() function to create an array from the resulting sum2 matrix

    sum2 = np.array(sum1)

    # Calling transpose_matrix() function taking the resulting sum2 matrix as the argument
    # Calling transpose_matrix() function to find and display the transpose of the sum2 matrix

    transpose_matrix(sum2)

    # Calling row_col_avg() function taking the resulting sum2 matrix as the argument
    # Calling row_col_avg() function to find and display the average values for each
    # row and column of the sum2 matrix

    row_col_avg(sum2)

# Start of matrix_subtraction() function definition

def matrix_subtraction(matrix1, matrix2):

    """The matrix_subtraction(matrix1, matrix2) function takes
    two matrices as an argument & then subtracts the two matrices
    & displays the result. It then calls the transpose_matrix()
    & row_col_avg() functions to find & display the transpose
    of the matrix & the average value for each row & column."""

    # Creating matrix_subtraction() function to subtract two matrices
    # and display the result. Also to find and display the transpose
    # as well as the average value for each row and column.

    # Calling np.array() function to create an array from the matrix1 matrix
    # Storing values in matrix_one variable

    matrix_one = np.array(matrix1)

    # Calling np.array() function to create an array from the matrix2 matrix
    # Storing values in matrix_two variable

    matrix_two = np.array(matrix2)

    # Calling np.subtract() function to subtract the matrix_one and matrix_two matrices
    # Storing resulting matrix in result1 variable

    result1 = np.subtract(matrix_one, matrix_two)

    print("\nYou selected Subtraction. The results are: ")  # Display message

    for i in range(3):  # Using a for loop for row entries (3 rows)

        for j in range(3):  # Using a for loop for row entries (3 columns)

            # Displaying each element of the resulting result1 matrix

            print(result1[i][j], end=" ")

        print()  # Calling the print() statement

    # Calling np.array() function to create an array from the resulting result2 matrix

    result2 = np.array(result1)

    # Calling transpose_matrix() function taking the resulting result2 matrix as the argument
    # Calling transpose_matrix() function to find and display the transpose of the result2 matrix

    transpose_matrix(result2)

    # Calling row_col_avg() function taking the resulting result2 matrix as the argument
    # Calling row_col_avg() function to find and display the average values for each
    # row and column of the result2 matrix

    row_col_avg(result2)

# Start of matrix_multiplication() function definition

def matrix_multiplication(matrix1, matrix2):

    """The matrix_multiplication(matrix1, matrix2) function takes
    two matrices as an argument and then multiplies the two matrices
    and displays the result. It then calls the transpose_matrix()
    and row_col_avg() functions to find and display the transpose
    of the matrix and the average value for each row and column."""

    # Creating matrix_multiplication() function to multiply two matrices
    # and display the result. Also to find and display the transpose
    # as well as the average value for each row and column.

    # Calling np.matrix() function to create a matrix from the matrix1 matrix
    # Storing values in matrix_one variable

    matrix_one = np.matrix(matrix1)

    # Calling np.matrix() function to create a matrix from the matrix2 matrix
    # Storing values in matrix_two variable

    matrix_two = np.matrix(matrix2)

    # Using np.matmul() function to multiply the matrix_one and matrix_two matrices
    # Storing resulting matrix in result1 variable

    result1 = np.matmul(matrix_one, matrix_two)

    # Calling np.array() function to create an array from the resulting result1 matrix
    # Storing in result1 variable

    result1 = np.array(result1)

    print("\nYou selected Matrix Multiplication. The results are: ")  # Display message

    for i in range(3):  # Using a for loop for row entries (3 rows)

        for j in range(3):  # Using a for loop for row entries (3 columns)

            # Displaying each element of the resulting result1 matrix
            # and leaving a space between them

            print(result1[i][j], end=" ")

        print()  # Calling the print() statement

    # Calling np.array() function to create an array from the resulting result2 matrix

    result2 = np.array(result1)

    # Calling transpose_matrix() function taking the resulting result2 matrix as the argument
    # Calling transpose_matrix() function to find and display the transpose of the result2 matrix

    transpose_matrix(result2)

    # Calling row_col_avg() function taking the resulting result2 matrix as the argument
    # Calling row_col_avg() function to find and display the average values for each
    # row and column of the result2 matrix

    row_col_avg(result2)

# Start of e_by_e_multiplication() function definition

def e_by_e_multiplication(matrix1, matrix2):

    """The e_by_e_multiplication(matrix1, matrix2) function takes
    two matrices as an argument & then multiplies the two matrices
    element by element & displays the result. It then calls the
    transpose_matrix() & row_col_avg() functions to find & display the
    transpose of the matrix & the average value for each row & column."""

    # Creating e_by_e_multiplication() function to multiply two matrices
    # element by element and display the result. Also to find and display
    # the transpose as well as the average value for each row and column.

    # Calling np.matrix() function to create a matrix from the matrix1 matrix
    # Storing values in matrix_one variable

    matrix_one = np.matrix(matrix1)

    # Calling np.matrix() function to create a matrix from the matrix2 matrix
    # Storing values in matrix_two variable

    matrix_two = np.matrix(matrix2)

    # Calling the np.multiply() function to multiply the two matrices element by element
    # Storing resulting matrix in result1 variable

    result1 = np.multiply(matrix_one, matrix_two)

    # Calling np.array() function to create an array from the resulting result1 matrix
    # Storing in result1 variable

    result1 = np.array(result1)

    print("\nYou selected Element by Element Multiplication. The results are: ")  # Display message

    for i in range(3):  # Using a for loop for row entries (3 rows)

        for j in range(3):  # Using a for loop for row entries (3 columns)

            # Displaying each element of the resulting result1 matrix

            print(result1[i][j], end=" ")

        print()  # Calling the print() statement

    # Calling np.array() function to create an array from the resulting result2 matrix

    result2 = np.array(result1)

    # Calling transpose_matrix() function taking the resulting result2 matrix as the argument
    # Calling transpose_matrix() function to find and display the transpose of the result2 matrix

    transpose_matrix(result2)

    # Calling row_col_avg() function taking the resulting result2 matrix as the argument
    # Calling row_col_avg() function to find and display the average values for each
    # row and column of the result2 matrix

    row_col_avg(result2)

# Start of int_validation() function definition for integers

def int_validation(int):

    """The int_validation() function validates int input
    using isnumeric() function to ensure input is only numeric characters"""

    # Creating int_validation() function that takes an int as an argument to validate int input

    if not int.isnumeric():  # If int inputted does not have any numeric characters

        return False  # Returns False if there's no numeric characters

    return True  # Returns True if there's only numeric characters

# Start of play_prompt() function definition

def play_prompt():

    """The play_prompt() function asks the user if they want to play the
    Matrix Game, if yes, continues with the game, if no, terminates the program."""

    # Creating play_prompt() function to ask user if they want to play

    running = True  # Creating running boolean variable for while loop condition

    # The while loop is used to continuously ask the prompt if user input is invalid

    while running:  # Start of while loop for input validation

        # Asking user if they want to play
        # Storing user input in answer variable

        answer = input("Do you want to play the Matrix Game?"
                       "\nEnter Y for Yes or N for No:")

        # Using upper() function to convert user input to upper case

        answer = answer.upper()

        if answer == "Y":  # If user enters y or Y, return True, continue with program
            return True

        # If answer is not "Y" or "N", user will be continuously prompted until a Y or N

        if answer == "N":  # If user enters n or N, return False, terminate program
            return False

# Start of display_menu() function definition

def display_menu():

    """The display_menu() function displays the menu for the user's options
    and prompts user for their choice while validating their input"""

    # 1. Addition
    # 2. Subtraction
    # 3. Matrix Multiplication
    # 4. Element by element multiplication

    print("\nSelect a Matrix Operation from the list below:\n")     # Intro message

    print("1. Addition")  # Option 1

    print("2. Subtraction")  # Option 2

    print("3. Matrix Multiplication")  # Option 3

    print("4. Element by element multiplication ")  # Option 4

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through user input validation

        # Prompting the user for their choice and storing answer in choice1 variable

        choice1 = input('Enter your choice: ')

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(choice1):

            # Creating choice variable and converting choice1 variable from a string into an int

            choice = int(choice1)

            return choice  # Returning user input in choice variable

# Start of main() function definition

def main():

    """The main() function is the start of the program interacting with the user.
    All other functions are called in this function to display the menu for the user
    to choose an option and perform the corresponding tasks that the user chooses."""

    # This menu-driven application provides users with the ability to perform
    # matrix math operations such as matrix addition, subtraction, multiplication
    # and element by element multiplication.

    print("******Welcome to the Python Matrix Application******")  # Welcome message

    if not play_prompt():

        # If play_prompt() function is False (User says no), displays exit message

        print("******Thanks for playing Python Numpy******")  # Displaying exit message

        sys.exit()  # Using exit() method to end the program

    phone_prompt()      # Calling phone_prompt() function to prompt user for their phone number

    zipcode_prompt()    # Calling zipcode_prompt() function to prompt user for their zipcode

    # Calling first_matrix() function to prompt user for their first 3x3 matrix
    # Storing resulting matrix and values in matrix1 variable

    matrix1 = first_matrix()

    # Calling second_matrix() function to prompt user for their second 3x3 matrix
    # Storing resulting matrix and values in matrix2 variable

    matrix2 = second_matrix()

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:     # Start of while loop

        # Calling the display_menu() function to display the menu
        # And storing user input value inside choice variable

        choice = display_menu()

        if choice == ADDITION:  # If user's choice is option 1

            # Calling matrix_addition() function with matrix1 and matrix2 as the arguments

            matrix_addition(matrix1, matrix2)

        if choice == SUBTRACTION:  # If user choice is option 2

            # Calling matrix_subtraction() function with matrix1 and matrix2 as the arguments

            matrix_subtraction(matrix1, matrix2)

        if choice == MATRIX_MULTIPLICATION:  # If user choice is option 3

            # Calling matrix_multiplication() function with matrix1 and matrix2 as the arguments

            matrix_multiplication(matrix1, matrix2)

        if choice == E_BY_E_MULTIPLICATION:  # If user choice is option 4

            # Calling e_by_e_multiplication() function with matrix1 and matrix2 as the arguments

            e_by_e_multiplication(matrix1, matrix2)

        if not play_prompt():

            # If play_prompt() function is False (User says no), displays exit message

            print("******Thanks for playing Python Numpy******")  # Displaying exit message

            break  # Using a break statement to stop the execution of the while loop


# Calling main method

if __name__ == "__main__":

    main()  # Calling main method
