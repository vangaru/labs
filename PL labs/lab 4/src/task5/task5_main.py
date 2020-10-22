import task5_functions

matrix = functions.generate_matrix(5)
functions.matrix_to_list(matrix)

functions.del_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

my_len = [ ['PO-4', ['Ivan Ivanenko', 'Dima Gribovskiy']], ['PO-5', ['Daniil Filatov']], ['PO-4', ['Ivan Ivanenko', 'Dima Gribovskiy']] ]

functions.print_group_info(my_len, 'PO-4')

functions.print_group_students(my_len)