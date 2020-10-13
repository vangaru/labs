import itertools
import numpy
import math

def get_decart_mult(array):
	decart_mult = []
	for i in itertools.product(array, array):
		decart_mult.append(i)
	
	return decart_mult

def R1_build(pair):
	if pair[0] % 4 == pair[1] % 4:
		return True
	else:
		return False

def R2_build(pair):
	if pair[0] + pair[1] == 8:
		return True
	else:
		return False

def R1_matrix_build(array):
	decart_mult = get_decart_mult(array)
	
	matrix = numpy.zeros((len(array) + 1, len(array) + 1), dtype=numpy.int)

	matrix[0] = range(len(array) + 1)

	for i in range(len(array) + 1):
		matrix[i][0] = i

	for pair in decart_mult:
		if R1_build(pair) == True:
			matrix[pair[0]][pair[1]] = 1
		else:
			matrix[pair[0]][pair[1]] = 0

	print(matrix)



def R2_matrix_build(array):
	decart_mult = get_decart_mult(array)
	
	matrix = numpy.zeros((len(array) + 1, len(array) + 1), dtype=numpy.int)

	matrix[0] = range(len(array) + 1)

	for i in range(len(array) + 1):
		matrix[i][0] = i

	for pair in decart_mult:
		if R2_build(pair) == True:
			matrix[pair[0]][pair[1]] = 1
		else:
			matrix[pair[0]][pair[1]] = 0

	print(matrix)