#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: OPS445NCC
Author: ksingh631
The python code in this file (a1_ksingh631.py) is original work written by Kushagra Singh. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys
from datetime import datetime

def after(date: str) -> str:
    """Returns the date of the next day."""
    # Split the input date string into year, month, and day
    year, month, day = map(int, date.split('-'))
    # Number of days in each month, considering leap years for February
    month_days = [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day += 1  # Move to the next day
    if day > month_days[month - 1]:  # If day exceeds the days in the month
        day = 1
        month += 1  # Move to the next month
        if month > 12:  # If month exceeds December, move to the next year
            month = 1
            year += 1
    # Return the next date in YYYY-MM-DD format
    return f"{year:04d}-{month:02d}-{day:02d}"

def leap_year(year: int) -> bool:
    """Returns 1 if the year is a leap year, otherwise 0."""
    # A leap year is divisible by 4, but not every century year is a leap year unless divisible by 400
    return 1 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 0

def mon_max(month: int, year: int) -> int:
    """Returns the number of days in a given month."""
    # Days in each month, adjusting for leap years in February
    month_days = [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]

def day_of_week(year: int, month: int, day: int) -> str:
    """Based on the algorithm by Tomohiko Sakamoto."""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    # Month offset values to calculate the day of the week
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    
    if month < 3:  # Adjust for January and February
        year -= 1
    # Calculate the day of the week number
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + day) % 7
    return days[num]  # Return the day of the week

def day_count(start_date: str, end_date: str) -> int:
    """Count the number of weekend days between start_date and end_date."""
    start_year, start_month, start_day = map(int, start_date.split('-'))
    end_year, end_month, end_day = map(int, end_date.split('-'))

    weekend_days = 0
    current_date = start_date
    # Loop through each day until the end date
    while current_date != after(end_date):
        year, month, day = map(int, current_date.split('-'))
        if day_of_week(year, month, day) in ['sat', 'sun']:  # Check for Saturday or Sunday
            weekend_days += 1
        current_date = after(current_date)  # Move to the next day
    return weekend_days

def valid_date(date: str) -> bool:
    """Checks if the given date in YYYY-MM-DD format is valid."""
    try:
        # Attempt to create a datetime object from the date string
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        # If a ValueError occurs, the date is not valid
        return False

def usage() -> None:
    """Print the usage message."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def main():
    """Main function to process arguments and print weekend days."""
    if len(sys.argv) != 3:
        usage()  # Incorrect number of arguments

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    if not (valid_date(start_date) and valid_date(end_date)):
        usage()  # Invalid date format

    if start_date > end_date:
        start_date, end_date = end_date, start_date  # Ensure start_date is earlier

    # Print the result
    print(f"The period between {start_date} and {end_date} includes {day_count(start_date, end_date)} weekend days.")

if __name__ == "__main__":
    main()
