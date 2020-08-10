n = int(input("Enter number of elements : "))

a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

uniqueNumber = list(set(a))

pairs = 0

for number in uniqueNumber:
	numAppear = a.count(number)
	numPairs = int(numAppear / 2)
	pairs = pairs + numPairs
	
print(pairs)
