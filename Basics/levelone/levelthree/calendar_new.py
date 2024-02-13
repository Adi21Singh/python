import calendar

# Define your date
year = 1776
month = 7
day = 4

# Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_of_week = calendar.weekday(year, month, day)

# Define a list of day names
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Print the day of the week
print("The day of the week for {}-{}-{} is {}".format(year, month, day, days[day_of_week]))