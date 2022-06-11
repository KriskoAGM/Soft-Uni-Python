names_of_gifts = input().split(" ")
gift = ''

while True:
    command = input()
    if command == 'No Money':
        break
    if 'OutOfStock' in command:
        command_1 = command.split(" ")
        gift = command_1[1]
        while gift in names_of_gifts:
            index = names_of_gifts.index(gift)
            names_of_gifts[index] = 'None'

    elif 'Required' in command:
        command_1 = command.split(" ")
        gift = command_1[1]
        if len(names_of_gifts) - 1 >= int(command_1[2]) > 0:
            index = int(command_1[2])
            names_of_gifts[index] = gift

    elif 'JustInCase' in command:
        command_1 = command.split(" ")
        gift = command_1[1]
        names_of_gifts[-1] = gift
while 'None' in names_of_gifts:
    names_of_gifts.remove('None')
print(" ".join(names_of_gifts))
