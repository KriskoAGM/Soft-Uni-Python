num_of_visitors = int(input())
back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0
work_out_counter = 0
protein_counter = 0

for i in range(num_of_visitors):
    activity = input()

    if activity == 'Back':
        back_counter += 1
        work_out_counter += 1

    if activity == 'Chest':
        chest_counter += 1
        work_out_counter += 1

    if activity == 'Legs':
        legs_counter += 1
        work_out_counter += 1

    if activity == 'Abs':
        abs_counter += 1
        work_out_counter += 1

    if activity == 'Protein shake':
        protein_shake_counter += 1
        protein_counter += 1

    if activity == 'Protein bar':
        protein_bar_counter += 1
        protein_counter += 1

training_num = (work_out_counter * 100) / num_of_visitors
product = (protein_counter * 100) / num_of_visitors

print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{training_num:.2f}% - work out")
print(f"{product:.2f}% - protein")
