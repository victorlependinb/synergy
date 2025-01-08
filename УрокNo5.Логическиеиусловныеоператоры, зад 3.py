inv0=int(input("Введите сколько у майкла: "))
inv1=int(input("Введите сколько у ивана: "))
inv2=int(input("Введите минимум: "))

if inv0>=inv2 and inv1>=inv2:
    print("И тот и тот")
else:
    if inv0>=inv2 and inv1<=inv2:
        print("Майкл")
    elif inv0<=inv2 and inv1>=inv2:
        print("Иван")
    elif (inv0 or inv1 < inv2) and ((inv0+inv1)>inv2):
        print("только вместе")
    else: 
        if (inv0 or inv1 < inv2) and ((inv0+inv1)<inv2):
            print("никто")