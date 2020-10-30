#ОТНОШЕНИЯ

import funcs

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

R1 = funcs.get_R1(A)
R2 = funcs.get_R2(A)

#ЗАДАНИЕ 1
print("МАТРИЦА ОТНОШЕНИЙ R1")
print(funcs.matrix_build(R1, A))

print("МАТРИЦА ОТНОШЕНИЙ R2")
print(funcs.matrix_build(R2, A))

print("ОБРАТНОЕ ОТНОШЕНИЕ R1")
print(funcs.get_inverse_relation(R1))

print("ОБРАТНОЕ ОТНОШЕНИЕ R2")
print(funcs.get_inverse_relation(R2))

print("ДОПОЛНЕНИЕ ОТНОШЕНИЯ R1")
print(funcs.get_relation_addition(A, R1))

print("ДОПОЛНЕНИЕ ОТНОШЕНИЯ R2")
print(funcs.get_relation_addition(A, R2))

print("ТРАНЗИТИВНОЕ ЗАМЫКАНИЕ ОТНОШЕНИЯ R2")
print(funcs.get_transitive_closure(matrix = funcs.matrix_build(R2, A)))

print("КОМПОЗИЦИЯ ОТНОШЕНИЙ R1 И R2")
print(funcs.attitudes_composition([[1, 4], [5, 2], [6, 3], [4, 5]], [[4, 5], [3, 5], [5, 1], [3, 5]]))

print("КОМПОЗИЦИЯ ОТНОШЕНИЙ R2 И R1")
print(funcs.attitudes_composition([[4, 5], [3, 5], [5, 1], [3, 5]], [[1, 4], [5, 2], [6, 3], [4, 5]]))


#ФУНКЦИИ 

#ЗАДАНИЕ 1

B = [1, 2, 3, 4]
C = [5, 6, 7]
S = [[1, 5], [2, 7], [4, 7], [3, 6]]

print("ЯВЛЯЕТСЯ ЛИ ОТНОШЕНИЕ S ФУНКЦИЕЙ")
funcs.func_type(B, C, S)
  

print(1 & 0)
