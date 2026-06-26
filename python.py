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
choice = input("What flavor do you like? :")
print(f"{choice} is a great flavor")