number_of_strings = int(input())
word = input()
list = []

for i in range(number_of_strings):
    strings = input()
    list.append(strings)

print(list)
for i in range(len(list) - 1, -1, -1):
    element = list[i]
    if word not in element:
        list.remove(element)
print(list)