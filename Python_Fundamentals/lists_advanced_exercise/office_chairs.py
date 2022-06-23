rooms = int(input())
total_chairs = ''
total_people = 0

for room in range(1, rooms + 1):
    chairs, people = input().split()
    total_chairs += chairs
    total_people += int(people)

    if len(chairs) < int(people):
        print(f"{abs(len(chairs) - int(people))} more chairs needed in room {room}")

if len(total_chairs) >= total_people:
    print(f"Game On, {abs(len(total_chairs) - total_people)} free chairs left")


