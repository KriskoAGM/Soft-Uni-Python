students_info = {}
command = input()

while ':' in command:

    command = command.split(":")
    name = command[0]
    student_id = int(command[1])
    course = command[2]

    if course not in students_info:
        students_info[course] = {}
    students_info[course][student_id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students_info.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")




