mt = int(input("Максимальная масса, которую могём: "))  
r = int(input("Колличество рыбаков ждунов: "))  
rybaky = []
while r>0:
    for i in range(r) :  
        i = int(input("Сколько этот весит: "))  
        if mt > i:  
            rybaky.append(i)
            r-=1
        else:    
            print("Не не не, этот тяжёлый, его не повезём!")  
            r-=1
rybaky.sort()   
odni = 0   
drugie = len(rybaky) - 1    
boat = 0    
while odni <= drugie:  
    if rybaky[odni] + rybaky[drugie] <= mt:  
        odni +=1       
    drugie -= 1  
    boat += 1   
print(f'Нам надо лодок: {boat}')  