import task2

def interface(students_info_list):
	while True:
		choice = int(input("Выберите действие(1 - Вывести всех студентов, 2 - Уменьшить возраст всех студентов, 3 - Выход): "))
		if choice == 1:
			task2.print_students_info(students_info_list)

		elif choice == 2:
			for i in range(len(students_info_list)):
				students_info_list[i][2] = str(int(students_info_list[i][2]) - 1)

			with open('studetns_info.txt', 'w', encoding = 'utf-8') as students_info:
				for student in students_info_list:
					students_info.write(';'.join(student) + '\n')


			for student in students_info_list:
				print(student)

		elif choice == 3:
			print("Завершение работы...")
			break

		else:
			print("Неверный ввод")

interface(task2.get_students_info_list())