#ЗАДАНИЕ 1

import funcs

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#ЗАДАНИЕ 1
print("МАТРИЦА ОТНОШЕНИЙ R1")
print(funcs.matrix_build(R = funcs.get_R1(A), array = A))

print("\n\n\nМАТРИЦА ОТНОШЕНИЙ R2")
print(funcs.matrix_build(R = funcs.get_R2(A), array = A))

#ЗАДАНИЕ 2
print("ОБРАТНОЕ ОТНОШЕНИЕ R1")
print(funcs.get_inverse_relation(R = funcs.get_R1(A)))

print("ОБРАТНОЕ ОТНОШЕНИЕ R2")
print(funcs.get_inverse_relation(R = funcs.get_R2(A)))

print("ДОПОЛНЕНИЕ ОТНОШЕНИЯ R1")
print(funcs.get_relation_addition(array = A, R = funcs.get_R1(A)))

print("ДОПОЛНЕНИЕ ОТНОШЕНИЯ R2")
print(funcs.get_relation_addition(array = A, R = funcs.get_R2(A)))

print("ТРАНЗИТИВНОЕ ЗАМЫКАНИЕ ОТНОШЕНИЯ R2")
print(funcs.get_transitive_closure(matrix = funcs.matrix_build(R = funcs.get_R2(A), array = A)))