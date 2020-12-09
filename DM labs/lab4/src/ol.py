x = 10000
f = open('input.txt') 
N = int(f.read())
arr = [i for i in range(1, x + 1)]
unrep = []
for i in arr:
	flag = []
	for j in str(i):
		if str(i).count(j) == 1:
			flag.append(True)
	if len(flag) == len(str(i)):
		unrep.append(i)
unrep = list(set(unrep))
unrep.sort()
f = open ('output.txt', 'w') 
f.write(str(unrep[N-1]))







