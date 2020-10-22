from random import randint
import sys
sys.path.append('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 4/src/task1')
sys.path.append('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 4/src/task2')
sys.path.append('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 4/src/task3')
sys.path.append('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 4/src/task4')
sys.path.append('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 4/src/task5')

import task1_functions
import task2_functions
import task3_functions
import task4_functions
import task5_functions

def task1_selection():
	print("\nЗАДАНИЕ 1")
	print("1 - Пункт 1 - Решить пример")
	print("2 - Пункт 2 - Дан список, содержащий строки и числа. Вывести все нечетные элементы списка построчно")
	print("3 - Пункт 3 - Дан список, содержащий только числа. Вывести результат сложения всех чисел от 1 до 10")
	print("4 - Пункт 4 - Дан список, содержащий только числа. Вывести минимальное число")

	point_choice = int(input("Выберите пункт задания: "))

	if point_choice == 1:
		print("\nЗадание 1 Пункт 1 - Решить пример")

		a = float(input('Введите a: '))
		b = float(input('Введите b: '))
		c = float(input('Введите c: '))
		d = float(input('Введите d: '))
		k = float(input('Введите k: '))
		
		task1_functions.print_expression_result(a, b, c, d, k)

	elif point_choice == 2:
		print("\nЗадание 1 Пункт 2 - Дан список, содержащий строки и числа. Вывести все нечетные элементы списка построчно")
		
		lst = [1, "two", "three", 4, 5.1, 6, 7, 8, 9]
		print("Изначальный список: " + str(lst))
		print("Полученные значения")
		task1_functions.print_odd_elements(lst)

	elif point_choice == 3:
		print("\nЗадание 1 Пункт 3 - Дан произвольный список, содержащий только числа. Вывести результат сложения всех чисел от 1 до 10")
		
		lst = [1, 15, -5, 26, 5, 9, 10]
		print("Изначальный список: " + str(lst))
		print("Результат сложения всех чисел от 1 до 10: " + str(task1_functions.get_calculate_result(lst)))

	elif point_choice == 4:
		print("\nЗадание 1 Пункт 4 - Дан список, содержащий только числа. Вывести минимальное число")

		lst = [3, 5, 0, -1, 20]
		print("Изначальный список: " + str(lst))
		print("Минимальное число: " + str(min(lst)))

	else:
		print("\nНеверный ввод!")

#################################################################################################################################

def task2_selection():
	print("\nЗАДАНИЕ 2 - Строки и списки")
	print("1 - Пункт 1 - Запрашивать у пользователя user_number до тех пор, пока оно не будет равно my_number")
	print("2 - Пункт 2 - Пусть задан список, содержащий строки. Выведите построчно все строки размером менее 10 символов")
	print("3 - Пункт 3 - Сгенерируйте и выведите строку размером N и состоящую из букв R")
	print("4 - Пункт 4 - Пусть дана строка. На основе данной строки сформируйте новую, содержащую только буквы")

	point_choice = int(input("Выберите пункт задания: "))

	if point_choice == 1:
		print("\nЗадание 2 Пункт 1 - Запрашивать у пользователя user_number до тех пор, пока оно не будет равно my_number")
		
		my_number = randint(1, 10)
		print("Число my_number: " + str(my_number))
		task2_functions.ask_user_number(my_number)

	elif point_choice == 2:
		print("\nЗадание 2 Пункт 2 - Пусть задан список, содержащий строки. Выведите построчно все строки размером менее 10 символов")

		lst = ["Python", "Laravel", "The Last OF Us 2", "Django", "Dragon Age Origins", "Fallout New Vegas", "PHP"]
		print("Изначальный список: " + str(lst))
		print("Полученные строки:")
		task2_functions.get_list_line(lst)

	elif point_choice == 3:
		print("\nЗадание 2 Пункт 3 - Сгенерируйте и выведите строку размером N и состоящую из букв R")

		N = int(input("Введите N: "))
		print("Полученная строка: " + task2_functions.get_R_line(N))

	elif point_choice == 4:
		print("\nЗадание 2 Пункт 4 - Пусть дана строка. На основе данной строки сформируйте новую, содержащую только буквы")

		string = "ffhuh43f84309fj3f349f";
		print("Изначальная строка: " + string)
		print("Полученная строка: " + task2_functions.remove_digits(string))
	
	else:
		print("\nНеверный ввод!")

#################################################################################################################################

def task3_selection():
	print("\nЗАДАНИЕ 3 - Матрицы")
	print("Дана матрица:")
	matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
		  	  [8, 7, 6, 5, 4, 3, 2, 1],
		  	  [2, 3, 4, 5, 6, 7, 8, 9],
		      [9, 8, 7, 6, 5, 4, 3, 2],
		      [1, 3, 5, 7, 9, 7, 5, 3],
		      [3, 1, 5, 3, 2, 6, 5, 7],
		      [1, 7, 5, 9, 7, 3, 1, 5],
		      [2, 6, 3, 5, 1, 7, 3, 2]]
	task3_functions.print_matrix(matrix)
	print("1 - Пункт 1 - Написать функцию сложения по строкам")
	print("2 - Пункт 2 - Написать функцию сложения по столбцам")
	print("3 - Пункт 3 - Написать функцию сложения по строкам четных элементов")
	print("4 - Пункт 4 - Написать функцию сложения по столбцам четных элементов")

	point_choice = int(input("Выберите пункт задания: "))

	if point_choice == 1:
		print("\nЗадание 3 Пункт 1 - Написать функцию сложения по строкам")
		task3_functions.rows_sum(matrix)

	elif point_choice == 2:
		print("\nЗадание 3 Пункт 2 - Написать функцию сложения по столбцам")
		task3_functions.cols_sum(matrix)

	elif point_choice == 3:
		print("\nЗадание 3 Пункт 3 - Написать функцию сложения по строкам четных элементов")
		task3_functions.even_rows_sum(matrix)

	elif point_choice == 4:
		print("\nЗадание 3 Пункт 4 - Написать функцию сложения по столбцам четных элементов")
		task3_functions.even_cols_sum(matrix)

	else:
		print("\nНеверный ввод!")

#################################################################################################################################

def task4_selection():
	print("\nЗАДАНИЕ 4 - Строки")
	print("1 - Пункт 1 - На основе данной строки создайте новую, в которой первые 2 буквы - Ли")
	print("2 - Пункт 2 - Дана строковая переменная, содержащая информацию о студентах. Вывести строку в определенном формате")
	print("3 - Пункт 3 - Дана строковая переменная, содержащая информацию о студентах. Вывести студентов, чей возраст 21 год")
	print("4 - Пункт 4 - Дана строка произвольной длины. Выведите информацию, о том, сколько в ней символов и слов")

	point_choice = int(input("Выберите пункт задания: "))

	if point_choice == 1:
		print("\nЗадание 4 Пункт 1 - На основе данной строки создайте новую, в которой первые 2 буквы - Ли")
		string = "Лист бумаги Лицея упал на пол - лицом,"
		print("Изначальная строка: " + string)
		print("Полученная строка: " + task4_functions.get_str(string))

	elif point_choice == 2:
		print("\nЗадание 4 Пункт 2 - Дана строковая переменная, содержащая информацию о студентах. Вывести строку в определенном формате")
		my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
		print("Изначальная строка: " + my_string)
		print("Отформатированная строка:")
		task4_functions.get_format_str(my_string)

	elif point_choice == 3:
		print("\nЗадание 4 Пункт 3 - Дана строковая переменная, содержащая информацию о студентах. Вывести студентов, чей возраст 21 год")
		students_info = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибович Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Cтудент 1 курса;"
		students_info = students_info + "_Романов Станислав Андреевич;23 года;Студент 3 курса;"
		students_info = students_info + "_Петров Всеволод Борисович;21 год;Студент 2 курса;"

		print("Данная строка: " + students_info)
		print("Студенты, чей Возраст 21 год:")
		task4_functions.get_students(students_info)

	elif point_choice == 4:
		print("\nЗадание 4 Пункт 4 - Дана строка произвольной длины. Выведите информацию, о том, сколько в ней символов и слов")
		
		string = "Лист бумаги Лицея упал на пол лицом"
		print("Данная строка: " + string)
		task4_functions.calculate_data(string)

	else:
		print("\nНеверный ввод!")

#################################################################################################################################

def task5_selection():
	print("\nЗАДАНИЕ 5 - Списки")
	print("1 - Пункт 1 - Дана матрица размером NxN. Представить матрицу в виде списка")
	print("2 - Пункт 2 - Дан список из 10 элементов. Удалить все четные элементы и добавить 2 новых")
	print("3 - Пункт 3 - Вывести список студентов группы в определенном формате")
	print("4 - Пункт 4 - Вывести студентов, чья фамилия меньше 7 букв")

	point_choice = int(input("Выберите пункт задания: "))

	if point_choice == 1:
		print("\nЗадание 5 Пункт 1 - Дана матрица размером NxN. Представить матрицу в виде списка")
		N = int(input("Введите N: "))
		matrix = task5_functions.generate_matrix(N)
		print("Полученная матрица:")
		task3_functions.print_matrix(matrix)
		print("Данная матрица в виде списка:")
		task5_functions.matrix_to_list(matrix)

	elif point_choice == 2:
		print("\nЗадание 5 Пункт 2 - Дан список из 10 элементов. Удалить все четные элементы и добавить 2 новых")
		lst = [1, 2, 3, 4, 5, 'six', 7, 8, 9, 10]
		print("Изначальный список: " + str(lst))
		lst = task5_functions.del_even(lst)
		lst = task5_functions.add_two(lst, 11, 'twelve')
		print("Полученный список: " + str(lst))

	elif point_choice == 3:
		print("\nЗадание 5 Пункт 3 - Вывести список студентов определенной группы в определенном формате")
		group_journal = [ ['PO-4', ['Ivan Ivanenko', 'Dima Gribovskiy']], ['PO-5', ['Daniil Filatov']] ]
		print("Журнал: " + str(group_journal))

		group_name = input("Введите название группы: ")
		print("Информация о данной группе:")
		task5_functions.print_group_info(group_journal, group_name)

	elif point_choice == 4:
		print("\nЗадание 5 Пункт 4 - Вывести студентов, чья фамилия меньше 7 букв")
		group_journal = [ ['PO-4', ['Ivan Ivanenko', 'Dima Gribovskiy']], ['PO-5', ['Daniil Filatov']], ['Singers', ['Bob Dylan', 'Axl Rose']] ]
		print("Журнал: " + str(group_journal))

		print("Студеты, чья фамилия меньше 7 букв:")
		task5_functions.print_group_students(group_journal)

	else:
		print("\nНеверный ввод!")

#################################################################################################################################

def menu():
	while True:
		print("\n1 - ЗАДАНИЕ 1")
		print("2 - ЗАДАНИЕ 2 - Строки и списки")
		print("3 - ЗАДАНИЕ 3 - Матрицы")
		print("4 - ЗАДАНИЕ 4 - Строки")
		print("5 - ЗАДАНИЕ 5 - Списки")
		print("0 - ВЫХОД")

		task_choice = int(input("Выберите задание: "))

		if task_choice == 1:
			task1_selection();

		elif task_choice == 2:
			task2_selection()

		elif task_choice == 3:
			task3_selection()

		elif task_choice == 4:
			task4_selection()

		elif task_choice == 5:
			task5_selection()

		elif task_choice == 0:
			print("\nЗавершение работы...")
			break

		else:
			print("\nНеверный ввод!")
