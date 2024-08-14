# Домашнее задание №1, Ураимов Нурислам

class SuperHero:
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def heros_name(self):
        print('имя героя:', self.name)

    def heros_health_points(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return (f"никнейм героя: {self.nickname}\nсуперспособность героя: {self.superpower}\n"
                f"здоровье героя: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Zakir Naik', 'Lion', 'supermemory', 100,
                 'brother/sister asked a good question')
hero.heros_name()
hero.heros_health_points()
print(hero)
print(len(hero))

yourHero = SuperHero(name=input('введите имя героя: ').title(),
                     nickname=input("введите 'никнейм' героя: "),
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
        yourHero = SuperHero(name=input('введите имя героя: ').title(),
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
