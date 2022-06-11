type_of_fire = input().split("#")
water = int(input())
current_water = water
cell_list = []
high_cell = 0
medium_cell = 0
low_cell = 0
effort = 0
total_fire = 0

for i in type_of_fire:
    level = i.split(" = ")
    cell = int(level[1])

    if cell > current_water:
        continue

    if 81 <= cell <= 125 and "High" in level:
        high_cell = cell
        current_water -= cell
        effort += cell * 0.25
        total_fire += cell
    elif 51 <= cell <= 80 and "Medium" in level:
        medium_cell = cell
        current_water -= cell
        effort += cell * 0.25
        total_fire += cell
    elif 1 <= cell <= 50 and "Low" in level:
        low_cell = cell
        current_water -= cell
        effort += cell * 0.25
        total_fire += cell
    else:
        continue
    if current_water >= 0:
        cell_list.append(cell)

print("Cells: ")
for element in cell_list:
    print(f" - {element}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




