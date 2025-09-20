from datetime import date
name = input("Enter your name:")
age = input("Enter your age:")

today = int(date.today().year)
yr_100 = None

def year_when_100(age: int, today: int) -> int:
    """Returns the year in which somebody will turn 100 based on their age today."""
    year = today + (100-age)
    return year

try:
    age = int(age)
except:
    print("Please enter age as a whole number")

else:
    if age <  0:
        print("Age must be greater than or equal to zero years old")

    else:
        if age >= 120: 
            print("Age must be less than 120 years old")
        else:
            yr_100 = year_when_100(age, today)
if 'yr_100' in locals():
    print(f"Hello {name}, you will turn 100 in the year {yr_100}!")