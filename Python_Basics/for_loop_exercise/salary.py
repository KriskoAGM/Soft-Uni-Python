opened_tabs = int(input())
salary = float(input())
condition = False


for _ in range(opened_tabs):
    current_tabs = input()

    if current_tabs == 'Facebook':
        salary -= 150
    elif current_tabs == 'Instagram':
        salary -= 100
    elif current_tabs == 'Reddit':
        salary -= 50

    if salary <= 0:
        condition = True
        break


if not condition:
    print(int(salary))
else:
    print('You have lost your salary.')