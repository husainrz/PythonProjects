# Husain Rizvi

# SDEV 300 - Lab 8 - Flask Login

"""This program imports Flask and render_template from flask
and creates different methods for the different html files
so that render_template can render the web page for the files.
This program also creates login and registration forms for the web
page. Additional functionality that this program provides is a
password update form as well as a logger and additional authentication
functions."""

from datetime import date   # importing date from datetime library
import logging      # importing logging library
# importing Flask, render_template, redirect, url_for, and request from flask library
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)   # Assigning the name of the Flask instance to app

# Creating basic configuration for logging to include a timestamp
# with the date, time, and IP address included

logging.basicConfig(
    level=logging.DEBUG,    # For debugging
    # Including date, timestamp, and a warning message
    format="{asctime} {levelname:<8} {message}",
    style='{'
)

# Start of complex_pwd() function definition

def complex_pwd(pwd):

    """"The complex_pwd() function takes a string of a password
    as its argument and validates the complexity of the password
    and returns whether it is valid or not. The password must be
    at least 12 characters long, with at least 1 upper case, 1
    lower case, 1 number & 1 special character."""

    # Creating complex_pwd() function to validate user's inputted password
    # Creating a string of potential special characters in password

    special_char = "!@#$%'()*+,-./:;<=>?@[]^_`{|}~"

    valid = True    # Creating boolean condition variable named valid

    # Using the open() function to open the CommonPassword.txt file for reading
    # Assigning it to the common1 variable

    common1 = open("CommonPassword.txt", "r")

    # Using the read() function to read through the CommonPassword.txt file
    # Assigning it to the common variable

    common = common1.read()

    if pwd in common:   # If pwd is in the text file

        valid = False   # Boolean condition variable valid is False

    if len(pwd) < 12:  # If length of the given password is less than 12

        valid = False   # Boolean condition variable valid is False

    # Using any(), isupper(), and islower() functions to check
    # for upper & lower case characters in password string
    # If there isn't any (if not any()) upper & lower case
    # characters in password string, valid = False

    if not any(char.isupper() for char in pwd) and not any(char.islower() for char in pwd):

        valid = False   # Boolean condition variable valid is False

    # Using any() & isdigit() function to check for numbers
    # & lower case characters in password string
    # If there isn't any (if not any()) upper & lower case
    # characters in password string, valid = False

    if not any(char.isdigit() for char in pwd) and not any(char in special_char for char in pwd):

        valid = False   # Boolean condition variable valid is False

    if valid:   # If valid is True

        return valid    # Return valid

@app.route('/')     # Decorator for the login() function
@app.route('/login.html', methods=['GET', 'POST'])      # Routing to /login.html page
def login():     # Start of login() function

    """This function renders the template for the login page using the
    login.html file and render_template and adds the title for the login page.
    This function also ensures that both the username and password entered
    are already in the system (in the text file)."""

    # Creating login() function to render the template for the login page
    # and check to ensure that the username and password entered are in the
    # system (database.txt).

    # Using request.method to ensure registration.html is using the POST method
    # If request.method is POST

    if request.method == "POST":

        # If the email value and password value entered is in the form

        if "email" in request.form and "password" in request.form:

            # Logging message for log in attempt

            logging.warning('Log In Attempt')

            # Using request.form to assign the email value entered from the form
            # into the username string variable

            username = request.form['email']

            # Using request.form to assign the password value entered from the form
            # into the password string variable

            pwd = request.form['password']

            # Using the open() function to open the database.txt file for reading
            # Assigning it to the database1 variable

            database1 = open("database.txt", "r")

            # Using the read() function to read through the database.txt file
            # Assigning it to the database variable

            database = database1.read()

            # If the username (email) and password values are in the text file

            if username in database and pwd in database:

                # Logging warning message for log in confirmation

                logging.warning('Log In Confirmed')

                # Using redirect() and url_for() functions to redirect
                # the user to the home page if their login credentials
                # were found

                return redirect(url_for('home'))

            else:

                # Logging warning message for failed login

                logging.warning('Failed log in')

                # Using render_template to render the template for the html file and
                # assign it the appropriate title, prompt, date, and error message

                return render_template('login.html', title="Top North American Predators Web Page",
                                       prompt="Please Log In",
                                       date=date.today(),
                                       error="****Username or password not found. "
                                              "Please re-enter or register for an account.****")

    # Using render_template to render the template for the html file and
    # assign it an appropriate title, prompt, and date

    return render_template('login.html', title="Top North American Predators Web Page",
                           prompt="Please Log In",
                           date=date.today())

# Decorator for the registration() function
@app.route('/registration.html', methods=['GET', 'POST'])
def registration():     # Start of registration() function

    """This function renders the template for the registration page using the
    registration.html file and render_template and adds the title for the registration page.
    This function also calls the complex_pwd() function to validate the password entered, and
    then stores the username and password entered into the database.txt text file if the password
    is validated."""

    # Creating registration() function to render the template for the registration page
    # and calls the complex_pwd() function to validate the password's complexity. The
    # program then stores the username and password in the database.txt file if
    # the password is complex enough.

    # Using request.method to ensure registration.html is using the POST method
    # If request.method is POST

    if request.method == "POST":

        # If the email value and password value entered is in the form

        if "email" in request.form and "password" in request.form:

            # Logging warning message for registration attempt

            logging.warning('User registering for account')

            # Using request.form to assign the email value entered from the form
            # into the username string variable

            username = request.form['email']

            # Using request.form to assign the password value entered from the form
            # into the password string variable

            pwd = request.form['password']

            # Calling the complex_pwd function and storing the password string
            # as the argument to validate the password

            # If complex_pwd returns True

            if complex_pwd(pwd):

                # Using the open() function to open the database.txt file in write mode
                # and assigned it an alias 'database'

                with open('database.txt', "w") as database:

                    # Using the writelines() function to write the username
                    # and password into the database.txt file onto new lines

                    database.writelines(f'{username}\n{pwd}')

                # Logging warning message for registration confirmation

                logging.warning('Registration Confirmed')

                # Using redirect() and url_for() functions to redirect
                # the user to the login page if password entered was not complex enough

                return redirect(url_for('login'))

            # Using render_template to render the template for the html file and
            # assign it the appropriate title, date, and error message

            return render_template('registration.html',
                                   title="Top North American Predators Web Page",
                                   date=date.today(),
                                   error="***********Please enter a more "
                                         "complex password.***********")

    # Using render_template to render the template for the html file and
    # assign it the appropriate title, and date

    return render_template('registration.html', title="Top North American Predators Web Page",
                           date=date.today())

# Decorator for the password() function
@app.route('/password.html', methods=['GET', 'POST'])
def password():     # Start of password() function

    """This function renders the template for the password update page using the
    password.html file and render_template and adds the title for the password page.
    This function also ...."""

    # Creating registration() function to render the template for the registration page
    # and calls the complex_pwd() function to validate the password's complexity. The
    # program then stores the username and password in the database.txt file if
    # the password is complex enough.

    # Using request.method to ensure registration.html is using the POST method
    # If request.method is POST

    if request.method == "POST":

        # If the email value and password value entered is in the form

        if "old" in request.form and "email" in request.form:

            # Logging warning message for password update attempt

            logging.warning('User updating/changing password')

            # Using request.form to assign the email value entered from the form
            # into the email string variable

            email = request.form['email']

            # Using request.form to assign the password value entered from the form
            # into the password string variable

            pwd = request.form['password']

            # Calling the complex_pwd function and storing the password string
            # as the argument to validate the password

            # If complex_pwd returns True

            if complex_pwd(pwd):

                # Using the open() function to open the database.txt file in write mode
                # and assigned it an alias 'database'

                with open('database.txt', "w") as database:

                    # Using the writelines() function to write the username
                    # and password into the database.txt file onto new lines

                    database.writelines(f'{email}\n{pwd}')

                # Logging warning message for password update confirmation

                logging.warning('Password Update Confirmed')

                # Using redirect() and url_for() functions to redirect
                # the user to the login page if password entered was not complex enough

                return redirect(url_for('login'))

            # Using render_template to render the template for the html file and
            # assign it the appropriate title, date, and error message

            return render_template('[password].html',
                                   title="Top North American Predators Web Page",
                                   date=date.today(),
                                   error="***********Please enter a more "
                                         "complex password that is not common.***********")

    # Using render_template to render the template for the html file and
    # assign it the appropriate title, and date

    return render_template('password.html', title="Top North American Predators Web Page",
                           date=date.today())

@app.route('/home.html')     # Decorator for the home() function
def home():     # Start of home() function

    """This function renders the template for the home page using the
    home.html file and render_template and adds the title for the home page."""

    # Using render_template to render the template for the html file and
    # assign it an appropriate title and date

    return render_template('home.html', title="Top Modern North American Predators",
                           date=date.today())

@app.route('/polar.html')   # Decorator for the polar() function
def polar():    # Start of polar() function

    """This function renders the template for the polar bear page using the
    polar.html file and render_template and adds the title, name, and
    classification for the page."""

    # Using render_template to render the template for the html file and
    # assign it an appropriate title, name, and classification

    return render_template('polar.html', title="Top North American Predator: Polar Bears",
                           name="Ursus maritimus", classification="Mammal")

@app.route('/grizzly.html')     # Decorator for the grizzly() function
def grizzly():      # Start of grizzly() function

    """This function renders the template for the grizzly bear page using the
    grizzly.html file and render_template and adds the title, name, and
    classification for the page."""

    # Using render_template to render the template for the html file and
    # assign it an appropriate title, name, and classification

    return render_template('grizzly.html', title="Top North American Predator: Grizzly Bears",
                           name="Ursus arctos horribilis", classification="Mammal")

@app.route('/lion.html')    # Decorator for the lion() function
def lion():     # Start of lion() function

    """This function renders the template for the mountain lion page using the
    lion.html file and render_template and adds the title, name, and classification for the page."""

    # Using render_template to render the template for the html file and
    # assign it an appropriate title, name, and classification

    return render_template('lion.html', title="Top North American Predator: Mountain Lions",
                           name="Puma concolor", classification="Mammal")


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
