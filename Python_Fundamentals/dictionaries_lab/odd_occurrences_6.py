elements = input().lower().split()
my_dict = {}

# my_dict = {word: elements.count(word) for word in elements} - dict comprehension

for word in elements:
    my_dict[word] = elements.count(word)

for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")