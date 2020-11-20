from SportsmanClass import Sportsman

class PrizeWinner(Sportsman):
	count = 0

	def __init__(self):
		PrizeWinner.count += 1
		print("Конструтор без параметров(PrizeWinner) № " + str(Sportsman.count))

	def __init__(self, name = "", age = 18, gender = "M", sport = "", place = 1):
		PrizeWinner.count += 1

		try:
			super(PrizeWinner, self).__init__(name, age, gender, sport)
			self.__place = int(place)
		except ValueError as err:
			print(err)

		print("Конструтор с параметрами(PrizeWinner) № " + str(Sportsman.count))

	
	def set_place(self, place):
		self.__place = int(place)

	def get_place(self):
		return self.__place


	def read(self):
		try:
			self.__name = input("Введите имя: ")
			self.__age = int(input("Введите возраст: "))
			self.__gender = input("Введите пол: ")
			self.__sport = input("Введите спорт: ")
			self.__place = int(input("Введите место: "))
		except ValueError:
			print("Ошибка ввода")

	def print_info(self):
		print("Имя: {}, Возраст: {}, Пол: {}, Спорт: {}, Место: {}".format(
			str(self.__name)[:30],
			str(self.__age)[:10],
			str(self.__gender)[:10],
			str(self.__sport)[:20],
			str(self.__place)[:10]
			))

	def __del__(self):
		print("Деструктор(Sportsman) № " + str(PrizeWinner.count))
		PrizeWinner.count -= 1


