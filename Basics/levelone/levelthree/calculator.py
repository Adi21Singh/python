import maths

num1 = int(input("Enter the value for number 1 : "))
num2 = int(input("Enter the value for number 2 : "))
optionsVal = int(input("Enter the value from 1 to 3 : "))

if (optionsVal == 1):
    sum = maths.add(num1, num2)
    print("You have selected the first option : ", sum)
elif (optionsVal == 2):
    minus = maths.sub(num1, num2)
    print("You have selected the second value ", minus)
elif (optionsVal == 3):
    multiplication = maths.multiply(num1, num2)
    print("Multiplication for 3 option is : ", multiplication)
    
else:
    print("You have selected the options")