number_of_lines = int(input())
sum_of_letters = 0

for letter in range(number_of_lines):
    letters = input()

    sum_of_letters += ord(letters)

print(f"The sum equals: {sum_of_letters}")
