number_of_lines = int(input())
tank_capacity = 255
poured_water = 0

for water in range(number_of_lines):
    liters_of_water = int(input())

    if (liters_of_water + poured_water) > tank_capacity:
        print("Insufficient capacity!")
        continue

    poured_water += liters_of_water

print(poured_water)
