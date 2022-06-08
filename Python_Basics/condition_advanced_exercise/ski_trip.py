stay_day = int(input())
room_type = input()
rating = input()
price = 0
number_of_nights = stay_day - 1

if room_type == 'room for one person':
    price = number_of_nights * 18

elif room_type == 'apartment':
    price = number_of_nights * 25
    if stay_day < 10:
        price -= price * 0.30
    elif 10 < stay_day <= 15:
        price -= price * 0.35
    elif stay_day > 15:
        price -= price * 0.50


elif room_type == 'president apartment':
    price = number_of_nights * 35
    if stay_day < 10:
        price -= price * 0.10
    elif 10 < stay_day <= 15:
        price -= price * 0.15
    elif stay_day > 15:
        price -= price * 0.20

if rating == 'positive':
    price += price * 0.25
elif rating == 'negative':
    price -= price * 0.10

print(f'{price:.2f}')

