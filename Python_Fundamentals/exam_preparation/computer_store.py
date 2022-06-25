expenses = 0
taxes = 0

while True:
    total_price = expenses + taxes
    command = input()

    if command == 'special':
        if total_price > 0:
            total_price = total_price - (total_price * 0.10)
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {expenses:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print('-----------')
            print(f"Total price: {total_price:.2f}$")
            break
        else:
            print("Invalid order!")
            break
    elif command == 'regular':
        if total_price > 0:
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {expenses:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print('-----------')
            print(f"Total price: {total_price:.2f}$")
            break
        else:
            print("Invalid order!")
            break

    price = float(command)

    if price <= 0:
        print('Invalid price!')
        continue
    expenses += price
    taxes = expenses * 0.20
