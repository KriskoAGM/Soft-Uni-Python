floors = int(input())
rows = int(input())

row_number = 0
row_name = ''

for floor in range(floors, 0, -1):
    for i in range(rows):
        row_number = floor * 10 + i

        if floor == floors:
            row_name = f'L{row_number} '

        elif floor % 2 != 0:
            row_name = f'A{row_number} '

        elif floor % 2 == 0:
            row_name = f'O{row_number} '

        print(row_name, end='')
    print()
