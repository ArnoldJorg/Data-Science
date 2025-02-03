# Task 3
# Write a program that determines the largest numerical value in a list. You may use the example lists given or create your own.

# Extension : Turn this into a function that takes the list as an argument and returns the largest value.


# list1 = [3,45,6,19,100]
# list2 = [12,4,120,5,11,15,42]


list2 = [12, 4, 120, 5, 11, 15, 42]
list1 = [3, 45, 6, 19, 100]


def my_function(r):
    x = max(r)
    return x


print(my_function(list1))
print(my_function(list2))
