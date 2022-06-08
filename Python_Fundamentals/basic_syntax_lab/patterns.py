num = int(input())

for rows in range(1, num + 1):
    for columns in range(0, rows):
        print('*', end= '')
    print()

for rows in range(num - 1, 0, -1):
    for columns in range(0, rows):
        print('*', end='')
    print()