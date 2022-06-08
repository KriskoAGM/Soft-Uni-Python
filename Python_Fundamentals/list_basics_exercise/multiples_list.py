factor = int(input())
count = int(input())
new_list = []
number = factor

for i in range(count):
    new_list.append(number)
    number += factor
print(new_list)


