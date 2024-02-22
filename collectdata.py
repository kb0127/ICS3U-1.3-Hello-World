user_name = str(input("What is your name?: "))
age = int(input("What is your age?: ")) 
mark = float(input("Enter your current grade: "))
locker = str(input("Have you been assigned a locker? (y/n): "))

print("Name: " + user_name)
print("Age: " + str(age))
print("Current grade: " + str(mark))
if locker == "y":
    print("Has been assigned a locker: True")
if locker == "n":
    print("Has been assigned a locker: False")