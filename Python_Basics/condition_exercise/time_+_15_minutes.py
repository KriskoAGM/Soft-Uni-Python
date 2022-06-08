hour = int(input())
minutes = int(input())

time = (hour * 60) + minutes + 15
current_minutes = time % 60
current_hour = time // 60

if current_hour > 23:
    print(f'0:{current_minutes:02d}')
else:
    print(f'{current_hour}:{current_minutes:02d}')
