actor_name = input()
points = float(input())
evaluators_num = int(input())

total_points = points

for i in range(evaluators_num):
    evaluator_name = input()
    points_from_evaluator = float(input())
    total_points += len(evaluator_name) * points_from_evaluator / 2

    if total_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break

points_needed = 1250.5 - total_points

if total_points < 1250.5:
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')