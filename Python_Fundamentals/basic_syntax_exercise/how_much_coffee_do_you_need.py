needed_coffee = 0

while True:
    command = input()
    if command == 'END':
        break
    if command in {'coding', 'dog', 'cat', 'movie'}:
        needed_coffee += 1
    elif command in {'CODING', 'DOG', 'CAT', 'MOVIE'}:
        needed_coffee += 2
    else:
        continue

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)



