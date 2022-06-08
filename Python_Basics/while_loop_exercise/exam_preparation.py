unsatisfied_grades = int(input())
times_failed = 0
problems_solved = 0
grades_sum = 0
last = ''
failed = True

while times_failed < unsatisfied_grades:
    name_of_problem = input()

    if name_of_problem == 'Enough':
        failed = False
        break

    grade = int(input())

    if grade <= 4:
        times_failed += 1

    grades_sum += grade
    problems_solved += 1
    last = name_of_problem

if failed:
    print(f'You need a break, {unsatisfied_grades} poor grades.')
else:
    print(f'Average score: {grades_sum / problems_solved:.2f}')
    print(f'Number of problems: {problems_solved}')
    print(f'Last problem: {last}')
