def factorial(x):
	fact = 1
	for i in range(1, x + 1):
		fact = fact * i
	return fact


n = int(input())

for i in range(n):
	number = int(input())#places input as current variable
	number = factorial(number)
	number = str(number)
	print(number[-1])