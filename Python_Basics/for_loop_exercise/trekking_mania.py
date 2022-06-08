number_of_groups = int(input())
total_people = 0
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(number_of_groups):
    people = int(input())
    total_people = total_people + people

    if people <= 5:
        musala += people

    elif 6 <= people <= 12:
        mont_blanc += people

    elif 13 <= people <= 25:
        kilimanjaro += people

    elif 26 <= people <= 40:
        k2 += people

    elif 41 <= people:
        everest += people

print(f'{musala / total_people * 100:.2f}%')
print(f'{mont_blanc / total_people * 100:.2f}%')
print(f'{kilimanjaro / total_people * 100:.2f}%')
print(f'{k2 / total_people * 100:.2f}%')
print(f'{everest / total_people * 100:.2f}%')






