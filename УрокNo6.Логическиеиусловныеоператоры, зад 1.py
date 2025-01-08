n1=int(input("Введите N целых чисел: "))
#n1=0
n2=0

for i in range(n1):
    n=int(input())
    if n==0:
        n2+=1
print("Целых чисел, равных нулю: ",n2)    


# while n1>0:
#     n=int(input())
#     n1-=1
#     if n==0:
#         n2+=1
# else:
#     print(n2)