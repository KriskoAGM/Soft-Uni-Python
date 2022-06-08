num_of_cats = int(input())
gram_sum = 0
group1 = 0
group2 = 0
group3 = 0

for i in range(num_of_cats):
    food_grams = float(input())
    gram_sum += food_grams

    if 100 <= food_grams < 200:
        group1 += 1

    if 200 <= food_grams < 300:
        group2 += 1

    if 300 <= food_grams < 400:
        group3 += 1

total_food = gram_sum / 1000
price = total_food * 12.45

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {price:.2f} lv.")