def fact(n):
    n3 = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            n3 *= i 
        return n3  
n=int(input("Введите число: "))
n2=[]
n4=fact(n)

for i in range(1, n4+1):
    n5=fact(i)
    n2.append(n5)
n2.reverse()
print(n2)   