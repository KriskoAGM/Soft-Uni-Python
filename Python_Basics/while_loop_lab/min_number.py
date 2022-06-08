num = 10000000000000

while True:
    n = input()

    if n == 'Stop':
        break

    if int(n) < int(num):
        num = n

print(num)