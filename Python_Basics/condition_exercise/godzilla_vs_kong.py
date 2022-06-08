budget = float(input())
statist = int(input())
statist_clothes = float(input())

decor_sum = budget * 0.10
clothes_sum = statist * statist_clothes

if statist > 150:
    clothes_sum -= clothes_sum * 0.10

total_sum = decor_sum + clothes_sum
money_left = budget - total_sum
money_needed = total_sum - budget

if total_sum > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more. ')

elif total_sum <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')



