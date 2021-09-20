print("how long is the triangle")
size = input()
i = 0
line = [0] * size
line[len(line) - 1] = 1

while i < size:
	printarr(line)

def printarr(arr):
	index = 0
	while index < len(arr):
		if arr[index] > 0:
			print(arr[index])

def updatearr(arr):
	index = 0
	while index < len(arr) - 1:
		arr[index] = arr[index] + arr[index+ 1]
