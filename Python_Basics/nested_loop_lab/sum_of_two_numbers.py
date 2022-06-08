start_num = int(input())
end_num = int(input())
magic_number = int(input())
counter = 0
is_found = False

for i in range(start_num, end_num + 1):
    for x in range(start_num, end_num + 1):
        counter += 1

        if i + x == magic_number:
            print(f'Combination N:{counter} ({i} + {x} = {magic_number})')
            is_found = True
            break

    if is_found:
        break

else:
    print(f'{counter} combinations - neither equals {magic_number}')



