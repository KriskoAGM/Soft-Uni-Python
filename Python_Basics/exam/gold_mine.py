num_of_location = int(input())


for i in range(num_of_location):
    expected_income_of_gold = float(input())
    days = int(input())
    gold_sum = 0

    for j in range(days):
        collected_gold = float(input())
        gold_sum += collected_gold

    average_gold = gold_sum / days

    if average_gold >= expected_income_of_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")

    else:
        print(f"You need {abs(average_gold - expected_income_of_gold):.2f} gold.")
