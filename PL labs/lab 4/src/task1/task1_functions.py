# Функция выводит решенный пример
def print_expression_result(a, b, c, d, k):
	if (b != 0 and a != 0):
		print("Результат вычисления выражения:")
		print( abs(((a**2 - b**3 - c**3 * a**2 ) * (b - c + c*(k - d/b**3)) - (k/b - k/a)*c)**2 - 20000) )
	else:
		print("На ноль делить нельзя")

#Функция выводит нечетные элементы списка
def print_odd_elements(lst):
	for element in lst:
		if (type(element) is float or type(element) is int) and element % 2 != 0:
			print(element)

#Функция возвращает результат сложения всех чисел списка от 1 до 10
def get_calculate_result(lst):
	calculate_result = 0

	for element in lst:
		if( element >= 1 and element <= 10):
			calculate_result += element

	return calculate_result

