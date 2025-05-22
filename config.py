from datetime import datetime, timedelta

start_date = datetime.strptime("1989-10-22", "%Y-%m-%d")
end_date = datetime.strptime("2012-12-29", "%Y-%m-%d")

current_date = start_date
weekend_count = 0

while current_date <= end_date:
    # weekday(): Monday=0 ... Sunday=6
    if current_date.weekday() in (5, 6):  # Saturday=5, Sunday=6
        weekend_count += 1
    current_date += timedelta(days=1)

print("Weekend days:", weekend_count)
