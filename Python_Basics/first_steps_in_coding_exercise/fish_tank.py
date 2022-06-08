length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
volume_in_litres = volume * 0.001
space_needed = percent / 100
litres_needed = volume_in_litres * (1 - space_needed)

print(litres_needed)

