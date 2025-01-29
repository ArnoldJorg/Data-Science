import string

with open("./data/bad_rabbit.txt", "r") as bad_rabbit:
    content = bad_rabbit.read()

translator = str.maketrans("", "", string.punctuation)
clean_text = content.translate(translator)

text_array = clean_text.split()

word_counts = {}
for word in text_array:
    word_counts[word] = word_counts.get(word, 0) + 1  # Efficient counting

counted_array = [{"word": word, "count": count} for word, count in word_counts.items()]

sorted_array = sorted(counted_array, key=lambda x: x["count"], reverse=True)

print(sorted_array[:10])
