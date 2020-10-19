
#Функция запрашивает user_number до тех пор, пока оно не будет равно my_number
def ask_user_number(my_number):
	while True:
		user_number = int(input("Введите user_number: "))
		if user_number == my_number:
			print("user_number совпал c my_number!!")
			break

#Функция возвращает построчно выводит все строки размером менее 10 символов из списка
def get_list_line(lst):
	for line in lst:
		if len(line) < 10:
			print(line)

#Функция возвращает строку размером N, состоящую из букв R
def get_R_line(N):
	R_line = ""

	for i in range(N):
		R_line += "R"

	return R_line

#Функция возвращает строку без чисел:
def remove_digits(string):
	new_string = ""

	for symbol in string:
		if symbol.isdigit():
			continue
		else:
			new_string += symbol

	return new_string

