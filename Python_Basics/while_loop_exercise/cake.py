width = int(input())
length = int(input())

num_of_pieces = width * length
pieces_left = 0

while True:
    num = input()

    if num == "STOP":
        break

    num_of_pieces -= int(num)

    pieces_left = abs(num_of_pieces)

    if num_of_pieces < 0:
        print(f'No more cake left! You need {pieces_left} pieces more.')
        break

if num_of_pieces > 0:
    print(f'{pieces_left} pieces are left.')


