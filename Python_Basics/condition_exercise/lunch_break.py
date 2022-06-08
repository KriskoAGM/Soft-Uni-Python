import math

show_name = input()
episode_length = int(input())
brake = int(input())

lunch_time = brake / 8
chill_time = brake / 4
left_time = brake - lunch_time - chill_time

free_time = math.ceil(abs(episode_length - left_time))

if left_time >= episode_length:
    print(f'You have enough time to watch {show_name} and left with {free_time} minutes free time.')
else:
    print(f"You don't have enough time to watch {show_name}, you need {free_time} more minutes.")





