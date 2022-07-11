phonebook = {}
info = input()

while "-" in info:
    name, phone_number = info.split("-")
    info = input()

    phonebook[name] = phone_number

search_count = int(info)

for i in range(search_count):
    search_name = input()

    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")

