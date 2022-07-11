country = input().split(", ")
capital = input().split(", ")
capitals = {country[i]: capital[i] for i in range(len(country))}

for key, value in capitals.items():
    print(f"{key} -> {value}")
