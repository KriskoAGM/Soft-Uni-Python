waiting_people = int(input())
lift_state = list(map(int, input().split()))
lift_capacity = len(lift_state) * 4

for index, seat in enumerate(lift_state):

    while seat != 4 and waiting_people > 0:
        seat += 1
        lift_state[index] += 1
        waiting_people -= 1

if lift_capacity > sum(lift_state) and waiting_people == 0:
    print("The lift has empty spots!")
    print(*lift_state)
elif waiting_people > 0 and sum(lift_state) == lift_capacity:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(*lift_state)
elif sum(lift_state) == lift_capacity and waiting_people == 0:
    print(*lift_state)



