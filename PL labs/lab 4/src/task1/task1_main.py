import task1_functions

print("\nЗАДАНИЕ 1 ПУНКТ 1")
print("Решить пример по варианту")

print("\nВвод данных")

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
d = float(input('Введите d: '))
k = float(input('Введите k: '))

functions.print_expression_result(a, b, c, d, k)

####################################################################

print("ЗАДАНИЕ 1 ПУНКТ 2")
print("Дан произвольный список, содержащий строки и числа")
print("Вывести все нечетные элементы построчно")

lst = [1, "PY", "TH", 4, "ON"]
print("\nИзначальный список: " + str(lst))
print("Нечетные элементы данного списка:")
functions.print_odd_elements(lst)

####################################################################

print("\n\nЗАДАНИЕ 1 ПУНКТ 3")
print("Дан произвольный список, содержащий только числа")
print("Вывести результат сложения всех чисел от 1 до 10")

lst = [1, 15, -5, 26, 5, 9, 10]
print("\nИзначальный список: " + str(lst))
print("Результат сложения всех чисел от 1 до 10: " + str(functions.get_calculate_result(lst)))

####################################################################

print("\n\nЗАДАНИЕ 1 ПУНКТ 4")
print("Дан произвольный список, содержащий только числа")
print("Вывести минимальное число")
print("\nИзначальный список: " + str(lst))
print("Минимальное число: " + str(min(lst)))