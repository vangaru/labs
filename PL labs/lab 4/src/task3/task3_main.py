import task3_functions

matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
		  [8, 7, 6, 5, 4, 3, 2, 1],
		  [2, 3, 4, 5, 6, 7, 8, 9],
		  [9, 8, 7, 6, 5, 4, 3, 2],
		  [1, 3, 5, 7, 9, 7, 5, 3],
		  [3, 1, 5, 3, 2, 6, 5, 7],
		  [1, 7, 5, 9, 7, 3, 1, 5],
		  [2, 6, 3, 5, 1, 7, 3, 2]]

print("\nЗАДАНИЕ 3")
print("\nДана матрица:")

functions.print_matrix(matrix)

print("\n\nЗАДАНИЕ 3 ПУНКТ 1")
print("Написать функцию сложения по строкам")
functions.rows_sum(matrix)

print("\n\nЗАДАНИЕ 3 ПУНКТ 2")
print("Написать функцию сложения по столбцам")
functions.cols_sum(matrix)

print("\n\nЗАДАНИЕ 3 ПУНКТ 3")
print("Написать функцию сложения по строкам четных элементов")
functions.even_rows_sum(matrix)

print("\n\nЗАДАНИЕ 3 ПУНКТ 4")
print("Написать функцию сложения по столбцам четных элементов")
functions.even_cols_sum(matrix)

