actor_budget = float(input())
budget_left = actor_budget
payment = 0

while True:
    actor_name = input()

    if actor_name == 'ACTION':
        print(f"We are left with {budget_left:.2f} leva.")
        break

    if len(actor_name) <= 15:
        payment = float(input())

        if budget_left < payment:
            print(f"We need {abs(budget_left - payment):.2f} leva for our actors.")
            break

        budget_left -= payment

    else:
        budget_left -= budget_left * 0.2








