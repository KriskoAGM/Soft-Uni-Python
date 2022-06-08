import sys

n = int(input())
max_sum = -sys.maxsize
current_sum = 0

for i in range(n):
    current_number = int(input())

    if current_number > max_sum:
        max_sum = current_number

    current_sum += current_number

if (current_sum - max_sum) == max_sum:
    print('Yes')
    print(f'Sum = {max_sum} ')
else:
    diff = abs((current_sum - max_sum) - max_sum)
    print('No')
    print(f'Diff = {diff}')