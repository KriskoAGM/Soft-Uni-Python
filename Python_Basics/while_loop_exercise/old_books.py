book_name = input()
counter = 0
found = False
current_book = input()

while True:

    if current_book == 'No More Books':
        break

    if current_book == book_name:
        found = True
        print(f"You checked {counter} books and found it.")
        break

    counter += 1
    current_book = input()

if not found:
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')
