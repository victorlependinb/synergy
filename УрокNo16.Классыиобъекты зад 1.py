class Kassa(object):
    summa = 0

    def __init__(self, s):
        self.summa = s

    def top_up(self):
        top=int(input("Введитет сколь пополнить: "))
        self.summa+=top

    def count_1000(self):
        print(self.summa//1000)

    def take_away(self):
        top_m=int(input("Введитет сколь снять: "))
        if self.summa>top_m:
            self.summa-=top_m
        else:
            print('Столько деняк нету')

kassa1=Kassa(10000)
kassa1.top_up()
kassa1.count_1000()
kassa1.take_away()