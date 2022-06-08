deposit_sum = float(input())
deposit_term = int(input())
annual_percent = float(input())

per_year = deposit_sum * (annual_percent / 100)
per_month = per_year / 12
total_sum = deposit_sum + (deposit_term * per_month)

print(total_sum)
