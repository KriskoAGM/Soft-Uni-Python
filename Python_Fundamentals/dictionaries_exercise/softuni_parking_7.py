info = {}
number_of_commands = int(input())

for _ in range(number_of_commands):

    commands = input().split()
    main_command = commands[0]
    name = commands[1]

    if name not in info and main_command == "register":
        license_plate = commands[2]
        info[name] = license_plate
        print(f"{name} registered {license_plate} successfully")

    elif name in info and main_command == "register":
        license_plate = commands[2]
        print(f"ERROR: already registered with plate number {license_plate}")

    elif main_command == "unregister" and name not in info:
        print(f"ERROR: user {name} not found")

    else:
        print(f"{name} unregistered successfully")
        info.pop(name)

for key, value in info.items():
    print(f"{key} => {value}")


