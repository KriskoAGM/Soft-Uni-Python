users = {}

while True:
    command = input()

    if command == "End":
        break

    company, id = command.split(" -> ")

    if company not in users:
        users[company] = []
        if id not in users[company]:
            users[company].append(id)
    else:
        if id in users[company]:
            continue
        users[company].append(id)

for key, value in users.items():
    print(key)
    for employee in value:
        print(f"-- {employee}")

