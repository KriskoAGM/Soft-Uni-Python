from math import pi

figure = input()
result = 0

if figure == 'square':
    a = float(input())
    result = a ** 2
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    result = a * b
elif figure == 'circle':
    r = float(input())
    result = pi * r ** 2
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    result = (a * b) / 2

print(f"{result:.3f}")



