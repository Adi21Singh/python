number = int(input("Enter the number to check if prime or not"))

if number > 1:
    for i in range(2,number):
        if (number % i == 0):
            print(number, ",This is not a prime number")
            print(i, "times", number//i, "is", number)
            break
    else:
        print("%d The number is prime" %number)    