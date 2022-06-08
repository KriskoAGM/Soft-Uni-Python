a = input()
b = input()
c = input()

win = 0
defeat = 0
draw = 0

if a[0] > a[2] or b[0] > b[2] or c[0] > c[2]:
    win += 1
    if a[0] < a[2] or b[0] < b[2] or c[0] < [2]:
        defeat += 1

if a[0] == a[2]:
    draw += 1
    if a[0] == a[2]:
        draw += 1
        if a[0] == a[2]:
            draw += 1

print(f'Team won {win} games.')
print(f'Team lost {defeat} games.')
print(f'Drawn games: {draw}')




