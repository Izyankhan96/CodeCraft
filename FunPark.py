print("Welcome to the Fun Park! Please tell me your name and age to verify your ticket")
name = input("Name : ").strip().title()
age = input("Age : ").strip()
while not age.isdigit():
    print("Please type your age as a number.")
    age = input("Age : ").strip()
age = int(age)
if age < 15:
    print(f"Sorry {name}, you must be 15 or older to enter.")
    exit()
print(f"Welcome {name}! Please set a PIN. You'll enter it at every ride (numbers only)")
pin = input("PIN : ").strip()
while not pin.isdigit():
    print("Your PIN has to be numbers only.")
    pin = input("PIN : ").strip()
print(f"Alright, your PIN is {pin}")
rides = ["adventure", "harry potter ride", "waterslide", "roller coaster"]
while True:
    print(rides)
    choice = input("Ride (or 'leave' to exit) : ").strip().lower()
    if choice == "leave":
        print("Thanks for visiting the Fun Park!")
        break
    if choice not in rides:
        print("That ride isn't on the map. Please pick one from the list.")
        continue
    pin_verify = input("Please enter your PIN : ").strip()
    if pin_verify == pin:
        print(f"You may enter the {choice}. Enjoy!")
    else:
        print("Wrong PIN. You can't go on this ride.")