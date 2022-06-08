capacity = int(input())
seats_left = capacity
income = 0

while True:
    num_of_people = input()

    if num_of_people == 'Movie time!':
        print(f"There are {seats_left} seats left in the cinema.")
        break

    if int(seats_left) >= int(num_of_people):
        seats_left -= int(num_of_people)

    else:
        print("The cinema is full.")
        break

    if int(num_of_people) % 3 == 0:
        price = (int(num_of_people) * 5) - 5
        income += price

    else:
        price = int(num_of_people) * 5
        income += price

print(f'Cinema income - {income} lv.')

