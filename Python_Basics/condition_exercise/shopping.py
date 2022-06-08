budget = float(input())
video_cards = int(input())
cpu = int(input())
ram = int(input())

video_card_sum = video_cards * 250
cpu_price = video_card_sum * 0.35
cpu_sum = cpu * cpu_price
ram_price = video_card_sum * 0.10
ram_sum = ram * ram_price
total_cost = video_card_sum + cpu_sum + ram_sum

if video_cards > cpu:
    total_cost -= total_cost * 0.15

diff = abs(budget - total_cost)
if budget >= total_cost:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
