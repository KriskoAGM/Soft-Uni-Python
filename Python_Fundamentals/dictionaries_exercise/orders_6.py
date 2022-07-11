def get_product_prices(dict):
    for key in dict:
        dict[key] = dict[key][0] * dict[key][1]


my_dict = {}

while True:
    command = input()

    if command == "buy":
        break

    product, price, quantity = command.split()

    if product not in my_dict:
        my_dict[product] = [float(price), int(quantity)]
    elif product in my_dict:
        my_dict[product][0] = float(price)
        my_dict[product][1] += int(quantity)

get_product_prices(my_dict)

for key, value in my_dict.items():
    print(f"{key} -> {value:.2f}")


