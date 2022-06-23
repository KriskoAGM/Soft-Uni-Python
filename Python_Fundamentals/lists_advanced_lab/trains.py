# number_of_wagons = int(input())
# new_list = [0] * number_of_wagons
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     data = command.split()
#     action = data[0]
#     people = int(data[1])
#
#     if action == 'add':
#         new_list[-1] += people
#     elif action == 'insert':
#         index = int(data[1])
#         new_list[index] += int(data[2])
#     elif action == 'leave':
#         index = int(data[1])
#         new_list[index] -= int(data[2])
# print(new_list)


wagons = int(input())
train = [0] * wagons

while True:
    command = input()

    if command == 'End':
        break

    data = command.split()
    command_1 = data[0]

    if command_1 == 'add':
        people = int(data[1])
        train[-1] += people
    elif command_1 == 'insert':
        index = int(data[1])
        people = int(data[2])
        train[index] += people
    elif command_1 == 'leave':
        index = int(data[1])
        people = int(data[2])
        train[index] -= people

print(train)























