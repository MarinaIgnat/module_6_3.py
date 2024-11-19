import random

class Animal:
    live = True
    sound = None        # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0   # степень опасности существа

    def __init__(self, cords, speed):
        self._cords = cords
        _cords = [0, 0, 0]      #координаты в пространстве
        self.speed = speed     #скорость передвижения существа(определяется при создании объекта)

        
    def move(self, dx, dy, dz):        #изменение соответствующих координат в _cords
        _cords_2 = [dx, dy, dz]
        for i in self._cords:
            if i * self.speed:
                _cords = _cords_2
            elif _cords_2[2] < 0:
                _cords_2[2] = _cords[2] and print("It's too deep, i can't dive :(")


    def get_cords(self):
        return f'X: {self.dx}, {self.dy}, {self.dz}'

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):      #класс описывающий птиц
    beak = True        #наличие клюва

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):   #класс описывающий плавающего животного

    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dz = abs(self._cords) * self.speed / 2


class PoisonousAnimal(Animal):   #класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal): #класс описывающий утконоса
    sound = "Click-click-click"     #звук, который издаёт утконос

    #def __init__(self, _):
        #super().move()
        #super().attack()


db = Duckbill(10, 5)

print(db.live)
print(db.beak)

#db.speak()

#db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()


















