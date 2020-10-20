
#Функция вывода матрицы
def print_matrix(matrix):
	for row in matrix:
		print(row)

#Функция сложения по строкам
def rows_sum(matrix):
	for row in matrix:
		
		row_sum = 0
		
		for element in row:
			row_sum += element

		print(str(row) + " == " + str(row_sum))

#Функция сложения по столбцам
def cols_sum(matrix):
	col_sum = []
	for i in range(len(matrix[0])):
		col_sum.append(0)

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			col_sum[j] += matrix[i][j]

	print_matrix(matrix)
	print("========================")
	print(col_sum)

#Функция сложения по строкам четных элементов.
def even_rows_sum(matrix):
	for row in matrix:
		
		row_sum = 0
		
		for element in row:
			if element % 2 == 0:
				row_sum += element

		print(str(row) + " == " + str(row_sum))


#Функция сложения по столбцам четных элементов
def even_cols_sum(matrix):
	col_sum = []
	for i in range(len(matrix[0])):
		col_sum.append(0)

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] % 2 == 0:
				col_sum[j] += matrix[i][j]

	print_matrix(matrix)
	print("========================")
	print(col_sum)