voucher_sum = int(input())
purchased_tickets = 0
purchased_products = 0

while True:
    text = input()
    price = 0
    if text == 'End':
        print(f'{purchased_tickets}')
        print(f'{purchased_products}')
        break

    if len(text) > 8:
        price = ord(text[0]) + ord(text[1])

        if price <= voucher_sum:
            voucher_sum -= price
            purchased_tickets += 1
            price = 0

    if len(text) <= 8:
        price = ord(text[0])

        if price <= voucher_sum:
            voucher_sum -= price
            purchased_products += 1
            price = 0

    if price > voucher_sum:
        print(f'{purchased_tickets}')
        print(f'{purchased_products}')
        break

