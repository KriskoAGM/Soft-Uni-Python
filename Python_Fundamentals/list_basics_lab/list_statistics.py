lines = int(input())
positive_list = []
negative_list = []
positive_count = 0

for i in range(lines):
    number = int(input())

    if number >= 0:
        positive_list.append(number)
        positive_count += 1
    else:
        negative_list.append(number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {sum(negative_list)}")