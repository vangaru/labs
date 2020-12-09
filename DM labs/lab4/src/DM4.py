import itertools
import numpy as np

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


# permutations([1, 2, 3, 4], 2)
# print("\n\n\n")
# antilex_permutations([1, 2, 3, 4], 2)

def get_expression(g1, g2):
	return (g1 * g2) % 63

def get_cayley_table(arr):
	cayley_table = dict()
	for g1 in arr:
		cayley_table[g1] = dict()
		for g2 in arr:
			cayley_table[g1][g2] = get_expression(g1, g2)
	return cayley_table

def is_neutral(e):
	if len(e) == 6:
		return True
	else:
		return False

def get_neutral_el(cayley_table):
	e = []
	for g1 in cayley_table:
		e = []
		for g2 in cayley_table[g1]:
			if g2 * g1 == g2:
				e.append(True)
		if(is_neutral(e)):
			return g1
	return False

def print_reverse_elements(cayley_table, e):
	for g1 in cayley_table:
		for g2 in cayley_table[g1]:
			if cayley_table[g1][g2] == e:
				print(str(g1) + ":" + str(g2))


array = [1,2,4,8,16,32]

def subgroup(g):
	if g == 1:
		return "Нейтральный элемент 1"
	subgroup = [g]

	while True:
		subgroup.append(get_expression(subgroup[-1], g))
		if subgroup[-1] == 1:
			return subgroup

def get_cayley_table_arr(arr):
	cayley_table = np.zeros( ( len(arr), len(arr) ), dtype = int )
	for g1 in range(len(arr)):
		for g2 in range(len(arr)):
			cayley_table[g1][g2] = get_expression(arr[g1], arr[g2])
	return cayley_table

def group_classes(cayley_table_arr, arr):
	index = len(arr) // 2
	for g2 in range(index):
		print(str(arr[g2]) + "H:" + str(cayley_table_arr[0][g2]) + ":" + str(cayley_table_arr[0][g2 + index]))

def get_factor_set(arr):
	index = len(arr) // 2
	factor_set = []
	for i in range(index):
		element = (str(arr[i]) + str("H"))
		factor_set.append(element)
	return factor_set

def factor_cayley_table(arr):
	factor_cayley_table = []
	for g1 in range(len(arr)):
		row = []
		for g2 in range(len(arr)):
			el = (str(get_expression(arr[g1], arr[g2])) + "H")
			row.append(el)
		factor_cayley_table.append(row)
	return factor_cayley_table

cayley_table = get_cayley_table(array)

print("Классы для заданной группы:")
ct = get_cayley_table_arr(array)
group_classes(ct, array)

print("Фактор-множкство:")
fts = get_factor_set(array)

sg = subgroup(4)

print("Подгруппа:")
print(sg)
print("Таблица Кэли по фактор-множеству по данной подгруппе:")
fct = factor_cayley_table(sg)
for row in fct:
	print(row)
#print(cayley_table)
# for g in array:
# 	print(cayley_table[g])

#group_classes(cayley_table, array)



# e = get_neutral_el(cayley_table)
# print("Нейтральный элемент: " + str(e))

# print("Обратные элементы:")
# print_reverse_elements(cayley_table, e)

# for g in array:
# 	print(str(subgroup(g)) + " Порядок подгруппы: " + str(len(subgroup(g)))) 

# sub_cayley_table = get_cayley_table(subgroup(4))

# print("\n")
# print(sub_cayley_table[4])
# print(sub_cayley_table[16])
# print(sub_cayley_table[1])

