def get_students_info_list():
	with open('studetns_info.txt', 'r', encoding = 'utf-8') as students_info:
		students_info_list = (students_info.read().splitlines())
		for i in range(len(students_info_list)):
			students_info_list[i] = students_info_list[i].split(";")
	return students_info_list


def print_students_info(students_info_list):
	for i in range(len(students_info_list) - 1):
		for j in range(len(students_info_list) - i - 1):
			if students_info_list[j][2] > students_info_list[j + 1][2]:
				students_info_list[j], students_info_list[j + 1] = students_info_list[j + 1], students_info_list[j]

	for student in students_info_list:
		print(student)


	