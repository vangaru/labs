import itertools

def recurrence_ratio(a, n, k1, k2):
	a.append(k1 * a[n - 1] - k2 * a[n - 2])
	print(a)
	if n == 4:
		print("5 член числовой последовательности: " + str(a[n]))
		return
	recurrence_ratio(a, n + 1, k1, k2)

#recurrence_ratio([-3, 1], 2, 2, 1)

def antilex_permutations(arr, k = None):
	if k == None:
		for perm in itertools.permutations(arr):
			print(perm)
	else:
		for perm in itertools.permutations(arr, k):
			print(perm)

def permutations(arr, k = None):
	arr = arr[::-1]
	if k == None:
		for perm in itertools.permutations(arr):
			print(perm)
	else:
		for perm in itertools.permutations(arr, k):
			print(perm)


permutations([1, 2, 3, 4], 2)
print("\n\n\n")
antilex_permutations([1, 2, 3, 4], 2)


