budget = float(input())
num_of_series = int(input())
costs = 0

for i in range(num_of_series):
    name = input()
    price = float(input())

    if name == 'Thrones':
        price -= price * 0.5
        costs += price

    elif name == 'Lucifer':
        price -= price * 0.4
        costs += price

    elif name == 'Protector':
        price -= price * 0.3
        costs += price

    elif name == 'TotalDrama':
        price -= price * 0.2
        costs += price

    elif name == 'Area':
        price -= price * 0.1
        costs += price

    else:
        costs += price

diff = abs(budget - costs)

if budget >= costs:
    print(f"You bought all the series and left with {diff:.2f} lv.")

else:
    print(f"You need {diff:.2f} lv. more to buy the series!")