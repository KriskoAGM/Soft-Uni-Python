import itertools

print("This program takes a combination of letters, numbers and symbols\nprints all possible combinations and their "
      "count and adds them into a text file\n")
print("NOTE: each time you run this program the text file will be overwritten\n")
counter = 0
numbers = input("Enter combination: ")
permutations = list(itertools.permutations(numbers))

new_list = ([''.join(permutation) for permutation in permutations])
file = open("combinations.txt", "w+")

for element in new_list:
    counter += 1
    print(f"Combination {counter}: {element}")
    file.write(f"{element}\n")

print(f"Total combinations found: {counter}\n")

while True:
    command = input("Type 'Quit' to exit program: ")
    if command == 'Quit'.lower():
        break
