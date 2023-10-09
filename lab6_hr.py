# Husain Rizvi

# SDEV 300 - Lab 6 - Flask HTML Rendering

"""This program imports Flask and render_template from flask
and creates different methods for the different html files
so that render_template can render the web page for the files."""

from datetime import date   # importing date from datetime library
from flask import Flask, render_template     # importing Flask and render_template

app = Flask(__name__)   # Assigning the name of the Flask instance to app

@app.route('/')     # Decorator for the home() function
def home():     # Start of home() function

    """This function renders the template for the home page using the
    home.html file and render_template and adds the title for the home page."""

    # Using render_template to render the template for the html file and
    # assign it an appropriate title

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
