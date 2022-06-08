import math

record_seconds = float(input())
meters = float(input())
swimming_time = float(input())

time = meters * swimming_time
time_added = math.floor(meters / 15) * 12.5
total_time = time + time_added

if record_seconds > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
elif record_seconds <= total_time:
    not_enough = total_time - record_seconds
    print(f'No, he failed! He was {not_enough:.2f} seconds slower.')


