from math import ceil

fan_name = input()
budget = float(input())
num_of_bottles = int(input())
num_of_chips = int(input())

total_beer_sum = num_of_bottles * 1.20
price_for_one_bag_chips = total_beer_sum * 0.45
total_chips_sum = price_for_one_bag_chips * num_of_chips
total_sum = total_beer_sum + ceil(total_chips_sum)

diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")

else:
    print(f"{fan_name} needs {diff:.2f} more leva!")