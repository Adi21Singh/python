lower_range = int(input("enter the lower range : "))
upper_range = int(input("enter the upper range : "))

#number = 55

for number in range(lower_range, upper_range + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i == 0):
                break
        else:
            print(number, ';')