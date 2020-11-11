import csv

with open('students_info.csv', 'r', encoding = 'utf-8') as file:
	reader = csv.DictReader(file, delimiter = ';')
	for line in reader:
		print ([line["№"], line["ФИО"], line["Возраст"], line["Группа"]])
