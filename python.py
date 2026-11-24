#This is a code which asks the user to guess a password once the user guesses the password the user will move on to the next part of the code.

def pick_from(question, options, wrong_message):
    """Show a numbered list and keep asking until the answer is on it.

    Accepts the number shown (like 2) or the name in any capitals
    (like "chicken"), and returns the name exactly as it is in the list.
    """
    for number, option in enumerate(options, start=1):
        print(number, option)
    while True:
        answer = input(question).strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        for option in options:
            if answer.lower() == option.lower():
                return option
        print(wrong_message)

print("Welcome to the Fun Program!")
name = input("What is your name? :").strip()
while name.lower() != "izyan":
    print("Please re-enter your name as that name was not recognized")
    name = input("What is your name? :").strip()
print("Hello Izyan! Welcome back!")
password = input("Please enter your password :")
while password != "Izyan124":
    print("That is incorrect please try again")
    password = input("Please enter your password :")
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
choice = pick_from("What is your favorite flavor? :", flavors,
                   "Sorry we dont have that flavor Please try again")
print(f"{choice} is a great flavor")
icecream = ["Vanilla"]
icecream.append("Chocolate")
icecream.append("Mango")
choice2 = pick_from("Whats your favorite ice cream flavor :", icecream,
                    "Sorry we dont have that flavor please try again")
print(f"{choice2} is a great flavor")
options = ["Dog","Cat","Tiger"]
options.append("Lion")
options.append("Giraffe")
options.append("Turtle")
options.append("Dinosaur")
animal = pick_from("Whats your favorite animal? :", options,
                   "Sorry please choose an animal from the given options")
print(f"{animal} is a great animal")
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
question2 = pick_from("What is your favorite color? :", colors,
                      "Sorry please choose a color from the given options")
print(f"{question2} is a great color")
cars = ["Mazda","Toyota","Tesla","Honda","Hyundai","Lexus","BYD"]
question3 = pick_from("Whats your favorite car? Choose from the options above :", cars,
                      "Sorry please choose a car from the given options")
print(f"{question3} is a great car")