some_string = input().split(", ")
result = sorted(some_string, key=lambda x: (-len(x), x))
print(result)