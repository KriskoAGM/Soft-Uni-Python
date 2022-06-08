budget = int(input())
season = input()
number_of_fisher = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if number_of_fisher <= 6:
    price -= price * 0.10
elif 6 < number_of_fisher <= 11:
    price -= price * 0.15
elif number_of_fisher > 11:
    price -= price * 0.25

if number_of_fisher % 2 == 0 and season != 'Autumn':
    price -= price * 0.05

diff = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')

else:
    print(f'Not enough money! You need {diff:.2f} leva.')
