days_counter = 1
progress = 5364

while True:
    text = input()

    if text == 'END':
        print("Failed.")
        print(f"{progress}")
        break

    if text == 'Yes':
        days_counter += 1

    if days_counter > 5:
        print("Failed.")
        print(f"{progress}")
        break

    metres_climbed = int(input())
    progress += metres_climbed

    if progress >= 8848:
        print(f"Goal reached for {days_counter} days!")
        break

#if progress < 8848:
    #print("Failed.")
    #print(f"{progress}")


