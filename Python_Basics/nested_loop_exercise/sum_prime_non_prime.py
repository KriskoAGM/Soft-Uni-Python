flag = False
prime_numbers = 0
non_prime = 0

while True:
    current_num = input()

    if current_num == 'stop':
        break

    current_num = int(current_num)

    if current_num < 0:
        print('Number is negative.')

    else:
        if current_num > 1:
            for i in range(2, current_num):
                if current_num % i == 0:
                    flag = True
                    break
            if flag:
                non_prime += current_num
                flag = False
            else:
                prime_numbers += current_num

print(f'Sum of all prime numbers is: {prime_numbers}')
print(f'Sum of all non prime numbers is: {non_prime}')