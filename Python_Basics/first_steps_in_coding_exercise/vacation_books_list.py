number_of_pages = int(input())
pages = int(input())
days = int(input())

total_time = number_of_pages / pages
time_needed = total_time // days
print(time_needed)