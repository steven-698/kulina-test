# n is number of switches
n = 100
L = [0] * n

for i in range(1, n+1):
	for j in range (1, n+1):
		if(j % i == 0):
			if(L[j-1] == 0):
				L[j-1] = 1
			else:
				L[j-1] = 0

print(L.count(1))