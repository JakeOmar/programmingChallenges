n = int(input())

for i in range(n):
	number = int(input())
	#check if number odd or even
	if number % 2 == 0:
		print(str(number) + " is even")
	else:
		print(str(number) + " is odd")