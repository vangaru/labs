class Graduate:
	count = 0

	def __init__(self):
		Graduate.count += 1
		print("Количество объектов: " + str(Graduate.count))

	def __init__(self, name = "", university = "", year = 0):
		Graduate.count += 1

		try:
			self.__name = name
			self.__university = university
			self.__year = int(year)
		except ValueError as err:
			print(err)

		print("Количество объектов: " + str(Graduate.count))


	def set_name(self, name):
		self.__name = name

	def set_university(self, university):
		self.__university = university

	def set_year(self, year):
		self.__year = int(year)


	def get_name(self):
		return self.__name

	def get_university(self):
		return self.__university

	def get_year(self):
		return self.__year


	def read(self):
		try:
			self.__name = str(input("Введите имя выпускника: "))
			self.__university = str(input("Введите название университета: "))
			self.__year = int(input("Введите год выпуска: "))
		except ValueError:
			print("Ошибка ввода")

	def print_info(self):
		print("Имя студента: {}, Название университета: {}, Год выпуска: {}".format(
			str(self.__name)[:30], 
			str(self.__university)[:30], 
			str(self.__year)[:5]
			))

	def print_file(self):
		with open("info.txt", "a") as file:
			file.write(str(self.get_name()) + " " + str(self.get_university()) + " " + str(self.get_year()) + "\n")

	def __del__(self):
		print("Вызвалася деструктор для " + str(Graduate.count) + " объекта")
		Graduate.count -= 1



if __name__ == "__main__":
	graduate1 = Graduate()
	graduate1.read()
	graduate1.print_file()

	graduate2 = Graduate("Vladislav", "BSU", "2019")
	graduate2.print_file()

	graduate1.print_info()
	graduate2.print_info()






