hour = int(input())
day = input()

if day in 'Monday Tuesday Wednesday Thursday Friday Saturday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
elif day == 'Sunday':
    print('closed')