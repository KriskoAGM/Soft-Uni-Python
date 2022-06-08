month = input()
days_overnight = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = days_overnight * 50
    apartment_price = days_overnight * 65
    if 7 < days_overnight < 14:
        studio_price -= studio_price * 0.05
    elif days_overnight > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10


elif month == 'June' or month == 'September':
    studio_price = days_overnight * 75.20
    apartment_price = days_overnight * 68.70
    if days_overnight > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10

elif month == 'July' or month == 'August':
    studio_price = days_overnight * 76
    apartment_price = days_overnight * 77
    if days_overnight > 14:
        apartment_price -= apartment_price * 0.10

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')