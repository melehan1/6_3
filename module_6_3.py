class Horse:
    def __init__(self):
        x_distance = 0
        self.x_distance = x_distance
        self.sound = 'Frrr'

    def run(self, dx):  # где dx - изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    def __init__(self):
        y_distance = 0
        self.y_distance = y_distance  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):  # изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy


class Pegasus(Horse, Eagle):  # В этом методе должны запускаться наследованные методы run и fly соответственно
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(
            self):  # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        return (self.x_distance, self.y_distance)

    def voice(self):  # печатает значение унаследованного атрибута sound
        print(self.sound)


print(Pegasus.mro())
p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
