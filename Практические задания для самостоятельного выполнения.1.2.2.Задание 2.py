n = input("Введите пятизначное число: ")
list_of_digits = list(map(int, str(n)))
d=list_of_digits[3]
d1=int(d)
e=list_of_digits[4]
e1=int(e)
s=list_of_digits[2]
s1=int(s)
dt=list_of_digits[0]
dt1=int(dt)
t=list_of_digits[1]
t1=int(t)
c=((d1**5)*s1)/(dt1-t1)
print(c)