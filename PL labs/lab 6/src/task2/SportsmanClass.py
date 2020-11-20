from PersonClass import Person

class Sportsman(Person):
	count = 0

	def __init__(self):
		Sportsman.count += 1
		print("Конструктор по умолчанию(Sportsman) № " + str(Sportsman.count))

	def __init__(self, name = "", age = 18, gender = "M", sport = ""):
		Sportsman.count += 1

		try:
			super(Sportsman, self).__init__(name, age, gender)
			self.__sport = sport
		except ValueError as err:
			print(err)

		print("Конструтор с параметрами(Sportsman) № " + str(Sportsman.count))


	def set_sport(self, sport):
		self.__sport = sport

	def get_sport(self):
		return self.__sport


	def read(self):
		try:
			self.__name = input("Введите имя: ")
			self.__age = int(input("Введите возраст: "))
			self.__gender = input("Введите пол: ")
			self.__sport = input("Введите спорт: ")
		except ValueError:
			print("Ошибка ввода")

	def print_info(self):
		print("Имя: {}, Возраст: {}, Пол: {}, Спорт: {}".format(
			str(self.__name)[:30],
			str(self.__age)[:10],
			str(self.__gender)[:10],
			str(self.__sport)[:20]
			))

	
	def __del__(self):
		print("Деструктор(Sportsman) № " + str(Sportsman.count))
		Sportsman.count -= 1


if __name__ == "__main__":
	sc = Sportsman()
	sc.read()
	sc.print_info()

