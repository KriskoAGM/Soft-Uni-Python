course_dict = {}

while True:

    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in course_dict:
        course_dict[course_name] = []
    course_dict[course_name].append(student_name)

for key, value in course_dict.items():
    print(f"{key}: {len(course_dict[key])}")
    for student in course_dict[key]:
        print(f"-- {student}")

