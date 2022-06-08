num_of_messages = int(input())

for i in range(num_of_messages):
    num = int(input())

    if num == 88:
        print('Hello')
    elif num == 86:
        print('How are you?')
    elif num < 86 or num == 87:
        print('GREAT!')
    elif num > 88:
        print('Bye.')