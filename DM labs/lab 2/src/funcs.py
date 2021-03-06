import itertools
import numpy
import math

# ФУНКЦИЯ ВОЗВРАЩАЕТ ДЕКАРТОВО ПРОИЗВЕДЕНИЯ МНОЖЕСТВА
def get_decart_mult(array):
	decart_mult = []
	for i in itertools.product(array, array):
		decart_mult.append(i)
	
	return decart_mult

# ФУНКЦИЯ ВОЗВРАЩАЕТ TRUE, ЕСЛИ ПАРА ДЕКАРТОВА ПРОИЗВЕДЕНИЯ
# ОТНОСИТСЯ К ОТНОШЕНИЮ R1
def R1_build(pair):
	return pair[0] % 4 == pair[1] % 4

# ФУНКЦИЯ ВОЗВРАЩАЕТ TRUE, ЕСЛИ ПАРА ДЕКАРТОВА ПРОИЗВЕДЕНИЯ
# ОТНОСИТСЯ К ОТНОШЕНИЮ R1
def R2_build(pair):
	return pair[0] + pair[1] == 8

# ФУНКЦИЯ ВОЗВРАЩАЕТ ОТНОШЕНИЕ R1
def get_R1(array):
	decart_mult = get_decart_mult(array)
	R1 = []

	for pair in decart_mult:
		if R1_build(pair) == True:
			R1.append(pair)

	return R1

# ФУНКЦИЯ ВОЗВРАЩАЕТ ОТНОШЕНИЕ R2
def get_R2(array):
	decart_mult = get_decart_mult(array)
	R2 = []

	for pair in decart_mult:
		if R2_build(pair) == True:
			R2.append(pair)

	return R2

# ФУНКЦИЯ ВОЗВРАЩАЕТ МАТРИЦУ ОТНОШЕНИЙ
def matrix_build(R, array):

	matrix = numpy.zeros((len(array), len(array)), dtype=numpy.int)

	for pair in R:
		matrix[pair[0] - 1][pair[1] - 1] = 1 

	return matrix

# ФУНКЦИЯ ВОЗВРАЩАЕТ ОБРАТНОЕ ОТНОШЕНИЕ 
def get_inverse_relation(R):
	inverse_relation = []

	for pair in R:
		temp_pair = pair
		pair = []

		pair.append(temp_pair[1])
		pair.append(temp_pair[0])

		inverse_relation.append(pair)

	return inverse_relation

# ФУНКЦИЯ ВОЗВРАЩАЕТ ДОПОЛНЕНИЕ ОТНОШЕНИЯ
def get_relation_addition(array, R):
	decart_mult = get_decart_mult(array)
	relation_addition = []

	for pair in decart_mult:
		if pair not in R:
			relation_addition.append(pair)

	return relation_addition 

# ФУНКЦИЯ ВОЗВРАЩАЕТ МАТРИЦУ ТРАНЗИТИВНОГО ЗАМЫКАНИЯЫ
def get_transitive_closure(matrix):
	n = len(matrix)
	transitive_closure = matrix 
	
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if (matrix[i][k] and matrix[k][j] == True):
					transitive_closure[i][j] = 1
				
	return transitive_closure

# ФУНКЦИЯ ВОЗВРАЩАЕТ КОМПОЗИЦИЮ ДВУХ ОТНОШЕНИЙ
def attitudes_composition( R1, R2):
	composition = []
	composition_pair = []

	for R1_pair in R1:
		for R2_pair in R2:
			if R1_pair[1] == R2_pair[0]:
				composition_pair.append(R1_pair[0])
				composition_pair.append(R2_pair[1])
				composition.append(composition_pair)
				composition_pair = []

	
	new_composition = []
	for pair in composition:
		if pair not in new_composition:
			new_composition.append(pair)

	return new_composition

#ФУНКЦИЯ ВОЗВРАЩАЕТ TRUE ЕСЛИ ОТНОШЕНИЕ ЯВЛЯЕТСЯ ФУНКЦИЕЙ 
def is_func(S):
	unambiguity = []

	for pair in S:
		
		if pair[0] in unambiguity:
			return False
		
		unambiguity.append(pair[0])

	return True

def func_type(B, C, S):
	if is_func(S):
		C_involved = []
		for pair in S:
			C_involved.append(pair[1])
		C_involved = set(C_involved)


		if(len(C) > len(C_involved)):
			print("Не инъекция и не сюрьекция")
		elif len(B) < len(C_involved):
			print("Инъекция не сюрьекция")
		elif len(C_involved) < len(B):
			print("Сюрьекция не инъекция")
		else:
			print("Биекция")
		return
	print("Не функция")














