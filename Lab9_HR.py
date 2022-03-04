# Husain Rizvi

# Lab 9 - Objects

# This program creates a Car class and object from the class and performs three different tests.
# These tests, each with different modifications, outputs the speed of the card after a
# specific acceleration number and then the speed after a specific brake number.


# Creating the Car class with data attributes

class Car:

    # Using the __init__ method to initialize the data attributes and setting default values
    # Giving make and model default strings as a placeholder for the user to choose a default model and make of their choosing

    def __init__( self, year = 2000, make = 'default1', model = 'default2', speed = 0 ):
        
        self.__year = year

        self.__make = make

        self.__model = model

        self.__speed = speed

    # Creating the setYear method for the year data attribute
    # Sets the __year attribute with the year the car was made

    def setYear( self, year ):

        # Valid years accepted are 1903 and above, therefore the condition filters for years 1903 and above

        if year >= 1903:

            self.__year = year

    # Creating getYear method to return the __year attribute for the car

    def getYear( self ):

        return self.__year

    # Creating the setMake method for the __make data attribute
    # Sets the __make attribute (manufacturer)

    def setMake( self, make ):

        # Using the strip() method to return a copy of the string with all whitespace removed
        # to ensure the argument is not blank and made up of only spaces

        if make.strip() != "":

            self.__make = make

    # Creating getMake method to return the __make attribute for the car

    def getMake( self ):

        return self.__make

    # Creating the setModel method for the __model data attribute
    # Sets the __model attribute for the car

    def setModel( self, model ):

        # Using the strip() method to return a copy of the string with all whitespace removed
        # to ensure the argument is not blank and made up of only spaces

        if model.strip() != "":

            self.__model = model

    # Creating getModel method to return the __model attribute for the car

    def getModel( self ):

        return self.__model

    # Creating accelerate method that add 5 to the __speed attribute when it is called and
    # speed cannot exceed 120 mph.

    def accelerate( self ):

        # Adding 5 to the given __speed attribute when it is called and making sure speed does
        # not exceed 120 mph.

        self.__speed = self.__speed + 5

        if self.__speed > 120:

            self.__speed = self.__speed - 5

            print( f'Warning: you cannot go faster than 120 MPH!!\n' )

    # Creating brake method that subtracts 5 to the __speed attribute when it is called and
    # speed cannot go below 0 mph.

    def brake( self ):

        # Subtracting 5 to the given __speed attribuet when it is called and making sure speed does
        # not go below 0 mph.
        # Subtracting 5 to the given __speed attribute when

        # Subtracting 5 to the given __speed attribute when it is called and making sure speed does
        # not go below 0 mph.

        self.__speed = self.__speed - 5

        if self.__speed < 0:

            self.__speed = self.__speed + 5

            print( f'Unable to brake, the vehicle is not moving!!\n' )

    # Creating getSpeed method to return the current speed

    def getSpeed( self ):

        return self.__speed

    
# Start of Test 1 - Default starting speed of 0

print( f'Test 1 - Default starting speed of 0\n' )

# Creating a Car object, carObj, from the Car() class to perform three different tests

carObj = Car()

# Using a for loop with the range function to call the accelerate method for the car object five times
# and then getting the current speed of the car with the getSpeed method to display it
    
for i in range( 1, 6 ):

    # Calling the accelerate method

    carObj.accelerate()

    print( f'The speed of the car after acceleration number {i} is: {carObj.getSpeed()}' )

# Displaying an empty line to create space between the two method outputs

print( f'' )

# Using a for loop with the range function to call the brake method for the car object five times
# and then getting the current speed of the car with the getSpeed method to display it

for i in range( 1, 6 ):

    # Calling the brake method

    carObj.brake()

    print( f'The speed of the car after brake number {i} is: {carObj.getSpeed()}' )

# Start of Test 2 - Set the value of the __speed variable to 100 (for testing only)

print( f'\nTest 2 - Set the value of the __speed variable to 100 (for testing only)\n' )

# Setting the value of the __speed variable for carObj to 100 

carObj = Car( speed = 100 )

# Using a for loop with the range function to call the accelerate method for the car object five times
# and then getting the current speed of the car with the getSpeed method to display it

for i in range( 1, 6 ):

    # Calling the accelerate method

    carObj.accelerate()

    print( f'The speed of the car after acceleration number {i} is: {carObj.getSpeed()}' )

# Displaying an empty line to create space between the two method outputs

print( f'' )

# Using a for loop with the range function to call the brake method for the car object five times
# and then getting the current speed of the car with the getSpeed method to display it

for i in range( 1, 6 ):

    # Calling the brake method

    carObj.brake()

    print( f'The speed of the car after brake number {i} is: {carObj.getSpeed()}' )


# Start of Test 3 - Change the value of the __speed variable to -5 (for testing only)

print( f'\nTest 3 - Change the value of the __speed variable to -5 (for testing only)\n' )

# Setting the value of the __speed variable for carObj to -5 

carObj = Car( speed = -5 )

# Using a for loop with the range function to call the accelerate method for the car object five times
# and then getting the current speed of the car with the getSpeed method to display it

for i in range( 0, 5 ):

    # Calling the accelerate method

    carObj.accelerate()

    print( f'The speed of the car after acceleration number {i} is: {carObj.getSpeed()}' )

# Displaying an empty line to create space between the two method outputs

print( f'' )

# Using a for loop with the range function to call the brake method for the car object five times
# and then getting the current speed of the car with the getSpeed method to display it

for i in range( 1, 6 ):

    # Calling the brake method

    carObj.brake()

    print( f'The speed of the car after brake number {i} is: {carObj.getSpeed()}' )

# End of Lab 9 - Objects
