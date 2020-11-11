import filefunctions

def interface(students_info):
	while True:
		choice = int(input("Выберите действие(1 - Вывести всех студентов, 2 - Уменьшить возраст всех студентов, 3 - Выход): "))
		if choice == 1:
			filefunctions.print_students_info(students_info)

		elif choice == 2:
			filefunctions.decrement(students_info)
			filefunctions.update(students_info)

		elif choice == 3:
			print("Завершение работы...")
			break

		else:
			print("Неверный ввод")


students_info = filefunctions.get_students_info()
interface(students_info)
