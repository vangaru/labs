import task2

def interface(students_info_list):
	while True:
		choice = int(input("Выберите действие(1 - Вывести всех студентов, 2 - Уменьшить возраст всех студентов, 3 - Выход): "))
		if choice == 1:
			task2.print_students_info(students_info_list)

		elif choice == 2:
			for i in range(len(students_info_list)):
				students_info_list[i][2] = int(students_info_list[i][2]) - 1

			for student in students_info_list:
				print(student)

		elif choice == 3:
			print("Завершение работы...")
			break

		else:
			print("Неверный ввод")

interface(task2.get_students_info_list())