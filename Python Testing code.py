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
cars = ["Mazda","Toyota","Tesla","Honda","Hyundai","Lexus","BYD"]
for i in range(len(cars)):
    print(i + 1, cars[i])
question3 = input("Whats your favorite car choose from the options given below :")
print(f"{question3}, is a great car")
