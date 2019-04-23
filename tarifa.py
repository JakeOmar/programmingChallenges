data = int(input())#asks for the amount of data added per month
months = int(input())#asks for the amount of months
left = 0#sets the counter at zero initially

for i in range(months):#loops for how many months given in the second input
	left = left + data#adds the data available per month to the counter
	left = left - int(input())#removes the amount of data used (given by the input) in the month
print(str(left + data))#gives the amount of data usable in the next month