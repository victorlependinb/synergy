class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self,capacity=50):
        return f'Вместимость одного автобуса: {self.name} {capacity} пассажиров'

class Autobus(Transport):
     def vyvod(self):
        print(f'Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}')

a1=Autobus('Renaul Logan',180,12)
print(a1.seating_capacity())
