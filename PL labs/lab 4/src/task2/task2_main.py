from random import randint
import task2_functions

print("\nЗАДАНИЕ 2 ПУНКТ 1")
print("Пусть задано некоторое число my_number. Пользователь вводит свое число user_number.")
print("Запрашивайте у пользователя user_number до")
print("тех пор, пока оно не будет равно my_number")

my_number = randint(1, 10)
print("\nЧисло my_number: " + str(my_number))
functions.ask_user_number(my_number)

####################################################################

print("\n\nЗАДАНИЕ 2 ПУНКТ 2")
print("Пусть задан список, содержащий строки")
print("Выведите построчно все строки размером менее 10 символов\n")

lst = ["Python", "Laravel", "The Last OF Us 2", "Django", "Dragon Age Origins", "Fallout New Vegas", "PHP"]
print("Изначальный список: " + str(lst))
print("Полученные строки:")
functions.get_list_line(lst)

####################################################################

print("\n\nЗАДАНИЕ 2 ПУНКТ 3")
print("Сгенерируйте и выведите:")
print("Строку размером N и состоящую из букв R\n")

N = int(input("Введите N: "))
print("Полученная строка: " + functions.get_R_line(N))

####################################################################

print("\n\nЗАДАНИЕ 2 ПУНКТ 4")
print("Пусть дана строка")
print("На основе данной строки сформируйте новую, содержащую только буквы")

string = "ffhuh43f84309fj3f349f";
print("\nИзначальная строка: " + string)
print("Полученная строка: " + functions.remove_digits(string))
