import random

def pl(t):
    for i in t:
        print(*i)



a = int(input("Введите X размера матрицы: ")) 
b = int(input("Введите Y размера матрицы: ")) 
 

matrix_1=[[random.randint(-50, 200) for _ in range(a)] for _ in range(b)]
matrix_2=[[random.randint(-50, 200) for _ in range(a)] for _ in range(b)]
matrix_3=[[0 for _ in range(a)] for _ in range(b)]


for i in range(len(matrix_3)):
    for j in range(len(matrix_3[0])):
        matrix_3[i][j]=matrix_1[i][j] + matrix_2[i][j]
print('-------matrix_1----------')
pl(matrix_1)
print('-------matrix_2----------')
pl(matrix_2)
print('-------matrix_3----------')
pl(matrix_3)
print('-------------------------')