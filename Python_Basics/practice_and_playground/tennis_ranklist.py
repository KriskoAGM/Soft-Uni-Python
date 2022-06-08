from math import floor

num_of_tournaments = int(input())
starting_points = int(input())
final_points = starting_points
win = 0

for i in range(num_of_tournaments):
    progress = input()

    if progress == 'W':
        win += 1
        final_points += 2000

    if progress == 'F':
        final_points += 1200

    if progress == 'SF':
        final_points += 720

average_points = ((final_points - starting_points) / num_of_tournaments)
win_rate = (win / num_of_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_rate:.2f}%")



