# Husain Rizvi

# SDEV 300 - Lab 5 - File Data Analysis

"""This program is a menu-driven application that allows a user to load
one of two CSV files (PopChange.csv & Housing.csv) and then performs histogram
analysis and plots for select variables on the datasets. It also gives specific
statistics of certain columns the user chooses."""

import pandas as pd     # importing pandas library as pd
import matplotlib.pyplot as plt     # importing matplotlib.pyplot library as plt

POPULATION_DATA = 1     # First choice (Population Data)
HOUSING_DATA = 2    # Second choice (Housing Data)
EXIT_PROGRAM = 3    # Third choice (Exit Program)

# Start of pop_data_menu() function definition

def pop_data_menu():

    """The pop_data_menu() function gives the user a menu
    for specific columns they would like to analyze from the
    PopChange.csv file. It then prompts the user for input and
    validates the users input and then returns the users choice."""

    # 1. Pop Apr 1
    # 2. Pop Jul 1
    # 3. Change Pop
    # 4. Exit Column

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through user input validation

        print("Select the Column you want to analyze: ")      # Prompt

        print("1. Pop Apr 1")   # Column 1

        print("2. Pop Jul 1")   # Column 2

        print("3. Change Pop")  # Column 3

        print("4. Exit Column")     # Exit Column Option

        # Prompting the user for their choice and storing answer in choice1 variable

        choice1 = input('Enter your choice: ')

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(choice1):

            # Creating choice variable and converting choice1 variable from a string into an int

            choice = int(choice1)

            return choice  # Returning user input in choice variable

# Start of pop_apr_1() function definition

def pop_apr_1():

    """The pop_apr_1() function is where the program calculates and displays
    all the specific statistics for the Pop Apr 1 column from the
    PopChange.csv file."""

    # Creating pop_apr_1() function to calculate and display all
    # the required statistics for the Pop Apr 1 column from the
    # PopChange.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (PopChange.csv) into DataFrame
    # Storing inside pop_change value

    pop_change = pd.read_csv("PopChange.csv")

    print("\nYou selected Pop Apr 1\n")     # Display message

    # Selecting the Pop Apr 1 column from the PopChange.csv file
    # Storing column in pop_apr variable

    pop_apr = pop_change["Pop Apr 1"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the Pop Apr 1 column and displaying it

    print(f'Count = {pop_apr.count()}')

    # Using the mean() function to return the average of the data in the
    # Pop Apr 1 column and storing the calculated average in the mean variable

    mean = pop_apr.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the Pop Apr 1 column and storing calculated value in the stdev variable

    stdev = pop_apr.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')      # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the Pop Apr 1 column and displaying it

    print(f'Min = {pop_apr.min()}')

    # Using the max() function to return the maximum value of
    # the Pop Apr 1 column and displaying it

    print(f'Max = {pop_apr.max()}')

    print("\nThe Histogram of this column is now displayed.")       # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the Pop Apr 1 column

    plt.hist(pop_apr, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("Pop Apr 1")

    plt.show()      # Using the plt.show() function to display histogram

# Start of pop_jul_1() function definition

def pop_jul_1():

    """The pop_jul_1() function is where the program calculates and displays
    all the specific statistics for the Pop Jul 1 column from the
    PopChange.csv file."""

    # Creating pop_jul_1() function to calculate and display all
    # the required statistics for the Pop Jul 1 column from the
    # PopChange.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (PopChange.csv) into DataFrame
    # Storing inside pop_change value

    pop_change = pd.read_csv("PopChange.csv")

    print("\nYou selected Pop Jul 1\n")     # Display message

    # Selecting the Pop Jul 1 column from the PopChange.csv file
    # Storing column in pop_jul variable

    pop_jul = pop_change["Pop Jul 1"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the Pop Jul 1 column and displaying it

    print(f'Count = {pop_jul.count()}')

    # Using the mean() function to return the average of the data in the
    # Pop Jul 1 column and storing the calculated average in the mean variable

    mean = pop_jul.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the Pop Jul 1 column and storing calculated value in the stdev variable

    stdev = pop_jul.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')      # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the Pop Jul 1 column and displaying it

    print(f'Min = {pop_jul.min()}')

    # Using the max() function to return the maximum value of
    # the Pop Jul 1 column and displaying it

    print(f'Max = {pop_jul.max()}')

    print("\nThe Histogram of this column is now displayed.")       # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the Pop Jul 1 column

    plt.hist(pop_jul, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("Pop Jul 1")

    plt.show()      # Using the plt.show() function to display histogram

# Start of change_pop_1() function definition

def change_pop_1():

    """The change_pop_1() function is where the program calculates and displays
    all the specific statistics for the Change Pop column from the
    PopChange.csv file."""

    # Creating change_pop_1() function to calculate and display all
    # the required statistics for the Change Pop column from the
    # PopChange.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (PopChange.csv) into DataFrame
    # Storing inside pop_change value

    pop_change = pd.read_csv("PopChange.csv")

    print("\nYou selected Change Pop\n")    # Display message

    # Selecting the Change Pop column from the PopChange.csv file
    # Storing column in change_pop variable

    change_pop = pop_change["Change Pop"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the Change Pop column and displaying it

    print(f'Count = {change_pop.count()}')

    # Using the mean() function to return the average of the data in the
    # Change Pop column and storing the calculated average in the mean variable

    mean = change_pop.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the Change Pop column and storing calculated value in the stdev variable

    stdev = change_pop.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')      # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the Change Pop column and displaying it

    print(f'Min = {change_pop.min()}')

    # Using the max() function to return the maximum value of
    # the Change Pop column and displaying it

    print(f'Max = {change_pop.max()}')

    print("\nThe Histogram of this column is now displayed.")       # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the Change Pop column

    plt.hist(change_pop, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("Change Pop")

    plt.show()      # Using the plt.show() function to display histogram

# Start of pop_data() function definition

def pop_data():

    """The pop_data() function is called when the user chooses
    the Population Data option from the initial menu. This function
    calls the pop_data_menu() function and gets the users choice.
    This program also calls the appropriate functions for the column(s)
    the user chooses."""

    # Creating pop_data() function to control the Population Data file
    # histogram analysis and statistics

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:     # Start of while loop

        # Calling the pop_data_menu() function to display the Population Data column
        # menu and storing user input value inside choice variable

        choice = pop_data_menu()

        if choice == 1:     # If user's choice is option 1

            pop_apr_1()     # Calling pop_apr_1() function

        if choice == 2:     # If user's choice is option 2

            pop_jul_1()     # Calling pop_jul_1() function

        if choice == 3:     # If user's choice is option 3

            change_pop_1()      # Calling change_pop_1() function

        if choice == 4:     # If user's choice is option 4

            print("\nYou selected to exit the column menu\n")   # Exit message

            break   # Using a break statement to stop the execution of the while loop

# Start of house_data_menu() function definition

def house_data_menu():

    """The house_data_menu() function gives the user a menu
    for specific columns they would like to analyze from the
    Housing.csv file. It then prompts the user for input and
    validates the users input and then returns the users choice."""

    # 1. AGE
    # 2. BEDRMS
    # 3. BUILT
    # 4. ROOMS
    # 5. UTILITY
    # 6. Exit Column

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through user input validation

        print("\nSelect the Column you want to analyze: ")      # Prompt

        print("1. AGE")     # Column 1

        print("2. BEDRMS")      # Column 2

        print("3. BUILT")       # Column 3

        print("4. ROOMS")       # Column 4

        print("5. UTILITY")     # Column 5

        print("6. Exit Column")     # Exit Column

        # Prompting the user for their choice and storing answer in choice1 variable

        choice1 = input('Enter your choice: ')

        # Calling int_validation() function to ensure user input is only numeric characters

        if int_validation(choice1):

            # Creating choice variable and converting choice1 variable from a string into an int

            choice = int(choice1)

            return choice  # Returning user input in choice variable

# Start of age_stats() function definition

def age_stats():

    """The age_stats() function is where the program calculates and displays
    all the specific statistics for the AGE column from the
    Housing.csv file."""

    # Creating age_stats() function to calculate and display all
    # the required statistics for the AGE column from the
    # Housing.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (Housing.csv) into DataFrame
    # Storing inside housing value

    housing = pd.read_csv("Housing.csv")

    print("\nYou selected AGE\n")   # Display message

    # Selecting the AGE column from the Housing.csv file
    # Storing column in age variable

    age = housing["AGE"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the AGE column and displaying it

    print(f'Count = {age.count()}')

    # Using the mean() function to return the average of the data in the
    # AGE column and storing the calculated average in the mean variable

    mean = age.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the AGE column and storing calculated value in the stdev variable

    stdev = age.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')      # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the AGE column and displaying it

    print(f'Min = {age.min()}')

    # Using the max() function to return the maximum value of
    # the AGE column and displaying it

    print(f'Max = {age.max()}')

    print("\nThe Histogram of this column is now displayed.")   # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the AGE column

    plt.hist(age, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("AGE")

    plt.show()      # Using the plt.show() function to display histogram

# Start of bedrms_stats() function definition

def bedrms_stats():

    """The bedrms_stats() function is where the program calculates and displays
    all the specific statistics for the BEDRMS column from the
    Housing.csv file."""

    # Creating bedrms_stats() function to calculate and display all
    # the required statistics for the BEDRMS column from the
    # Housing.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (Housing.csv) into DataFrame
    # Storing inside bedrms value

    bedrms = pd.read_csv("Housing.csv")

    print("\nYou selected BEDRMS\n")    # Display message

    # Selecting the BEDRMS column from the Housing.csv file
    # Storing column in bedrooms variable

    bedrooms = bedrms["BEDRMS"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the BEDRMS column and displaying it

    print(f'Count = {bedrooms.count()}')

    # Using the mean() function to return the average of the data in the
    # BEDRMS column and storing the calculated average in the mean variable

    mean = bedrooms.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the BEDRMS column and storing calculated value in the stdev variable

    stdev = bedrooms.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')      # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the BEDRMS column and displaying it

    print(f'Min = {bedrooms.min()}')

    # Using the max() function to return the maximum value of
    # the BEDRMS column and displaying it

    print(f'Max = {bedrooms.max()}')

    print("\nThe Histogram of this column is now displayed.")   # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the BEDRMS column

    plt.hist(bedrooms, bins=100)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("BEDRMS")

    plt.show()      # Using the plt.show() function to display histogram

# Start of built_stats() function definition

def built_stats():

    """The built_stats() function is where the program calculates and displays
    all the specific statistics for the BUILT column from the
    Housing.csv file."""

    # Creating built_stats() function to calculate and display all
    # the required statistics for the BUILT column from the
    # Housing.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (Housing.csv) into DataFrame
    # Storing inside built value

    built = pd.read_csv("Housing.csv")

    print("\nYou selected BUILT\n")     # Display message

    # Selecting the BUILT column from the Housing.csv file
    # Storing column in built variable

    built = built["BUILT"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the BUILT column and displaying it

    print(f'Count = {built.count()}')

    # Using the mean() function to return the average of the data in the
    # BUILT column and storing the calculated average in the mean variable

    mean = built.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the BUILT column and storing calculated value in the stdev variable

    stdev = built.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')      # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the BUILT column and displaying it

    print(f'Min = {built.min()}')

    # Using the max() function to return the maximum value of
    # the BUILT column and displaying it

    print(f'Max = {built.max()}')

    print("\nThe Histogram of this column is now displayed.")   # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the BUILT column

    plt.hist(built, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("BUILT")

    plt.show()      # Using the plt.show() function to display histogram

# Start of rooms_stats() function definition

def rooms_stats():

    """The rooms_stats() function is where the program calculates and displays
    all the specific statistics for the ROOMS column from the
    Housing.csv file."""

    # Creating rooms_stats() function to calculate and display all
    # the required statistics for the ROOMS column from the
    # Housing.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (Housing.csv) into DataFrame
    # Storing inside rooms value

    rooms = pd.read_csv("Housing.csv")

    print("\nYou selected ROOMS\n")     # Display message

    # Selecting the ROOMS column from the Housing.csv file
    # Storing column in rooms variable

    rooms = rooms["ROOMS"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the ROOMS column and displaying it

    print(f'Count = {rooms.count()}')

    # Using the mean() function to return the average of the data in the
    # ROOMS column and storing the calculated average in the mean variable

    mean = rooms.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the ROOMS column and storing calculated value in the stdev variable

    stdev = rooms.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')  # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the ROOMS column and displaying it

    print(f'Min = {rooms.min()}')

    # Using the max() function to return the maximum value of
    # the ROOMS column and displaying it

    print(f'Max = {rooms.max()}')

    print("\nThe Histogram of this column is now displayed.")   # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the ROOMS column

    plt.hist(rooms, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("ROOMS")

    plt.show()     # Using the plt.show() function to display histogram

# Start of utility_stats() function definition

def utility_stats():

    """The utility_stats() function is where the program calculates and displays
    all the specific statistics for the UTILITY column from the
    Housing.csv file."""

    # Creating rooms_stats() function to calculate and display all
    # the required statistics for the UTILITY column from the
    # Housing.csv file

    # Using the pandas function read_csv() to read a
    # comma-separated values (CSV) file (Housing.csv) into DataFrame
    # Storing inside utility value

    utility = pd.read_csv("Housing.csv")

    print("\nYou selected UTILITY\n")   # Display message

    # Selecting the UTILITY column from the Housing.csv file
    # Storing column in utility variable

    utility = utility["UTILITY"]

    print("The statistics for this column are: \n")     # Display message

    # Using the count() function to count the number of not empty values
    # for each row in the UTILITY column and displaying it

    print(f'Count = {utility.count()}')

    # Using the mean() function to return the average of the data in the
    # UTILITY column and storing the calculated average in the mean variable

    mean = utility.mean()

    # Using the round() function to round the calculated average and format
    # it to the second decimal place (i.e. 53.33)

    mean = round(mean, 2)

    print(f'Mean = {mean}')     # Displaying calculated and formatted mean

    # Using the std() function to calculate the standard deviation of the data
    # in the UTILITY column and storing calculated value in the stdev variable

    stdev = utility.std()

    # Using the round() function to round the standard deviation and format
    # it to the second decimal place (i.e. 53.33)

    stdev = round(stdev, 2)

    print(f'Standard Deviation = {stdev}')  # Displaying calculated and formatted stdev

    # Using the min() function to return the minimum value of
    # the UTILITY column and displaying it

    print(f'Min = {utility.min()}')

    # Using the max() function to return the maximum value of
    # the UTILITY column and displaying it

    print(f'Max = {utility.max()}')

    print("\nThe Histogram of this column is now displayed.")   # Display message

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplots(figsize=(15, 5))

    # Using the plt.hist() function to make a histogram with the UTILITY column

    plt.hist(utility, bins=50)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("UTILITY")

    plt.show()     # Using the plt.show() function to display histogram

# Start of house_data() function definition

def house_data():

    """The house_data() function is called when the user chooses
    the Housing Data option from the initial menu. This function
    calls the house_data_menu() function and gets the users choice.
    This program also calls the appropriate functions for the column(s)
    the user chooses."""

    # Creating house_data() function to control the Housing Data file
    # histogram analysis and statistics

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through user input validation

        # Calling the house_data_menu() function to display the Housing Data column
        # menu and storing user input value inside choice variable

        choice = house_data_menu()

        if choice == 1:     # If user's choice is option 1

            age_stats()     # Calling age_stats() function

        if choice == 2:     # If user's choice is option 2

            bedrms_stats()      # Calling bedrms_stats() function

        if choice == 3:     # If user's choice is option 3

            built_stats()   # Calling built_stats() function

        if choice == 4:     # If user's choice is option 4

            rooms_stats()   # Calling rooms_stats() function

        if choice == 5:     # If user's choice is option 5

            utility_stats()     # Calling utility_stats() function

        if choice == 6:     # If user's choice is option 6

            print("\nYou selected to exit the column menu\n")     # Exit message

            break   # Using a break statement to stop the execution of the while loop

# Start of int_validation() function definition for integers

def int_validation(int):

    """The int_validation() function validates int input
    using isnumeric() function to ensure input is only numeric characters"""

    # Creating int_validation() function that takes an int as an argument to validate int input

    if not int.isnumeric():  # If int inputted does not have any numeric characters

        return False  # Returns False if there's no numeric characters

    return True  # Returns True if there's only numeric characters

# Start of display_menu() function definition

def display_menu():

    """The display_menu() function displays the menu for the user's options
    and prompts user for their choice while validating their input"""

    # 1. Population Data
    # 2. Housing Data
    # 3. Exit Program

    print("\nSelect the file you want to analyze:\n")     # Prompt

    print("1. Population Data")  # Option 1

    print("2. Housing Data")  # Option 2

    print("3. Exit the program")  # Option 3

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

    # This program allows a user to load one of two CSV files(PopChange.csv & Housing.csv)
    # and then performs histogram analysis and plots for select variables on the datasets.
    # It also gives specific statistics of certain columns the user chooses.

    print("******Welcome to the Python Data Analysis App******")  # Welcome message

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:     # Start of while loop

        # Calling the display_menu() function to display the menu
        # And storing user input value inside choice variable

        choice = display_menu()

        if choice == POPULATION_DATA:  # If user's choice is POPULATION_DATA

            print("You have entered Population Data.\n")    # Display message

            pop_data()      # Calling pop_data() function

        if choice == HOUSING_DATA:  # If user choice is HOUSING_DATA

            print("You have entered Housing Data.\n")   # Display message

            house_data()    # Calling house_data() function

        if choice == EXIT_PROGRAM:  # If user choice is EXIT_PROGRAM

            # Displaying exit message

            print("\n******Thanks for playing the Python Data Analysis App******")

            break  # Using a break statement to stop the execution of the while loop


# Calling main method

if __name__ == "__main__":

    main()  # Calling main method
