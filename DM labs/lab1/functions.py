
#СОЗДАНИЕ БИТОВОЙ МАСКИ
def bitmask_generation(array, universum):
	bitmask = []

	for element in universum:
		if element in array:
			bitmask.append(1)
		else:
			bitmask.append(0)

	return bitmask


#ПРЯМОЕ ПРОИЗВЕДЕНИЕ МНОЖЕСТВ
def array_union(array1, array2):
	union = []
	union_part = []

	for i in range(len(array1)):
		for j in range(len(array2)):
			union_part.append(array1[i])
			union_part.append(array2[j])
			union.append(union_part)
			union_part = []

	union_power = len(union) * 2

	print("\nПРОИЗВЕДЕНИЕ:" + str(union) + "\n")
	print("МОЩНОСТЬ:" + str(union_power) + "\n")


#СОЗДАНИЕ И ВЫВОД БУЛЕАНА И БИНАРНОГО КОДА МНОЖЕСТВ
def boolean(array):
	boolean = []
	boolean_part = []
	boolean_pattern = []
	boolean_binary_code = []
	boolean_size = 2 ** len(array)

	print("\nБИНАРНЫЙ КОД МНОЖЕСТВ:\n")

	for n in range(boolean_size):
		while n > 0:
			boolean_binary_code = [n % 2] + boolean_binary_code
			n = n // 2

		if len(boolean_binary_code) < len(array):
			for i in range(len(boolean_binary_code), len(array)):
				boolean_binary_code = [0] + boolean_binary_code

		print(boolean_binary_code)

		boolean_pattern.append(boolean_binary_code)
		boolean_binary_code = []

	print("\nБУЛЕАН:\n")

	for boolean_binary_code in boolean_pattern:
		for index in range(len(array)):
			if boolean_binary_code[index] == 1:
				boolean_part.append(array[index])

		print(boolean_part)
		boolean.append(boolean_part)
		boolean_part = []

	return boolean


#СЛИВАЕТ ДВА СПИСКА В ОДИН ОТСОРТИРОВАННЫЙ СПИСОК И ВОЗВРАЩАЕТ ЕГО
def merge(left_array, right_array):
	sorted_array = []
	left_array_index = 0
	right_array_index = 0

	for i in range(len(left_array) + len(right_array)):

		if left_array_index < len(left_array) and right_array_index < len(right_array):

			if left_array[left_array_index] < right_array[right_array_index]:
				sorted_array.append(left_array[left_array_index])
				left_array_index += 1
			
			else:
				sorted_array.append(right_array[right_array_index])
				right_array_index += 1

		elif left_array_index == len(left_array):
			sorted_array.append(right_array[right_array_index])
			right_array_index += 1

		elif right_array_index == len(right_array):
			sorted_array.append(left_array[left_array_index])
			left_array_index += 1

	return sorted_array


#ФУНКЦИЯ БЫСТРОЙ СОРТИРОВКИ
def merge_sort(array):

	if len(array) < 2:
	 	return array

	mid = len(array) // 2

	left_array = merge_sort(array = array[:mid])
	right_array = merge_sort(array = array[mid:])
	
	return merge(left_array = left_array, right_array = right_array)


#ФУНКЦИЯ ПЕРЕСЕЧЕНИЯ МНОЖЕСТВ
def array_crossing(array1, array2, array3, universum):
	array1_bitmask = bitmask_generation(array = array1, universum = universum)
	array2_bitmask = bitmask_generation(array = array2, universum = universum)
	array3_bitmask = bitmask_generation(array = array3, universum = universum)
	crossing_array = []
	
	for index in range(len(universum)):
		if array1_bitmask[index] == array2_bitmask[index] == array3_bitmask[index] == 1:
			crossing_array.append(universum[index])


	print("\nПЕРЕСЕЧЕНИЕ МНОЖЕСТВ:\n")
	print(crossing_array)


#ФУНКЦИЯ ВОЗВРАТА РАЗНОСТИ 2 МНОЖЕСТВ
#array1 - МНОЖЕСТВО, ИЗ КОТОРОГО ВЫЧИТАЕТСЯ array2
def array_differ(array1, array2, universum):
	array1_bitmask = bitmask_generation(array = array1, universum = universum)
	array2_bitmask = bitmask_generation(array = array2, universum = universum)
	differ_array = array1

	for index in range(len(universum)):
		if array1_bitmask[index] == array2_bitmask[index] == 1:
			differ_array.remove(universum[index])

	return differ_array


#ФУНКЦИЯ ВОЗВРАТА РЕЗУЛЬТАТА ВЫПОЛНЕНИЯ ОПЕРАЦИИ ПО ВАРИАНТУ
#(A \ B) \ C
def lab_operation(array1, array2, array3, universum):
	return array_differ(array1 = array_differ(array1, array2, universum), array2 = array3, universum = universum)


#ФУНКЦИЯ РАЗБИЕНИЯ МНОЖЕСТВА
def partition(array):
	if len(array) == 1:
		yield [array]
		return

	first = array[0]

	for smaller in partition(array[1:]):

		for n, subset in enumerate(smaller):
			yield smaller[:n] + [[first] + subset]  + smaller[n+1:]

		yield [[first]] + smaller


#ФУНКЦИЯ ВЫВОДА РАЗБИЕНИЯ
def partition_output(array):

	print("\nРАЗБИЕНИЕ МНОЖЕСТВА:\n")

	for subset in partition(array = array):
		print(subset)
	



def gray_code(array):
	gray_code = []

	print("\nБИНАРНЫЙ КОД ГРЕЯ ДЛЯ КАЖДОГО ЭЛЕМЕНТА МНОЖЕСТВА\n")

	for element in array:
		element_to_gray = element ^ (element >> 1)
		
		while(element_to_gray > 0):
			gray_code = [element_to_gray % 2] + gray_code
			element_to_gray = element_to_gray // 2

		if len(gray_code) < 4:
			for i in range(len(gray_code), 4):
				gray_code = [0] + gray_code
		
		print(gray_code)
		gray_code = []







