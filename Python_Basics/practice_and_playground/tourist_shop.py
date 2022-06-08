budget = float(input())
budget_left = budget
purchased = 0
costs = 0

while True:
    name_of_product = input()

    if name_of_product == 'Stop':
        print(f"You bought {purchased} products for {costs:.2f} leva.")
        break

    price_of_product = float(input())

    if budget_left >= price_of_product or budget_left < price_of_product:
        purchased += 1

        if purchased % 3 == 0:
            discount = price_of_product / 2
            budget_left -= discount
            costs += discount
            continue

        budget_left -= price_of_product
        costs += price_of_product

    if budget_left < 0:
        diff = abs(budget_left)
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
