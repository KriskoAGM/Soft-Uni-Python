num_of_orders = int(input())
total = 0

for i in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        sum = price_per_capsule * days * capsules_per_day
        print(f'The price for the coffee is: ${sum:.2f}')
        total += sum

print(f"Total: ${total:.2f}")

