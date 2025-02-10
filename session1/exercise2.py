import random


def check_random_even_or_odd():
    a = random.randint(1, 100)
    if a % 2 == 0:
        result = f"{a} is even"

    else:
        result = f"{a} is odd"

    with open("random_number_info.txt", "w") as file:
        file.write(result)

    print(result)


check_random_even_or_odd()
