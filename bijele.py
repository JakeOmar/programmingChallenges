inp = input().split(" ")
for i in range(len(inp)):
	inp[i] = int(inp[i])

#king, queen, rooks, bishop, knights, pawns
peices = [1,1,2,2,2,8]


for i in range(len(peices)):
	print(peices[i]-inp[i])