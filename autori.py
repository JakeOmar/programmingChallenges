inp = input().split("-")
# splits input by hyphen
acro = []
# creates empty array
for name in inp:#iterates over the amout of things in the inp list
	acro.append(name[0])#adds the first letter of each element in the list to the array

acro = "".join(acro)#joins the array together with nothing as delimiter as a string
print(acro)