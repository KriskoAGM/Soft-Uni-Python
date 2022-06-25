elements = input().split()
moves = 0
empty_list = []
while True:
    command = input()

    if command == 'end':
        break

    moves += 1

    index = list(map(int, command.split()))
    first_index = index[0]
    second_index = index[1]

    if first_index == second_index or 0 > first_index or first_index >= len(elements) or 0 > second_index or \
            second_index >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        list_half = len(elements) // 2
        elements.insert(list_half, "-" + str(moves) + "a")
        elements.insert(list_half + 1, "-" + str(moves) + "a")

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        empty_list.append(elements[first_index])
        empty_list.append(elements[second_index])
        elements = [num for num in elements if num not in empty_list]
        empty_list.clear()
    else:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
if len(elements) > 0:
    print("Sorry you lose :(")
    print(*elements)
