chicken = int(input())
fish = int(input())
vegetarian = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.40
vegetarian_price = vegetarian * 8.15

total_price = chicken_price + fish_price + vegetarian_price
desert_price = (total_price * 0.20) + total_price
final_price = desert_price + 2.50

print(final_price)