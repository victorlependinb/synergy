class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
     def vyvod(self):
        print(f'Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}')

a1=Autobus('Renaul Logan',180,12)
a1.vyvod()