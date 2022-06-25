targets = list(map(int, input().split()))

while True:
    command = input()

    if command == 'End':
        print(*targets, sep="|")
        break

    commands = command.split()
    action = commands[0]
    index = int(commands[1])
    value = int(commands[2])

    if action == 'Shoot':
        if 0 <= index < len(targets):
            if targets[index] - value <= 0:
                targets.pop(index)
            else:
                targets[index] -= value

    elif action == "Add":
        if index < 0 or index >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(index, value)

    elif action == "Strike":
        if index - value >= 0 and index + value < len(targets):
            start_index = index - value
            final_index = index + value
            targets = [targets[x] for x in range(len(targets)) if x < start_index or x > final_index]
        else:
            print("Strike missed!")
