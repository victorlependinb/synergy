palindrom = input("Введите слово для проверки: ")
if palindrom == palindrom[::-1]:
    print("yes")
else:
    print("no")