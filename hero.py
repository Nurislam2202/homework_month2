# Домашнее задание №1, Ураимов Нурислам

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def heros_name(self):
        print('\nимя героя:', self.name)

    def heros_health_points(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return (f"никнейм героя: {self.nickname}\nсуперспособность героя: {self.superpower}\n"
                f"здоровье героя: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Zakir Naik', 'Lion', 'supermemory', 100,
                 'brother/sister asked a good question')
print(hero.people)
hero.heros_name()
hero.heros_health_points()
print(hero)
print(len(hero))

yourHero = SuperHero(name=input('\nвведите имя героя: ').title(),
                     nickname=input("введите 'никнейм' героя: ").title(),
                     superpower=input('суперсила героя: '),
                     health_points=float(input('здоровье героя: ')),
                     catchphrase=input('коронная фраза героя: '))
yourHero.heros_name()
yourHero.heros_health_points()
print(yourHero)
print(len(yourHero))

while True:
    question = input("\nхотите повторить? (введите 'да' или 'нет')\n"
                     "shall we repeat? (enter 'yes' or 'no'): ")
    if question == 'да' or question == 'yes':
        yourHero = SuperHero(name=input('\nвведите имя героя: ').title(),
                             nickname=input("введите 'никнейм' героя: "),
                             superpower=input('суперсила героя: '),
                             health_points=float(input('здоровье героя: ')),
                             catchphrase=input('коронная фраза героя: '))
        yourHero.heros_name()
        yourHero.heros_health_points()
        print(yourHero)
        print(len(yourHero))
    elif question == 'нет' or question == 'no':
        break
    else:
        print("\nвведите только 'да' или 'нет'!\n"
              "enter only 'yes' or 'no'!")
        continue


class AirSuperHero(SuperHero):
    cloak = 'have'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def new_heros_health_points(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def new_phrase(self):
        print("фраза: 'True in the True_phrase'")

    def __str__(self):
        return f"{super().__str__()}\nумение летать: {self.fly}"


class SpaceSuperHero(SuperHero):
    cloak = "don't have"

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def new_heros_health_points(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def new_phrase(self):
        print("фраза: 'True in the True_phrase'")

    def __str__(self):
        return f"{super().__str__()}\nумение летать: {self.fly}"


newHero = AirSuperHero('Kane', 'Airman', 'fly', 100,
                       'faster than the wind', 70)
newHero.heros_name()
newHero.new_heros_health_points()
print(newHero)
print(f'длина коронный фразы героя: {len(newHero)}')
print(f'плащ: {newHero.cloak}')
print(f'урон: {newHero.damage}')
newHero.new_phrase()

newHero2 = SpaceSuperHero('Galaxy', 'SpaceHero', 'teleport', 100,
                          'to infinity and beyond', 100)
newHero2.heros_name()
newHero2.new_heros_health_points()
print(newHero2)
print(f'длина коронный фразы героя: {len(newHero2)}')
print(f'плащ: {newHero2.cloak}')
print(f'урон: {newHero2.damage}')
newHero2.new_phrase()


class Villian(AirSuperHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)

    def gen_x(self): ...

    def crit(self):
        self.damage = self.damage ** 2

    def new_phrase(self):
        pass


monster1 = Villian('Mike', 'rhinoceros', 'power', 100, 'AAGGGHHHH',
                   90)
monster1.crit()
monster1.new_phrase()
monster1.heros_name()
monster1.new_heros_health_points()
print(monster1)
print(f'длина коронный фразы злодея: {len(monster1)}')
print(f'урон: {monster1.damage}')
