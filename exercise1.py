my_name = "Arnold"
city = "London"
hobbies = ["football", "gym", "walks", "going to coffee shops"]

hobby_text = (
    ",".join(hobbies[:-1]) + f" and {hobbies[-1]}" if len(hobbies) > 1 else hobbies[0]
)

my_text = f"My name is {my_name} and I live in {city}. My hobbies are {hobby_text}."

with open("my_info.txt", "w") as file:
    file.write(my_text)

print("File 'my_info.txt' created successfully!")
