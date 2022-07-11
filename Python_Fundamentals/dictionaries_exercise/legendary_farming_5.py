def check_progress(dict):
    if dict["shards"] >= 250 or dict["fragments"] >= 250 or dict["motes"] >= 250:
        return True
    return False


def obtained_item(dict):
    if dict["shards"] >= 250:
        dict["shards"] -= 250
        return "Shadowmourne obtained!"

    elif dict["fragments"] >= 250:
        dict["fragments"] -= 250
        return "Valanyr obtained!"

    elif dict["motes"] >= 250:
        dict["motes"] -= 250
        return "Dragonwrath obtained!"


materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

while True:
    if check_progress(materials):
        break

    info = input().lower().split()

    for i in range(0, len(info), 2):
        value = int(info[i])
        key = info[i + 1]

        if key not in materials:
            materials[key] = 0
        materials[key] += value

        if check_progress(materials):
            break

print(obtained_item(materials))

for key, value in materials.items():
    print(f"{key}: {value}")
