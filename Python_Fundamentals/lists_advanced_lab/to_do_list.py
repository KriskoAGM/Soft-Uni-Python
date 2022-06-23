# notes = []
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     task_and_priority = command.split("-")
#     priority = int(task_and_priority[0])
#     task = task_and_priority[1]
#     notes.append((priority, task))
#
# sorted_notes = [task_data[1] for task_data in sorted(notes)]
# print(sorted_notes)

notes = []
while True:
    task = input()

    if task == "End":
        break

    task = task.split("-")
    priority = task[0]
    note = task[1]
    notes.append((priority, note))

result = [x[1] for x in sorted(notes)]
print(result)






























