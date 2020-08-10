n = int(input("Enter number of elements : "))

a = list(input("\nEnter the character : ").strip().split())[:n]

for index, i in enumerate(a):
	if(i.upper() == 'U'):
		a[index] = 1
	
	if(i.upper() == 'D' ):
		a[index] = -1

isValley = False
numValley = 0
path = 0 

for n in a:
	path = path + n
	if(path < 0):
		isValley = True
	elif(path > 0):
		isValley = False
	elif(path == 0 and isValley):
		numValley = numValley + 1
		
print(numValley)