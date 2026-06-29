#This is a code which asks the user to guess a password once the user guesses the password the user will move on to the next part of the code.
name = input("What is your name? :")
print(name)
print(f"Hello {name} Welcome to my python program where i test some code sometimes.")
age = input("How old are you? :")
print(f"Hello {name} you are {age} years old")
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