numbers = input().split()
numbers_to_remove = int(input())
integer_list = []

for n in numbers:
    integer_list.append(int(n))

for index in range(numbers_to_remove):
    integer_list.remove(min(integer_list))
print(*integer_list, sep=", ")

# numbers = list(map(int, input().split()))
# remove = int(input())
#
# for num in range(remove):
#     numbers.remove(min(numbers))
# print(", ".join(str(x) for x in numbers))
