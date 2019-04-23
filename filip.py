string = input()
string = string.split(" ")

num1 = string[0]
num1 = num1[::-1]
num1 = int(num1)
num2 = string[1]
num2 = num2[::-1]
num2 = int(num2)

if num1 > num2:
	print(num1)
else:
	print(num2)