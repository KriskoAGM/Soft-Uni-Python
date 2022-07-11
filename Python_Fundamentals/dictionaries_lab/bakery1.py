food = input().split()
bakery = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = food[index + 1]
    bakery[key] = int(value)

print(bakery)

