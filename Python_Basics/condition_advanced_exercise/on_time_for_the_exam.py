exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
diff = abs(exam_time - arrival_time)

if exam_time == arrival_time:
    print('On time')

elif arrival_time > exam_time:
    print('Late')
    hour = diff // 60
    minutes = diff % 60

    if diff > 59:
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')

elif arrival_time < exam_time:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    else:
        print('Early')
        hour = diff // 60
        minutes = diff % 60

        if diff > 59:
            print(f'{hour}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')




