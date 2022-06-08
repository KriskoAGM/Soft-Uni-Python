fruit = input()
day = input()
quantity = float(input())
price = 0
condition = True


if day in "'Monday' 'Tuesday' 'Wednesday' 'Thursday' 'Friday'":
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    else:
        print('error')
        condition = False


elif day in "'Saturday' 'Sunday'":
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    else:
        print('error')
        condition = False

else:
    print('error')
    condition = False

if condition:
    final_price = quantity * price
    print(f'{final_price:.2f}')



