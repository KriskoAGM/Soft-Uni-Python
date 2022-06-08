days_num = int(input())
day_counter = 0
total_litres = 0
total_degrees = 0

for i in range(days_num):
    rakija_quantity = float(input())
    degrees = float(input())

    day_counter += 1
    total_litres += rakija_quantity
    total_degrees += rakija_quantity * degrees

print(f'Liter: {total_litres:.2f}')

average_degrees = total_degrees / total_litres

print(f'Degrees: {average_degrees:.2f}')

if average_degrees < 38:
    print("Not good, you should baking!")

elif 38 <= average_degrees <= 42:
    print("Super!")

else:
    print("Dilution with distilled water!")









