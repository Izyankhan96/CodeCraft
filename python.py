#This is a code which asks the user to guess a password once the user guesses the password the user will move on to the next part of the code.
print("Welcome to the Fun Program!")
name = input("What is your name? :")
while name != "Izyan":
    print("Please re-enter your name as that name was not recognized")
    name = input("What is your name? :")
print("Hello Izyan! Welcome back!")
password = input("Please enter your password :")
while password != "Izyan124":
    print("That is incorrect please try again")
    password = input("Please enter your password? :")
print("That is correct please answer the questions below!")
question = input("Try guessing the number :")
while question != "738721":
    print("Please try again")
    question = input("Try guessing the number :")
print("Thats correct now lets try something harder this time")
guess = input("Try guessing the password :")
while guess != "Python Program":
    print("That is incorrect please try again")
    guess = input("Try guessing the password :")
print("That is correct!")
flavors = ["Ranch"]
flavors.append("Chicken")
flavors.append("Margarita")
for i in range(len(flavors)):
    print(i + 1, flavors[i])
choice = input("What is your favorite flavor? :")
while choice not in flavors:
    print("Sorry we dont have that flavor Please try again ")
    choice = input("What is your favorite flavor? :")
print(f"{choice} is a great flavor")
icecream = ["Vanilla"]
icecream.append("Chocolate")
icecream.append("Mango")
for i in range(len(icecream)):
    print(i + 1, icecream[i])
choice2 = input("Whats your favorite ice cream flavor :")
while choice2 not in icecream:
    print("Sorry we dont have that flavor please try again")
    choice2 = input("Pick an Ice cream flavor :")
print(f"{choice2} is a great flavor")
options = ["Dog","Cat","Tiger"]
options.append("Lion")
options.append("Giraffe")
options.append("Turtle")
options.append("Dinosour")
for i in range(len(options)):
    print(i + 1, options[i])
question = input("Whats your favorite animal? :")
while question not in options:
    print("Sorry please choose an animal from the given options")
    question = input("Whats your favorite animal? :")
print(f"{question} is a great pet")
print("Now lets try another guessing game")
guess2 = input("Try guessing the password :")
while guess2 != "PythonProgrambetter":
    print("That is incorrect please try again")
    guess2 = input("Try guessing the password :")
print("Thats correct lets try something harder with numbers and letters")
guess3 = input("Try guessing the password :")
while guess3 != "PythonProgram3637":
    print("That is incorrect please try again")
    guess3 = input("Try guessing the password :")
print("Thats correct now lets try something harder with numbers, letters and symbols")
guess4 = input("Try guessing the password :")
while guess4 != "PythonProgram3637!":
    print("That is incorrect please try again")
    guess4 = input("Try guessing the password :")
print("Thats correct!")
print("Now lets do this last one")
guess5 = input("Try guessing the password :")
while guess5 != "pythonProgram3736@3667":
    print("That is incorrect please try again")
    guess5 = input("Try guessing the password :")
print("Thats correct! I have a couple more questions for you")
colors = ["Red","Blue","Green","Yellow","Orange","Purple"]
colors.append("Pink")
colors.append("Silver")
colors.append("Gold")
colors.append("White")
colors.append("Black")
colors.append("Brown")
colors.append("Gray")
colors.append("Cyan")
colors.append("Magenta")
colors.append("Teal")
colors.append("Maroon")
colors.append("Navy")
colors.append("Olive Green")
for i in range(len(colors)):
    print(i + 1, colors[i])
question2 = input("What is your favorite color? :")
while question2 not in colors:
    print("Sorry please choose a color from the given options")
    question2 = input("What is your favorite color? :")
print(f"{question2} is a great color")
cars = {"Mazda","Toyota","Tesla","Honda","Hyundai","Lexus","BYD"}
for i in range(len(cars)):
    print(i + 1, cars[i])
question3 = input("Whats your favorite car choose from the options given below :")
print(f"{question3}, is a great car")