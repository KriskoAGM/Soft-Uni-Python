num = 5

for rows in range(num):
    for columns in range(rows, num):
        print(' ', end=' ')
    for columns in range(rows):
        print('*', end=' ')
    for columns in range(rows + 1):
        print('*', end=' ')
    print()
