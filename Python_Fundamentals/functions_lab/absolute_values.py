numbers = input().split(" ")
new_list = []
for num in numbers:
    new_list.append(float(num))

result = list(map(abs, new_list))
print(result)

