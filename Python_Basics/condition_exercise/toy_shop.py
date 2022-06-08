excursion_price = float(input())
puzzle = int(input())
doll = int(input())
bears = int(input())
minions = int(input())
truck = int(input())
discount = 0

price = (puzzle * 2.60) + (doll * 3) + (bears * 4.10) \
        + (minions * 8.20) + (truck * 2)
number_of_toys = puzzle + doll + bears + minions + truck

if number_of_toys >= 50:
    discount = price * 0.25

final_price = price - discount
loan = final_price * 0.10
profit = final_price - loan

if profit >= excursion_price:
    money_left = profit - excursion_price
    print(f'Yes! {money_left:.2f} lv left.')

elif profit <= excursion_price:
    not_enough = excursion_price - profit
    print(f'Not enough money! {not_enough:.2f} lv needed.')



