phones = input().split(", ")

while True:

    command = input()

    if command == 'End':
        print(*phones, sep=", ")
        break

    commands = command.split(" - ")
    action = commands[0]

    if action == "Add":
        phone = commands[1]
        if phone in phones:
            continue
        else:
            phones.append(phone)

    elif action == 'Remove':
        phone1 = commands[1]
        if phone1 in phones:
            phones.remove(phone1)
        else:
            continue

    elif action == 'Bonus phone':
        bonus = commands[1].split(":")
        old_phone = bonus[0]
        new_phone = bonus[1]
        if old_phone in phones:
            index1 = phones.index(old_phone)
            phones.insert(index1 + 1, new_phone)
        else:
            continue

    elif action == 'Last':
        phone3 = commands[1]
        if phone3 in phones:
            index = phones.index(phone3)
            phones.pop(index)
            phones.append(phone3)
        else:
            continue
