import functions

#ОБЪЯВЛЕНИЕ ВХОДНЫХ ДАННЫХ
universum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
A = [1, 3, 5, 6, 7, 8]
B = [2, 3, 4, 5, 8]
C = [1, 2, 3, 5, 6]

#ЗАДАНИЕ 1 - ПОСТРОИТЬ БУЛЕАН
boolean = functions.boolean(array = A)

#ЗАДАНИЕ 2 - СОРТИРОВКА СЛИЯНИЕМ
print("\nОСТСОРТИРОВАННОЕ МНОЖЕСТВО:\n")
print(functions.merge_sort(A + B))

#ЗАДАНИЕ 3 - РЕАЛИЗОВАТЬ ОПЕРАЦИЮ ПЕРЕСЕЧЕНИЯ МНОЖЕСТВ, ИСПОЛЬЗУЯ МАСКУ
functions.array_crossing(array1 = A, array2 = B, array3 = C, universum = universum)

#ЗАДАНИЕ 4 - НАЙТИ ПРЯМОЕ ПРОИЗВЕДЕНИЕ А х В И ЕГО МОЩНОСТЬ
functions.array_union(array1 = A, array2 = B)

#ЗАДАНИЕ 5 - ВЫЧИСЛИТЬ ПРОГРАММНО ВЫРАЖЕНИЕ СОГЛАСНО ВАРИАНТУ
print("РЕЗУЛЬТАТ ВЫЧИСЛЕНИЯ ВЫРАЖЕНИЯ:\n")
print(functions.lab_operation(array1 = A, array2 = B, array3 = C, universum = universum))

#ЗАДАНИЕ 7 - РЕАЛИЗОВАТЬ ПРОГРАММНО АЛГОРИТМ РАЗБИЕНИЯ МНОЖЕСТВ
functions.partition_output(array = [1, 6, 5, 7])

#ЗАДАНИЕ 8 - ПОСТРОИТЬ КОД ГРЕЯ ДЛЯ МНОЖЕСТВА
A = [1, 3, 5, 6, 7, 8]
functions.gray_code(array = [8])

