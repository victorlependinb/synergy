class Cherep(object):
    y=0
    x=0
    s=1

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def go_up(self):
        self.y+=self.s

    def go_down(self):
        self.y-=self.s

    def go_left(self):
        self.x-=self.s

    def go_right(self):
        self.x+=self.s

    def evolve(self):
        self.s+=1

    def degrade(self):
        if (self.s-1)>0:
            self.s-=1
        else:
            print('Ошибка')

    def count_moves(self):
        x1=int(input("Введитет новые координаты координаты X: "))
        y1=int(input("Введитет новые координаты координаты Y: "))
        x2=(x1-self.x)//self.s
        y2=(y1-self.y)//self.s
        s1=x2+y2
        print(f'Минимальное количество действий чтобы добраться от текщей позиции: ', s1-3)

    def gdeya(self):
        x1=self.x
        y1=self.y
        print(f'Я сейчас тут: ', x1,y1)

        


cherep1=Cherep(0,0)
cherep1.go_up()
cherep1.go_up()
cherep1.go_up()
cherep1.go_right()
cherep1.go_right()
cherep1.go_right()
cherep1.go_right()

cherep1.gdeya()
cherep1.count_moves()