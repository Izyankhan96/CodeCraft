name = input("Hello Welcome to the grade checker what is your name? :")
print(f"Hello, {name} I see your name in our system")
password = input("What is your password :")
while password != "TheGradeChecker71":
    print("That is not correct Please re-enter your password :")
    password = input("What is your password")
print(f"That is correct Welcome back {name}")
print("Here is your grade :")
grade = 96
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C")
