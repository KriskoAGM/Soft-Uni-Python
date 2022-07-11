products = input().split()
my_dict = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    my_dict[key] = int(value)

searched_products = input().split()

for product in searched_products:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


