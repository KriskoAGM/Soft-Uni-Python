nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint * 1.10) * 14.50
thinner_price = thinner * 5
bag_price = 0.40

total_price = nylon_price + paint_price + thinner_price + bag_price
worker_price = (total_price * 0.30) * hours

final_price = total_price + worker_price

print(final_price)

