# Leap Year Check
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# Taking input from user
year = int(input("Enter a year: "))
check_leap_year(year)