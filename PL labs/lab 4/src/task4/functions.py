
#Функция возвращает строку, состоящую слова, в которых первые 2 буквы - Ли
def get_str(string):
	string = string.replace(",", "")
	string = string.replace(".", "")
	string = string.replace("!", "")
	string = string.replace("?", "")
	string = string.replace(";", "")
	string = string.replace(";", "-")

	string = string.split()

	new_string = ""

	for word in string:
		if word[0] == "Л" and word[1] == "и":
			new_string  = new_string + word + " "

	return new_string

#Функция возврощает массив, содержащий информацию о студентах
def get_str_matrix(string, cols):
	string = string.replace("_", "")
	string = string.split(";")

	str_matrix = []
	str_matrix_row = []

	for i in range(len(string)):
		if i == len(string) - 1:
			str_matrix_row.append(string[i])
			str_matrix.append(str_matrix_row)
			break

		if i != 0 and i % cols == 0:
			str_matrix.append(str_matrix_row)
			str_matrix_row = []

		str_matrix_row.append(string[i])

	return str_matrix

#Функция форматированного вывода 
def get_format_str(string):
	str_matrix = get_str_matrix(string, 5)

	for i in range(len(str_matrix)):
		if i == 0:
			print("%-25s %-15s %-15s" % (str_matrix[i][0] + str_matrix[i][1] + str_matrix[i][2],
							   		 	 str_matrix[i][3],
							   		 	 str_matrix[i][4],
			))
		else:
			print("%-25s %-15s %-15s" % (str_matrix[i][0] + " " + str_matrix[i][1] + " " + str_matrix[i][2], 
										 str_matrix[i][3], 
										 str_matrix[i][4],
			))

def get_students(string):
	str_matrix = get_str_matrix(string, 3)

	for student in str_matrix:
		if student[1][0] == "2" and student[1][1] == "1":
			print(student)

def calculate_data(string):
	data_list = string.split()
	amount_of_symbols = 0
	amount_of_words = 0

	for word in data_list:
		amount_of_words += 1
		amount_of_symbols += len(word)

	print("Количество слов: " + str(amount_of_words))
	print("Количество символов: " + str(amount_of_symbols))

