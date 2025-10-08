from datetime import datetime, timedelta
today = datetime.now()
new_date = today - timedelta(days=5)
print("Current date:", today)
print("Date minus 5 days:", new_date)

#Print yesterday, today, tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())

#Drop microseconds from datetime
now = datetime.now().replace(microsecond=0)
print("Datetime without microseconds:", now)

#Calculate two date difference in seconds
date1 = datetime(2025, 10, 1, 12, 0, 0)
date2 = datetime(2025, 10, 8, 12, 0, 0)
diff = (date2 - date1).total_seconds()
print("Difference in seconds:", diff)