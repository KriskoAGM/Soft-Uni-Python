my_dict = {}

while True:

    command = input()

    if command == "stop":
        break

    quantity = int(input())

    if command not in my_dict:
        my_dict[command] = 0
    my_dict[command] += quantity

for key, value in my_dict.items():
    print(f"{key} -> {value}")
