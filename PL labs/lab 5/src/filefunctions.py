import csv
import operator

def get_students_info():
	with open('students_info.csv', 'r') as file:
		students_info = csv.DictReader(file, delimiter = ';')
		return list(students_info)

def print_students_info(students_info):
	for i in range(len(students_info) - 1):
		for j in range(len(students_info) - i - 1):
			if students_info[j]['Возраст'] > students_info[j + 1]['Возраст']:
				students_info[j], students_info[j + 1] = students_info[j + 1], students_info[j]

	for student in students_info:
		print([student['№'], student['ФИО'], student['Возраст'], student['Группа']])

def decrement(students_info):
	for i in range(len(students_info)):
		students_info[i]['Возраст'] = int(students_info[i]['Возраст']) - 1


def update(students_info):
	with open('students_info.csv', 'w', newline = '') as file:
		writer = csv.DictWriter(file, delimiter = ';', fieldnames = ['№', 'ФИО', 'Возраст', 'Группа'])
		writer.writeheader()
		for student_info in students_info:
			writer.writerow(student_info)

