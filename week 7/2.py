import datetime

now = datetime.datetime.now()

print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%H:%M"))
print(now.strftime("%I:%M %p"))