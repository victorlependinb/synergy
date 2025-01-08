c1=int(input("Колличество в первом списке: "))
c2=int(input("Колличество во втором списке: "))
cl1=[]
cl2=[]
for i in range(c1):
    d2=int(input("Число для первого списака: "))
    cl1.append(d2)
for i in range(c2):
    d3=int(input("Число для второго списака: "))
    cl2.append(d3)  

cl3=set(cl1)
cl4=set(cl2)

odinakov = cl3.intersection(cl4)
print("Колличество одинаковых чисел: ",len(odinakov))
print("Список одинаковых чисел: ",odinakov)