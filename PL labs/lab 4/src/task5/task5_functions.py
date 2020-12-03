import random

def generate_matrix(N):
	matrix = []

	for i in range(N):
		matrix.append([])
		for j in range(N):
			matrix[i].append(random.randint(1, 10))

	return matrix

def matrix_to_list(matrix):
	lst = []

	for row in matrix:
		for digit in row:
			lst.append(digit)

	print(lst)

def add_two(lst, el1, el2):
	lst.append(el1)
	lst.append(el2)

	return lst

def del_even(lst):
	for element in lst:
		if (type(element) is int or type(element) is float) and  element % 2 == 0:
			lst.remove(element)
	return lst

def print_group_info(my_len, group_name):
	group_info = ""

	for group in my_len:
		if group[0] == group_name:
			group_info += group[0] + ": "
			
			for name in group[1]:
				group_info += name + ", "

			index_to_delete = len(group_info) - 2

			group_info_list = list(group_info)
			group_info_list.pop(index_to_delete)
			group_info = "".join(group_info_list)

			print(group_info)

			group_info = ""

def print_group_students(my_len):
	for group in my_len:
		for name in group[1]:
			full_name = name.split()
			if len(full_name[1]) < 7:
				print(full_name[1])	
