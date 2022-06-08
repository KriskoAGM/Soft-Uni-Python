yearly_tax = int(input())

sneaker_price = yearly_tax - (40/100) * yearly_tax
suit_price = sneaker_price - (20/100) * sneaker_price
ball_price = suit_price / 4
acc_price = ball_price / 5

total_price = yearly_tax + sneaker_price + suit_price + ball_price + acc_price

print(total_price)