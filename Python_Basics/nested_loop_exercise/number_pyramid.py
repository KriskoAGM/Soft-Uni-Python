number = int(input())
current = 1
condition = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current > number:
            condition = True
            break
        print(str(current) + ' ', end='')
        current += 1

    if condition:
        break

    print()