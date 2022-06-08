num = int(input())
div2_counter = 0
div3_counter = 0
div4_counter = 0

for n in range(num):
    nums = int(input())

    if nums % 2 == 0:
        div2_counter += 1

    if nums % 3 == 0:
        div3_counter += 1

    if nums % 4 == 0:
        div4_counter += 1

p1 = div2_counter * 100 / num
p2 = div3_counter * 100 / num
p3 = div4_counter * 100 / num

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')

