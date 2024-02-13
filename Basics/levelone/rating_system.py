rating_feedback = int(input("Please procide the product rating between 1 and 5 : "))

if rating_feedback == 1:
    print("Sorry to hear aout your experience")
elif rating_feedback == 2:
    print("We are trying to get better")
elif rating_feedback == 3:
    print("Thanks getting better")
elif rating_feedback == 4:
    print("We almost missed the perfect rating")
elif rating_feedback == 5:
    print("Happy to know")
else:
    print("Sorry, please select the correct value")