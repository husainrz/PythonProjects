# Husain Rizvi

# Lab 7 - Lists

# This program uses seven functions and a list to store and process test scores. This program gives the user
# several different options on what to do with the test scores, whether they want to get the score metrics
# (min/max/avg), or to mine the scores, update the scores, or display the scores.


# Creating and defining the empty list of scores

scores_list = []

# Defining the main function

def main():

    get_scores()

    # Creating a counter variable as a control for the while loop 

    count = 0

    while count == 0:   # Using a while loop as the repetition control structure to loop the menu

        # Calling the display menu function to display the menu 

        display_menu()

        # Prompting user for a menu choice

        userChoice = input( "Enter your choice: " )

        # Converting menu choice from String to int

        userChoice = int( userChoice )

        # Using an if statement as the decision control structure to determine which function to execute

        if userChoice > 0 & userChoice < 6: # Assigning a range

            # Choice 1: Score Metrics

            if userChoice == 1:

                # Calling score_metrics function

                score_metrics(scores_list)

            # Choice 2: Mine Scores    

            elif userChoice == 2:

                # Calling mine_scores function

                mine_scores(scores_list)

            # Choice 3: Update Scores    

            elif userChoice == 3:

                # Calling update_scores functio

                update_scores(scores_list)

            # Choice 4: Display Scores    

            elif userChoice == 4:

                # Calling display_scores function
    
                display_scores(scores_list)

            # Choice 5: Quit    

            else:

                count = 1

                print( "\nExiting the program..." )

        else:

            print( "\nError - please input an integer between 1 - 5.\n" )


# Defining the get_scores function

def get_scores():

    # Asking user for number of test scores being entered and storing input in numScores variable

    numScores = input( "\nHow many scores will you be entering: " )

    # Converting input from String to int

    numScores = int( numScores )

    # Using a for loop to repeatedly prompt the user to input scores until the specified number has been entered
    # Using the range function with the i counter variable to make sure the user is prompted the appropriate number of times

    for i in range( 1, numScores + 1 ):

        # Prompting user to input scores and using i variable to indicate which number test score it is 

        score = input( f'Enter test score {i} (0-100): ' )

        # Converting input from String to int

        score = int(score)

        # If statement in case of input error

        if score < 0 or score > 100:

            print( "Error - Please enter a number between 0 and 100." )

        else:

            # Appending the scores inputted by the user into the scores_list list

            scores_list.append(score)
    

# Defining the display_menu function that displays the menu

def display_menu():

    # Displaying the menu

    print( "\n1. Score Metrics (min/max/avg)" )

    print( "2. Mine Scores (low/high scores)" )

    print( "3. Update Scores" )

    print( "4. Display Scores" )

    print( "5. Quit" )
    
    # End of display_menu function


# Defining the mine_scores function and using the scores list as the parameter

def score_metrics(scores_list):

    # Outputting the number of scores by using the length function

    print( f'\n\nNumber of Scores: {len(scores_list)}' )

    # Outputting the highest score by using the max function and displaying with two decimal points

    print( f'\nHigh Score:      {max(scores_list):.2f}' )

    # Outputting the lowest score by using the min function and displaying with two decimal points

    print( f'Low Score:       {min(scores_list):.2f}' )

    # Outputting the lowest score by using the sum and length function to calculate the average
    # and displaying with two decimal points

    print( f'Average Score:   {sum(scores_list) / len(scores_list):.2f}' )
    

# Defining the mine_scores function and using the scores list as the parameter

def mine_scores(scores_list):

    # Using list comprehension to create the new sorted_list which has the scores that are greater than or equal to the average score

    sorted_list = [top for top in scores_list if top >= ( sum(scores_list) / len(scores_list) ) ]

    # Using the sort function to sort the new sorted_list in ascending order

    sorted_list.sort()

    # Displaying the new sorted list as specified

    print( "\n\nTop Scores" )

    print( f' {sorted_list[0]:.2f}' )

    print( f' {sorted_list[1]:.2f}' )

    # Using list comprehension to create the new sorted_list2 which has the scores that are less than the average score

    sorted_list2 = [bottom for bottom in scores_list if bottom < ( sum(scores_list) / len(scores_list) ) ]

    # Using the sort function to sort the new sorted_list2 in ascending order

    sorted_list2.sort()

    # Displaying the new sorted list as specified 

    print( "\nBottom Scores" )

    print( f' {sorted_list2[0]:.2f}' )

    print( f' {sorted_list2[1]:.2f}' )

    print( f' {sorted_list2[2]:.2f}' )
    
    
# Defining the update_scores function

def update_scores(scores_list):

    print( "\nUpdate test score" )

    # Counter variable for for loop

    count = 0

    # Creating a for loop to iterate through and display the scores_list list

    for score in scores_list:

        count += 1

        # Count variable is being used to count the number of scores and display them one after the other

        print( f'{count}. {score:.2f}' )

    # Prompting user to input the index of the score number they would like to update

    scoreToUpdate = input( "Select score number to update: " )

    # Converting input from string to int

    scoreToUpdate = int( scoreToUpdate )

    # Prompting user to input the updated score

    updatedScore = input( "Enter new score: " )

    # Converting input from String to int

    updatedScore = int( updatedScore )

    # Updated the score by selecting the correct index and setting it equal to the updated score

    scores_list[scoreToUpdate - 1] = updatedScore

    # Creating new counter variable for new for loop

    count2 = 0

    # Creating a for loop to iterate through and display the new updated score_list

    for score in scores_list:

        count2 += 1

        # Count variable is being used to count the number of scores and display them one after the other

        print( f'{count2}. {score:.2f}' )


# Defining the display_scores function

def display_scores(scores_list):

    print( "\nScores in reverse order:" )

    # Creating a new list that is reversed using the old scores_list but using a slice operation with negative indices to reverse the list

    reversed_list = scores_list[::-1]

    # Creating a for loop to iterate through and display the new updated reversed reversed_list

    for score in reversed_list:

        print( f'   {score:.2f}' )


# Calling the main function

main()

# End of Lab 7 - Lists
