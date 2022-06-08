def price_calculator(product, num):
    price = 0
    if product == 'coffee':
        price = num * 1.50
    elif product == 'water':
        price = num * 1
    elif product == 'coke':
        price = num * 1.40
    elif product == 'snacks':
        price = num * 2

    return f'{price:.2f}'


requested_product = input()
quantity = int(input())

print(price_calculator(requested_product, quantity))
