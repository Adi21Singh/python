# number = 3

# factorial = 1

# if number < 0:
#     print("we do not calcaulate negative factorial")
# elif number == 1:
#     print("The result is 1")
# else:
#     for i in range(1, number + 1):
#         print(i)
#         factorial = factorial * i
#         i-1
#     print("The result is ",factorial)

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(n,0,-1):
            result *= i
            print(i)
        return result

# Test the function
print(factorial(4))