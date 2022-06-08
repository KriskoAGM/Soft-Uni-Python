flower_type = input()
flower_quantity = int(input())
budget = int(input())
price = 0

if flower_type == 'Roses':
    price = flower_quantity * 5
    if flower_quantity > 80:
        price -= price * 0.10

elif flower_type == 'Dahlias':
    price = flower_quantity * 3.80
    if flower_quantity > 90:
        price -= price * 0.15

elif flower_type == 'Tulips':
    price = flower_quantity * 2.80
    if flower_quantity > 80:
        price -= price * 0.15

elif flower_type == 'Narcissus':
    price = flower_quantity * 3
    if flower_quantity < 120:
        price += price * 0.15

elif flower_type == 'Gladiolus':
    price = flower_quantity * 2.50
    if flower_quantity < 80:
        price += price * 0.20

diff = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {flower_quantity} {flower_type} and {diff:.2f} leva left.')

else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
