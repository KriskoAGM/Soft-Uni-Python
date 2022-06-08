num_of_jury = int(input())
students_counter = 0
total_grades = 0

while True:
    current_presentation_grade = 0
    presentation_name = input()

    if presentation_name == 'Finish':
        total_grades /= num_of_jury * students_counter
        print(f"Student's final assessment is {total_grades:.2f}.")
        break

    students_counter += 1
    for i in range(num_of_jury):
        jury_grade = float(input())
        current_presentation_grade += jury_grade
        total_grades += jury_grade

    current_presentation_grade /= num_of_jury
    print(f'{presentation_name} - {current_presentation_grade:.2f}.')