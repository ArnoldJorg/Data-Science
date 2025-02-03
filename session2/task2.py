# Task 2
# Using at least one loop, write a program that will print the following pattern:

# £
# ££
# £££
# ££££
# £££££
# ££££
# £££
# ££
# £

i = 0
while i < 5:
    i += 1  # Equivalent to i++
    print("£" * i)

j = 5
while j > 0:

    j -= 1  # Equivalent to i++
    print("£" * j)
