number_of_electrons = int(input())
shell = []

for i in range(1, number_of_electrons):
    current_shell_capacity = 2 * i ** 2

    if current_shell_capacity < number_of_electrons:
        shell.append(current_shell_capacity)
        number_of_electrons -= current_shell_capacity
    else:
        shell.append(number_of_electrons)
        break

print(shell)

