degrees = int(input())
time_of_day = input()
day = ['Morning', 'Afternoon', 'Evening']
ups = ['Sweatshirt', 'Shirt', 'T-Shirt', 'Swim Suit']
down = ['Sneakers', 'Moccasins', 'Sandals', 'Barefoot']
outfit = ''
shoes = ''

if time_of_day == day[0]:
    if 10 <= degrees <= 18:
        outfit = ups[0]
        shoes = down[0]
    elif 18 < degrees <= 24:
        outfit = ups[1]
        shoes = down[1]
    else:
        outfit = ups[2]
        shoes = down[2]

elif time_of_day == day[1]:
    if 10 <= degrees <= 18:
        outfit = ups[1]
        shoes = down[1]
    elif 18 < degrees <= 24:
        outfit = ups[2]
        shoes = down[2]
    else:
        outfit = ups[3]
        shoes = down[3]

elif time_of_day == day[2]:
    if 10 <= degrees <= 18:
        outfit = ups[1]
        shoes = down[1]
    elif 18 < degrees <= 24:
        outfit = ups[1]
        shoes = down[1]
    else:
        outfit = ups[1]
        shoes = down[1]

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")