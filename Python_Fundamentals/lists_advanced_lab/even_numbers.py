numbers = list(map(int, input().split(", ")))
indices = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(indices)