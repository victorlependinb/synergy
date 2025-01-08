# -*- coding: utf-8 -*-
from curses.ascii import isdigit
petscol = []
def read():  
    pet = input("Введите ID питомца или имя: ")
    pet1=0
    pet2=''
    print("Ваш питомец")  
    print("---------------")  
    eto=False

    if pet.isdigit()==True:
        pet1=int(pet)
        if (pet1>0):
            for person in petscol:
                if person['ID'] == pet1:
                    eto=True
                    print(f'ID питомца: {person["ID"]}, имя: {person["имя"]}, вид: {person["вид"]}, возраст: {suffix(person["возраст"])}, владелец: {person["владелец"]}')
                    return
            if eto==False:
                print("Питомец с таким ID не найден.")
                print("---------------")  
                return
    else:
        pet2=pet
        for person in petscol:
            if person['имя'] == pet2:
               eto=True
               print(f'ID питомца: {person["ID"]}, имя: {person["имя"]}, вид: {person["вид"]}, возраст: {suffix(person["возраст"])}, владелец: {person["владелец"]}')
               return
        if eto==False:
            print("Питомец с таким именем не найден.") 
            print("---------------")   
            return

def create(): 
    print('Введите информацию о питомце') 
    name, species, age, owner_name=pet_input()
    new_id = len(petscol) + 1 
    pets1 = {'ID':new_id,'имя': name, 'вид': species, 'возраст': age, 'владелец': owner_name}
    petscol.append(pets1)

def suffix(age):  
    if 11 <= age % 100 <= 14:  
        return f"{age} лет"  
    elif age % 10 == 1:  
        return f"{age} год"  
    elif age % 10 in [2, 3, 4]:  
        return f"{age} года"  
    else:  
        return f"{age} лет"  

def delete(): 
    print("---------------")  
    pet = input("Введите ID питомца: ")
    if pet.isdigit()==True:
        pet1=int(pet)
        if len(petscol)>=pet1:
            #pet1=int(pet)
            for person in petscol:
                if person['ID'] == pet1:
                    petscol.remove(person)
                    print(f"Питомец с ID {pet} удален.")  
                    print("---------------")  
                    return                                                                     
        elif pet>len(petscol):  
            print("Питомец с таким ID не найден.") 
            print("---------------")  
            return
        else:
            if len(petscol)==0:
                print("В списке нет питомцев")
                print("---------------")  
                return
    else:
        print("ID можно только числом!")
        print("---------------")  
        return


def update():  
    pet = int(input("Введите ID питомца: ")) 
    pet1=pet-1
    if len(petscol)>=pet:
        name, species, age, owner_name=pet_input()
        pets1 = {'ID':pet,'имя': name, 'вид': species, 'возраст': age, 'владелец': owner_name}
        petscol[pet1]=pets1
        print(f"Информация о питомце с ID {pet} обновлена.") 
        print("---------------")  
    elif pet>len(petscol): 
        print(f"Питомец с ID {pet} не найден.")  
        print("---------------")  

def pet_input():  
        name = input('Введите имя питомца: ')  
        species = input('Введите вид питомца: ')
        owner_name = input('Введите владельца питомца: ')
        while True:
            age1 = input('Введите возраст питомца: ')
            if age1.isdigit()==True:
                age=int(age1)
                return name, species, age, owner_name
            else:
                print('Возраст нужно ввести числом!')
                print("---------------")  

def allpet():  
    if len(petscol)>0:
        print("Вcе наши питомцы")  
        print("---------------")  
        for person in petscol:
            print(f'ID питомца: {person["ID"]}, имя: {person["имя"]}, вид: {person["вид"]}, возраст: {suffix(person["возраст"])}, владелец: {person["владелец"]}')
    else:
        print('Список пуст!')
        print("---------------")  

while True:  
    print('Список команд: ')
    print('create - созадть')
    print('read - найти')
    print('delete - удалить')
    print('update - обновить')
    print('allpet - вывести всех')
    command = input("Введите команду (или 'stop' для выхода) : ")  
    if command.lower() == 'stop':  
        print("Команда 'stop' получена. Завершение программы.")  
        break  

    if command == 'create':  
        create()  
    elif command == 'read':  
        read()
    if command == 'delete':  
        delete()  
    if command == 'update':  
         update()  
    if command == 'allpet':  
         allpet()  
