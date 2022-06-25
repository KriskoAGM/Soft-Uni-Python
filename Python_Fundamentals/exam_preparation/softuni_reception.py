employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
count_of_students = int(input())
time_needed = 0
all_employee_answers_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency

while count_of_students > 0:
    count_of_students -= all_employee_answers_per_hour
    time_needed += 1
    if time_needed % 4 == 0:
        time_needed += 1

print(f"Time needed: {time_needed}h.")

