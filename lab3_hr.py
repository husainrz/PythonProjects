# Husain Rizvi

# SDEV 300 - Lab 3 - Lists and Sets

"""This program is a menu-driven application that allows a user to display,
sort and update, as needed a List of U.S. states containing the state capital,
overall state population, and state flower."""

import matplotlib.pyplot as plt     # importing matplotlib.pyplot library as plt

# Creating constants for menu options

DISPLAY_STATES = 1
# Option 1 (Display all U.S. States in Alphabetical order along with the Capital,
# State Population, and Flower)
SEARCH_STATES = 2
# Option 2  (Search for a specific state and display the appropriate Capital name,
# State Population, and an image of the associated State Flower.)
DISPLAY_BAR_GRAPH = 3
# Option 3  (Provide a Bar graph of the top 5 populated States showing their overall population.)
UPDATE_POPULATION = 4
# Option 4  (Update the overall state population for a specific state.)
EXIT_PROGRAM = 5    # Option 5 (Exit the program)

# Start of get_states() function definition

def get_states():

    """The get_states() functions creates a list called states
    and adds all 50 states along with the Capital, State Population,
    Flower, and the file path for the image of the Flower. It then
    sorts the list into alphabetical order and returns the list."""

    # Creating list called states and adding all 50 states
    # along with the Capital, State Population, Flower,
    # and the file path for the image of the Flower."""

    states = [['AL', 'Montgomery', 4918689, 'Camellia',
               '/Users/macbook/PycharmProjects/Flowers/camellia.jpg'],
              # Adding Alabama and its values
              ['AK', 'Juneau', 727951, 'Forget Me Not',
               '/Users/macbook/PycharmProjects/Flowers/ForgetMeNot.jpg'],
              # Adding Alaska and its values
              ['AZ', 'Phoenix', 7399410, 'Saguaro Cactus Blossom',
               '/Users/macbook/PycharmProjects/Flowers/SaguaroCactus.jpg'],
              # Adding Arizona and its values
              ['AR', 'Little Rock', 3025875, 'Apple Blossom',
               '/Users/macbook/PycharmProjects/Flowers/AppleBlossom.jpg'],
              # Adding Arkansas and its values
              ['CA', 'Sacramento', 39562858, 'California Poppy',
               '/Users/macbook/PycharmProjects/Flowers/CaliforniaPoppy.jpg'],
              # Adding California and its values
              ['CO', 'Denver', 5826185, 'Rocky Mountain Columbine',
               '/Users/macbook/PycharmProjects/Flowers/Columbine.jpg'],
              # Adding Colorado and its values
              ['CT', 'Hartford', 3559054, 'Mountain Laurel',
               '/Users/macbook/PycharmProjects/Flowers/MountainLaurel.jpg'],
              # Adding Connecticut and its values
              ['DE', 'Dover', 982049, 'Peach Blossom',
               '/Users/macbook/PycharmProjects/Flowers/PeachBlossom.jpg'],
              # Adding Delaware and its values
              ['FL', 'Tallahassee', 21711157, 'Orange Blossom',
               '/Users/macbook/PycharmProjects/Flowers/OrangeBlossom.jpg'],
              # Adding Florida and its values
              ['GA', 'Atlanta', 10723715, 'Cherokee Rose',
               '/Users/macbook/PycharmProjects/Flowers/CherokeeRose.jpg'],
              # Adding Georgia and its values
              ['HI', 'Honolulu', 1411151, 'Pua Aloalo',
               '/Users/macbook/PycharmProjects/Flowers/Pua.jpg'],
              # Adding Hawaii and its values
              ['ID', 'Boise', 1823594, 'Syringa',
               '/Users/macbook/PycharmProjects/Flowers/Syringa.jpg'],
              # Adding Idaho and its values
              ['IL', 'Springfield', 12620571, 'Purple Violet',
               '/Users/macbook/PycharmProjects/Flowers/Violet.jpg'],
              # Adding Illinois and its values
              ['IN', 'Indianapolis', 6768941, 'Peony',
               '/Users/macbook/PycharmProjects/Flowers/Peony.jpg'],
              # Adding Indiana and its values
              ['IA', 'Des Moines', 3161522, 'Wild Prairie Rose',
               '/Users/macbook/PycharmProjects/Flowers/WildRose.jpg'],
              # Adding Iowa and its values
              ['KS', 'Topeka', 2915269, 'Sunflower',
               '/Users/macbook/PycharmProjects/Flowers/Sunflower.jpg'],
              # Adding Kansas and its values
              ['KY', 'Frankfort', 4474193, 'Goldenrod',
               '/Users/macbook/PycharmProjects/Flowers/GoldenRod.jpg'],
              # Adding Kentucky and its values
              ['LA', 'Baton Rouge', 4637898, 'Magnolia',
               '/Users/macbook/PycharmProjects/Flowers/Magnolia.jpg'],
              # Adding Louisiana and its values
              ['ME', 'Augusta', 1349367, 'White Pine Cone and Tassel',
               '/Users/macbook/PycharmProjects/Flowers/WhitePine.jpg'],
              # Adding Maine and its values
              ['MD', 'Annapolis', 6055558, 'Black-Eyed Susan',
               '/Users/macbook/PycharmProjects/Flowers/Susan.jpg'],
              # Adding Maryland and its values
              ['MA', 'Boston', 6902371, 'Mayflower',
               '/Users/macbook/PycharmProjects/Flowers/Mayflower.jpg'],
              # Adding Massachusetts and its values
              ['MI', 'Lansing', 9989642, 'Apple Blossom',
               '/Users/macbook/PycharmProjects/Flowers/AppleBlossom.jpg'],
              # Adding Michigan and its values
              ['MN', 'Saint Paul', 5673015, 'Pink and White Lady Slipper',
               '/Users/macbook/PycharmProjects/Flowers/LadySlipper.jpg'],
              # Adding Minnesota and its values
              ['MS', 'Jackson', 2971278, 'Magnolia',
               '/Users/macbook/PycharmProjects/Flowers/Magnolia.jpg'],
              # Adding Mississippi and its values
              ['MO', 'Jefferson City', 6153233, 'White Hawthorn Blossom',
               '/Users/macbook/PycharmProjects/Flowers/HawthornBlossom.jpg'],
              # Adding Missouri and its values
              ['MT', 'Helena', 1076891, 'Bitterroot',
               '/Users/macbook/PycharmProjects/Flowers/Bitterroot.jpg'],
              # Adding Montana and its values
              ['NE', 'Lincoln', 1943202, 'Goldenrod',
               '/Users/macbook/PycharmProjects/Flowers/GoldenRod.jpg'],
              # Adding Nebraska and its values
              ['NV', 'Carson City', 3132971, 'Sagebrush',
               '/Users/macbook/PycharmProjects/Flowers/Sagebrush.jpg'],
              # Adding Nevada and its values
              ['NH', 'Concord', 1365957, 'Purple Lilac',
               '/Users/macbook/PycharmProjects/Flowers/PurpleLilac.jpg'],
              # Adding New Hampshire and its values
              ['NJ', 'Trenton', 8878355, 'Violet',
               '/Users/macbook/PycharmProjects/Flowers/Violet.jpg'],
              # Adding New Jersey and its values
              ['NM', 'Santa Fe', 2100917, 'Yucca Flower',
               '/Users/macbook/PycharmProjects/Flowers/Yucca.jpg'],
              # Adding New Mexico and its values
              ['NY', 'Albany', 19376771, 'Rose',
               '/Users/macbook/PycharmProjects/Flowers/Rose.jpg'],
              # Adding New York and its values
              ['NC', 'Raleigh', 10594553, 'Dogwood',
               '/Users/macbook/PycharmProjects/Flowers/Dogwood.jpg'],
              # Adding North Carolina and its values
              ['OH', 'Columbus', 11701859, 'Scarlet Carnation',
               '/Users/macbook/PycharmProjects/Flowers/Carnation.jpg'],
              # Adding Ohio and its values
              ['OK', 'Oklahoma City', 3973707, 'Mistletoe',
               '/Users/macbook/PycharmProjects/Flowers/Mistletoe.jpg'],
              # Adding Oklahoma and its values
              ['OR', 'Salem', 4253588, 'Oregon Grape',
               '/Users/macbook/PycharmProjects/Flowers/OregonGrape.jpg'],
              # Adding Oregon and its values
              ['PA', 'Harrisburg', 12803056, 'Mountain Laurel',
               '/Users/macbook/PycharmProjects/Flowers/MountainLaurel.jpg'],
              # Adding Pennsylvania and its values
              ['RI', 'Providence', 1060435, 'Violet',
               '/Users/macbook/PycharmProjects/Flowers/Violet.jpg'],
              # Adding Rhode Island and its values
              ['SC', 'Columbia', 5213272, 'Yellow Jessamine',
               '/Users/macbook/PycharmProjects/Flowers/Jessamine.jpg'],
              # Adding South Carolina and its values
              ['ND', 'Bismarck', 766044, 'Wild Prairie Rose',
               '/Users/macbook/PycharmProjects/Flowers/WildRode.jpg'],
              # Adding North Dakota and its values
              ['SD', 'Pierre', 890620, 'Pasque Flower',
               '/Users/macbook/PycharmProjects/Flowers/Pasque.jpg'],
              # Adding South Dakota and its values
              ['TN', 'Nashville', 6886717, 'Iris',
               '/Users/macbook/PycharmProjects/Flowers/Iris.jpg'],
              # Adding Tennessee and its values
              ['TX', 'Austin', 29363096, 'Bluebonnet',
               '/Users/macbook/PycharmProjects/Flowers/Bluebonnet.jpg'],
              # Adding Texas and its values
              ['UT', 'Salt Lake City', 3258366, 'Sego Lily',
               '/Users/macbook/PycharmProjects/Flowers/SegoLily.jpg'],
              # Adding Utah and its values
              ['VT', 'Montpelier', 623620, 'Red Clover',
               '/Users/macbook/PycharmProjects/Flowers/RedClover.jpg'],
              # Adding Vermont and its values
              ['VA', 'Richmond', 8569752, 'Dogwood',
               '/Users/macbook/PycharmProjects/Flowers/Dogwood.jpg'],
              # Adding Virginia and its values
              ['WA', 'Olympia', 7705917, 'Pink Rhododendron',
               '/Users/macbook/PycharmProjects/Flowers/PinkRhododendron.jpg'],
              # Adding Washington and its values
              ['WV', 'Charleston', 1780003, 'Rhododendron',
               '/Users/macbook/PycharmProjects/Flowers/Rhododendron.jpg'],
              # Adding West Virginia and its values
              ['WI', 'Madison', 5837462, 'Wood Violet',
               '/Users/macbook/PycharmProjects/Flowers/WoodViolet.jpg'],
              # Adding Wisconsin and its values
              ['WY', 'Cheyenne', 579917, 'Indian Paintbrush',
               # Adding Wyoming and its values
               '/Users/macbook/PycharmProjects/Flowers/Paintbrush.jpg']]

    states.sort()   # Using the sort() function to sort the states list into alphabetical order

    return states   # Returning the states list

# Start of display_states() function definition

def display_states():

    """The display_states() function calls the get_states() function
    and stores it in the states variable and then displays all U.S.
    States in Alphabetical order along with the Capital, State Population,
    and Flower."""

    states = get_states()   # Calling get_states() function and storing values in states variable

    # Calling len() function to get the length of states and storing in length variable

    length = len(states)

    print("\nState\tCapital\t\tPopulation\t\tFlower")    # Printing the column names

    # Using a for loop with the range() function to go through the states list

    for i in range(0, length):    # Start of for loop

        # Printing out all the values for all 50 states and formatting where needed

        print(f'\n{states[i][0]}\t{states[i][1]}\t\t{states[i][2]}\t\t{states[i][3]}')

# Start of get_state() function definition

def get_state():

    """The get_state() function prompts user for the state
    they would like to search for and then validates the
    users input"""

    # Creating get_state() function to prompt user for the state they want to search for

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through state prompt

        # Prompting user for their state and storing input in state variable

        state = input("Search for a state (Use the two letter abbreviation, i.e: MD): ")

        # Calling string_validation() function in if statement for input validation
        # Calling len() function for input string length validation

        if string_validation(state) and len(state) == 2:

            return state    # Returning user input and storing input in state variable

        print("Error - please enter a two letter abbreviation of the state, i.e: MD.")

# Start of search_states() function definition

def search_states():

    """The search_states() function calls the get_states() function
    and stores the state value in the states variable. It then
    searches for the specific state and displays the appropriate
    Capital name, State Population, and an image of the associated State Flower."""

    states = get_states()   # Calling get_states() function and storing values in states variable

    # Calling len() function to get the length of states

    length = len(states)    # Storing value in length variable

    state = get_state()     # Calling get_state() function and storing value in state variable

    # Using a for loop with the range() function to iterate over the list of states and their values

    for i in range(0, length):

        # Using an if statement with the condition that the user's inputted state is the same as a
        # state from the list

        if state == (states[i][0]):

            print("\nState\t\tCapital\t\tPopulation\t\tFlower")    # Column names

            # Printing out all the values for all 50 states and formatting where needed

            print(f'\n{states[i][0]}\t\t{states[i][1]}\t\t{states[i][2]}\t\t{states[i][3]}')

            # Using the plt.imread() function and using the flower's image file path as the argument
            # and storing in img variable

            img = plt.imread(states[i][4])

            # Using the plt.imshow() function and using the img variable as the argument

            plt.imshow(img)

            # Using plt.show() function to display the State Flower's image

            plt.show()

# Start of display_bar_graph() function definition

def display_bar_graph():

    """The display_bar_graph() function provides a bar graph
    of the top 5 populated States showing their overall population."""

    # Displaying the top 5 populated States from lowest to highest

    print("The top 5 populated States (lowest to highest) are "
          "Pennsylvania, New York, Florida, Texas, and California.")

    # The names variable consists of the x-axis names (the top 5 populated states)

    names = ['Pennsylvania', 'New York', 'Florida', 'Texas', 'California']

    # The values variable consists of the population of the states (in millions)

    values = [12.8, 19.3, 21.7, 29.3, 39.5]

    # Using the plt.figure() function to increase the size of the figure to 3000x1000

    plt.figure(figsize=(15, 5))

    # Using the plt.subplot() function to add an axes to the current figure

    plt.subplot()

    # Using the plt.bar() function to make a bar plot with the names and values

    plt.bar(names, values)

    # Using the plt.suptitle() function to add a centered suptitle to the figure

    plt.suptitle("Top 5 Populated States (in Millions)")

    # Using the plt.show() function to display the bar graph figure

    plt.show()

# Start of get_state_p2() function definition

def get_state_p2():

    """The get_state_p2() function prompts user for the state
    they would like to search for to update the population
    and then validates the users input"""

    # Creating get_state_p2() function to prompt user for the state they want to search for

    running = True  # Creating running boolean variable for while loop condition

    # While loop allows user to be continuously prompted if user input is invalid

    while running:  # Start of while loop to loop through state prompt

        # Prompting user for their state and storing input in state variable

        state = input("Search for a state to update the population of the state"
                      " (Use the two letter abbreviation, i.e: MD):")

        # Calling string_validation() function in if statement for input validation
        # Calling len() function for input string length validation

        if string_validation(state) and len(state) == 2:

            return state    # Returning user input and storing input in state variable

        print("Error - please enter a two letter abbreviation of the state., i.e: MD")

# Start of update_population() function definition

def update_population():

    """The update_population() function calls the get_states() function
    and stores the state value in the states variable and then calls the
    get_state_p2() function and stores the value in the state variable. The
    program then updates the given states population."""

    states = get_states()   # Calling get_states() function and storing values in states variable

    # Calling len() function to get the length of states

    length = len(states)    # Storing value in length variable

    # Calling get_state_p2() function and storing value in state variable

    state = get_state_p2()

    # Using a for loop with the range() function to iterate over the list of states and their values

    for i in range(0, length):

        # Using an if statement with the condition that the user's inputted state is the same as a
        # state from the list

        if state == (states[i][0]):     # Start of if statement

            # Storing a population value from the states list into the population variable

            population = states[i][2]

            # Updating the population value of the given state
            # from the states list with the population variable

            states[i][2] = population

            # Displaying the updated population of the given state

            print(f'\nUpdated Population of {state}: {population}')

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

    # 1. Display all U.S. States in Alphabetical order along with the
    # Capital, State Population, and Flower
    # 2. Search for a specific state and display the appropriate Capital name
    # State Population, and an image of the associated State Flower.
    # 3. Provide a Bar graph of the top 5 populated States showing their overall population
    # 4. Update the overall state population for a specific state.
    # 5. Exit program

    print("\nThe following menu options give the user the options to display, sort "
          "and update, as needed a List of U.S. states containing the state capital,"
          " overall state population, and state flower.")

    print("1. Display all U.S. States in Alphabetical order along with the"
          " Capital, State Population, and Flower")    # Option 1

    print("2. Search for a specific state and display the appropriate"
          " Capital name, State Population, and an image of the associated"
          " State Flower.")   # Option 2

    print("3. Provide a Bar graph of the top 5 populated States showing"
          " their overall population")    # Option 3

    print("4. Update the overall state population for a specific state.")  # Option 4

    print("5. Exit program\n")    # Option 5

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

    # This menu-driven application allows a user to display, sort and update, as needed
    # a List of U.S. states containing the state capital, overall state population, and
    # state flower.

    print("**********************************************************")  # Header

    print("Welcome to the U.S. States List Python Program!")  # Welcome message

    choice = 0  # Creating the variable choice to control the loop and store user's choice

    # Creating a while loop with the condition that the user's choice is not exit program

    while choice != EXIT_PROGRAM:  # Start of while loop

        # Calling the display_menu() function to display the menu
        # And storing user input value inside choice variable

        choice = display_menu()

        if choice == DISPLAY_STATES:  # If user's choice is option 1

            # Calling display_states() function

            display_states()

        if choice == SEARCH_STATES:     # If user's choice is option 2

            # Calling search_states() function

            search_states()

        if choice == DISPLAY_BAR_GRAPH:      # If user's choice is option 3

            # Calling display_bar_graph() function

            display_bar_graph()

        if choice == UPDATE_POPULATION:      # If user's choice is option 4

            # Calling update_population() function

            update_population()

        if choice == EXIT_PROGRAM:    # If user choice is option 5

            # Thank you and goodbye message

            print("\nThanks for trying the U.S. States List Python Program!"
                  " Take care!")

            break   # Using a break statement to stop the execution of the while loop


# Calling main method

if __name__ == "__main__":

    main()  # Calling main method
