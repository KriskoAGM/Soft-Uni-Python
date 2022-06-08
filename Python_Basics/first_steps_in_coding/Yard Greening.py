meters_per_square = float(input())
price = meters_per_square * 7.61
discount = 0.18 * price
final_price = price - discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
