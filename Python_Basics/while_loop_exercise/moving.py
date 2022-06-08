width = int(input())
length = int(input())
height = int(input())

available_space = width * length * height
space_occupied = 0

while True:
    num = input()

    if num == 'Done':
        break

    space_occupied += int(num)

    if space_occupied > available_space:
        break

diff = abs(available_space - space_occupied)

if space_occupied > available_space:
    print(f'No more free space! You need {diff} Cubic meters more.')

else:
    print(f'{diff} Cubic meters left.')