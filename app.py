#code for calculator
print("Select one of the following commands:-")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division ")

operation = input()

if operation == "1":
   num1 = input("Enter 1st number ")
   num2 = input("Enter 2nd number ")
   print("The answer is " + str(int(num1) + int(num2)))

elif operation == "2" :
   num1 = input("Enter 1st number")
   num2: str = input("Enter 2nd number")
   print("The answer is " + str(int(num1) - int(num2)))

elif operation == "3" :
   num1 = input("Enter 1st number")
   num2 = input("Enter 2nd number")
   print("The answer is " + str(int(num1) * int(num2)))

elif operation == "4":
   num1 = input("Enter 1st number")
   num2 = input("Enter 2nd number")
   print("The answer is " + str(int(num1) / int(num2)) )

else:
    print("Invalid Entry")





