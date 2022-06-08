pens = int(input())
markers = int(input())
prep_litres = int(input())
discount = int(input())

pen_price = 5.80
marker_price = 7.20
prep_litres_price = 1.20

pen_final_price = pens * pen_price
marker_final_price = markers * marker_price
prep_final_price = prep_litres * prep_litres_price
discount_price = (discount / 100)

total_price = pen_final_price + marker_final_price + prep_final_price
final_price = total_price - (total_price * discount_price)

print(final_price)