projection = input()
rows = int(input())
columns = int(input())
profit = 0
projection_type = ['Premiere', 'Normal', 'Discount']


def multiply(a, b):
    result = a * b
    return result


capacity = multiply(rows, columns)

if projection == projection_type[0]:
    profit = multiply(capacity, 12)

elif projection == projection_type[1]:
    profit = multiply(capacity, 7.50)

elif projection == projection_type[2]:
    profit = multiply(capacity, 5)

print(f'{profit:.2f} leva')
