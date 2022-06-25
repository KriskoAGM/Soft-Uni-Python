array = list(map(int, input().split()))

while True:
    command = input()

    if command == 'end':
        break

    elif command == 'decrease':
        array = [x - 1 for x in array]
        continue

    commands = command.split()
    action = commands[0]
    index1 = int(commands[1])
    index2 = int(commands[2])

    if action == 'swap':
        array[index1], array[index2] = array[index2], array[index1]

    elif action == 'multiply':
        array[index1] = array[index1] * array[index2]

print(*array, sep=", ")
