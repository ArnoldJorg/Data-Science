import string

with open("./data/bad_rabbit.txt", "r") as bad_rabbit:
    content = bad_rabbit.read()

result = content.replace("very", "the")

print(result)
