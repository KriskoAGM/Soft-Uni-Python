step_counter = 0

while step_counter < 10000:
    steps = input()

    if steps == 'Going home':
        steps_left = int(input())
        step_counter += steps_left
        break

    step_counter += int(steps)

diff = int(abs(step_counter - 10000))
if step_counter >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

else:
    print(f'{diff} more steps to reach goal.')