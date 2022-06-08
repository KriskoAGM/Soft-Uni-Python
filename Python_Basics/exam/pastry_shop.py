sweet = input()
num_of_requested_sweets = int(input())
day_of_month = int(input())
price = 0
discounted_price = 0

if sweet == 'Cake':
    if day_of_month <= 15:
        price = num_of_requested_sweets * 24
    elif day_of_month > 15:
        price = num_of_requested_sweets * 28.70

elif sweet == 'Souffle':
    if day_of_month <= 15:
        price = num_of_requested_sweets * 6.66
    elif day_of_month > 15:
        price = num_of_requested_sweets * 9.80

elif sweet == 'Baklava':
    if day_of_month <= 15:
        price = num_of_requested_sweets * 12.60
    elif day_of_month > 15:
        price = num_of_requested_sweets * 16.98

if 100 <= price <= 200 and day_of_month <= 22:
    price -= price * 0.15

if price > 200 and day_of_month <= 22:
    price -= price * 0.25

if day_of_month <= 15:
    discounted_price = price * 0.10

final_price = price - discounted_price
print(f'{final_price:.2f}')



