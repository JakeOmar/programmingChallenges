time = input().split(" ")
hour = int(time[0])
minute = int(time[1])

if minute >= 45:
	minute = minute - 45
elif hour == 0:
	hour = 23
	minute = 60 - (45 - minute)
else:
	hour = hour - 1
	minute = 60 - (45 - minute)
print(str(hour) + " " + str(minute))