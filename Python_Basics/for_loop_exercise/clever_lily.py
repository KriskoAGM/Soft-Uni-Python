from math import floor

age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

number_of_toys = 0
saved_money = 0

for i in range(1, age + 1):

    if i % 2 == 0:
        saved_money += 10 * (i / 2)
    else:
        number_of_toys += 1

money_taken = floor(age / 2)
available_money = (number_of_toys * price_per_toy) + (saved_money - money_taken)
diff = abs(available_money - washing_machine_price)

if available_money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')

