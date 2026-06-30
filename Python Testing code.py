name = input("Hello Welcome to the grade checker what is your name? :")
print(f"Hello, {name} I see your name in our system")
Id_number = input("Please provide your grade checking number :")
while Id_number != "1234566":
    print("That is incorrect please Try again :")
    Id_number = input("Please provide your grade checking number :")
print("Alright! Please enter your password below")
password = input("Password :")
while password != "TheGradeChecker71":
    print("That is not correct Please re-enter your password :")
    password = input("Password :")
print(f"That is correct Welcome back {name}")
print("Here is your grade :")
grade = 96
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C")
