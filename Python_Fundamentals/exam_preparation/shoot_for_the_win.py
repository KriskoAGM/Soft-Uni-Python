targets = list(map(int, input().split()))

while True:
    command = input()

    if command == 'End':
        break

    index = int(command)
    if 0 > index or index >= len(targets):
        continue

    power = targets[index]
    targets[index] = -1
    for index1, num in enumerate(targets):
        if targets[index1] < 0:
            continue

        if num > power:
            num -= power
            targets[index1] = num

        elif num <= power:
            num += power
            targets[index1] = num

count_of_shots = targets.count(-1)
shot_targets = " ".join(str(x) for x in targets)
print(f"Shot targets: {count_of_shots} -> {shot_targets}")



