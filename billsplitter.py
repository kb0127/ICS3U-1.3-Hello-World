print("Restaurant Bill Splitter")
amount_people = int(input("How many people in your group?: "))
bill = float(input("What was the total bill after tax?: "))
tip = float(input("How much do you want to tip in percent (ex. 0.15 for 15%)?:  "))

total_bill = (bill * 1.15)
total_tip = (total_bill * tip)

customer_pay = float((bill + total_tip)/amount_people)

print("Each person should pay " + str(customer_pay))