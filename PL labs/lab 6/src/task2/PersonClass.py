class Person:
	count = 0

	def __init__(self):
		Person.count += 1
		print("Конструктор без параметров(Person) № " + str(Person.count))

	def __init__(self, name = "", age = 18, gender = "M"):
		Person.count += 1

		try:
			self.__name = name
			self.__age = int(age)
			self.__gender = gender
		except ValueError as err:
			print(err)

		print("Конструктор с параметрами(Person) № " + str(Person.count))


	def set_name(self, name):
		self.__name = name

	def set_age(self, age):
		self.__age = int(age)

	def set_gender(self, gender):
		self.__gender = gender


	def get_name(self):
		return self.__name

	def get_age(self):
		return self.__age

	def get_gender(self):
		return self.__gender


	def read(self):
		try:
			self.__name = input("Введите имя: ")
			self.__age = int(input("Введите возраст: "))
			self.__gender = input("Введите пол: ")
		except ValueError:
			print("Ошибка ввода")

	def print_info(self):
		print("Имя: {}, Возраст: {}, Пол: {}".format(
			str(self.__name)[:30],
			str(self.__age)[:10],
			str(self.__gender)[:10]
			))

	def __del__(self):
		print("Деструктор(Person) № " + str(Person.count))
		Person.count -= 1

