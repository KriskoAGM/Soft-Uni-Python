version = input().replace(".", "")
next_version = int(version) + 1
empty_list = [x for x in str(next_version)]
print(*empty_list, sep='.')