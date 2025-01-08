pitomsy = dict()  
pitom_n = input("Имя питомца: ")  
pitom_vid = input(f"Введите вид питомца {pitom_n}: ")  
pitom_age = int(input(f"Введите возраст питомца {pitom_n}: "))  
pitom_user = input(f"Введите владельца питомца {pitom_n}: ")  
if pitom_age % 10 == 1 and pitom_age % 100 != 11:  
    age = "год"  
elif pitom_age % 10 in [2, 3, 4] and not (pitom_age % 100 in [12, 13, 14]):  
    age = "года"  
else:  
    age = "лет"  
pet_info = {  
    "Вид питомца ": pitom_vid,  
    "Возраст питомца ": f"{pitom_age} {age}",  
    "Владелец питомца ": pitom_user  
}  
pitomsy[pitom_n] = pet_info  
print(pitomsy)