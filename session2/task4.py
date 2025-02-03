# Task 4
# Write a function that return the next day of a given date.


# def next_day(day,month,year):


def next_day(day, month, year):
    # Days in each month (non-leap year)
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # Check for leap year (February has 29 days)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29  # Adjust February for leap year

    # Move to next day
    day += 1

    # If the new day exceeds the max days of the month, reset to 1 and increment month
    if day > days_in_month[month]:
        day = 1
        month += 1

        # If the new month exceeds 12, reset to 1 and increment year
        if month > 12:
            month = 1
            year += 1

    return f"{day}/{month}/{year}"  # Return the corrected date


# Example usage
print(next_day(10, 12, 2001))
print(next_day(30, 6, 2001))
print(next_day(31, 12, 2023))
print(next_day(28, 2, 2024))  # Expected output: 29/2/2024 (leap year case)


next_day(10, 12, 2001)
