# Task 1
# Write a program that determines whether a value is:

# A multiple of 7
# A multiple of 5
# A multiple of both 7 and 5
# None of the above
# Print out an appropriate response for each option.

import random


def check_random_even_or_odd():
    a = random.randint(1, 100)

    if a % 7 == 0 & a % 5 != 0:
        result = f"{a} is multiple of 7"

    if a % 5 == 0 & a % 7 != 0:
        result = f"{a} is a multiple of 5"

    if a % 5 == 0 & a % 7 == 0:
        result = f"{a} is a multiple of both 7 and 5 "

    else:
        result = f"{a} is neither a multiple of 7 or 5 "
    with open("multiple_of_7_and_5.txt", "w") as file:
        file.write(result)

    print(result)


check_random_even_or_odd()
