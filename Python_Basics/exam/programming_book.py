price_for_one_page = float(input())
price_for_one_cover = float(input())
discount = int(input())
payment_sum = float(input())
total_sum_percent = int(input())

start_price = price_for_one_page * 899 + price_for_one_cover * 2
discounted_price = start_price - (discount / 100) * start_price
price_for_designer = discounted_price + payment_sum
final_price = price_for_designer - (total_sum_percent / 100) * price_for_designer
print(f'Avtonom should pay {final_price:.2f} BGN.')