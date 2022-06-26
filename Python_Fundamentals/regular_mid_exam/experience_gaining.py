needed_experience = float(input())
count_of_battles = int(input())
battle_counter = 0
gained_xp = 0

for _ in range(count_of_battles):
    earned_xp = float(input())

    gained_xp += earned_xp
    battle_counter += 1

    if battle_counter % 3 == 0:
        gained_xp += earned_xp * 0.15

    elif battle_counter % 5 == 0:
        gained_xp -= earned_xp * 0.10

    elif battle_counter % 15 == 0:
        gained_xp += earned_xp * 0.5

    if gained_xp >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle_counter} battles.")
        break

if needed_experience > gained_xp:
    diff = abs(needed_experience - gained_xp)
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")
