my_dict = {}
words = "".join(s for s in input().split())

for word in words:
    my_dict[word] = words.count(word)

for key, value in my_dict.items():
    print(f"{key} -> {value}")
