spis = input('Введите через пробел числа : ')
chisla = map(int, spis.split())
seen = set()
for n in chisla:
    if n in seen:
        print("Число: ",n,"YES")
    else:
        print("Число: ",n,"NO")
        seen.add(n)