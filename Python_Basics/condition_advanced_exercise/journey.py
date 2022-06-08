budget = float(input())
season = input()
costs = 0
destination = ''
vacation_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_type = 'Camp'
        costs = budget * 0.30
    elif season == 'winter':
        vacation_type = 'Hotel'
        costs= budget * 0.70

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation_type = 'Camp'
        costs = budget * 0.40
    elif season == 'winter':
        vacation_type = 'Hotel'
        costs = budget * 0.80

elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        vacation_type = 'Hotel'
        costs = budget * 0.90
    elif season == 'winter':
        vacation_type = 'Hotel'
        costs = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{vacation_type} - {costs:.2f}')


