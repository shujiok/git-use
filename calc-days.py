from datetime import datetime

current_date = datetime.today()
print(f"it is {current_date.date().strftime('%Y/%m/%d')} today")
plan_date = datetime.strptime(input('input plan date(%Y/%m/%d): '), '%Y/%m/%d')

# print(current_date)
# print(plan_date)

diff = plan_date - current_date
print(f'days remaining: {diff.days}')

