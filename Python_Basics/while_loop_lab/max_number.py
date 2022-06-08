max_num = -10000000000000

while True:
    n = input()

    if n == 'Stop':
        break

    if int(n) > int(max_num):
        max_num = n

print(max_num)
