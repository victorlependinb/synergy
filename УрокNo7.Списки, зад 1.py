n = int(input("Введите количество чисел >=1 и <=1000000 "))
list = []
for i in range(n):
    a = int(input("Введите значение болше 1, и меньше 10000: "))
    list.append(a)
list.reverse()
print(list)