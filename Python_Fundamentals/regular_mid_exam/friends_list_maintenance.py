friends = input().split(", ")
blacklisted = 0
lost = 0
while True:

    command = input()

    if command == "Report":
        print(f"Blacklisted names: {blacklisted}")
        print(f"Lost names: {lost}")
        print(*friends)
        break

    commands = command.split()

    if commands[0] == "Blacklist":
        name = commands[1]
        if name not in friends:
            print(f"{name} was not found.")
        else:
            print(f"{name} was blacklisted.")
            blacklisted += 1
        for index, names in enumerate(friends):
            if names == name:
                friends[index] = "Blacklisted"

    elif commands[0] == "Error":
        index1 = int(commands[1])
        if 0 <= index1 < len(friends) and friends[index1] != "Blacklisted" and friends[index1] != "Lost":
            print(f"{friends[index1]} was lost due to an error.")
            friends[index1] = "Lost"
            lost += 1
        else:
            continue

    elif commands[0] == "Change":
        index2 = int(commands[1])
        new_name = commands[2]
        if 0 <= index2 < len(friends):
            print(f"{friends[index2]} changed his username to {new_name}.")
            friends[index2] = new_name
        else:
            continue








