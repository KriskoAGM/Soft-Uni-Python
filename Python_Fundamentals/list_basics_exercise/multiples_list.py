factor = int(input())
count = int(input())
new_list = []
number = factor

for i in range(count):
    new_list.append(number)
    number += factor
print(new_list)


# Second solution
# factor = int(input())
# count = int(input())
# new_list = [x*factor for x in range(1, count + 1)]
# print(new_list)

