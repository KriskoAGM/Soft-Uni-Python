money_needed = float(input())
money_saved = float(input())
day_counter = 0
spend_counter = 0

while money_saved < money_needed and spend_counter <5:
    command = input()
    money = float(input())
    day_counter += 1

    if command == 'save':
        money_saved += money
        spend_counter = 0

    elif command == 'spend':
        money_saved -= money
        spend_counter += 1

        if money_saved < 0:
            money_saved = 0

    if spend_counter == 5:
        print("You can't save the money.")
        print(day_counter)

    if money_saved >= money_needed:
        print(f'You saved the money for {day_counter} days.')