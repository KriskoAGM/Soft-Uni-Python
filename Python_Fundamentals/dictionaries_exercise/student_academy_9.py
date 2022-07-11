def remove_students(dict):
    for key, value in list(dict.items()):
        average = sum(value) / len(value)
        if average < 4.50:
            dict[key] = average
            dict.pop(key)
            continue
        dict[key] = average


grade_dict = {}
number_of_students = int(input())

for _ in range(number_of_students):
    student_name = input()
    student_grade = input()

    if student_name not in grade_dict:
        grade_dict[student_name] = []
    grade_dict[student_name].append(float(student_grade))

remove_students(grade_dict)

for key, value in grade_dict.items():
    print(f"{key} -> {value:.2f}")
