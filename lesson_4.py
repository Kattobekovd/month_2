from random import randint,choice

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value


    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value


    def __str__(self):
        return f'{self.__name} health: {self.__health} Damage {self.__damage}'

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if (type(hero) == Berserk and
                        self.defence !='BLOCK_DAMAGE_AND_REVERD'):
                    blocked = randint(1, 2) * 5  # 5 , 10
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage




    def choose_defence(self, heroes):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def __str__(self):
        return 'BOSS' + super().__str__() + f'defence {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass

class Berserk(Hero):
    def __init__(self, name, health, damage,):
        super().__init__(name, health, damage,'BLOCK_DAMAGE_AND_REVERD')
        self.__blocked_Damage = 0
    @property
    def blocked_damage(self):
        return self.__blocked_Damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_Damage = value

    def apply_super_power(self, boss, heroes):
        #ЗДесь будет реализация CRIRTICAL DAMAGE
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage} to boss.')


class Warrior(Hero):
    def __init__(self, name, health, damage,):
        super().__init__(name, health, damage,'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes ):
        #ЗДесь будет реализация CRIRTICAL DAMAGE
        random_cpefficient = randint(2,5 ) #2,3,4,5
        boss.health -= self.damage * random_cpefficient
        print(f'Warrior {self.name} hit criticaly {self.damage * random_cpefficient}.')

class Magic(Hero):
    def __init__(self, name, health, damage,):
        super().__init__(name, health, damage,'Boost')

    def apply_super_power(self, boss, heroes):
         # ЗДесь будет реализация Boost
         pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage,'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
         # ЗДесь будет реализация Boost
         for hero in heroes:
             if hero.health > 0 and self != hero:
                 hero.health += self.__heal_points

class Witcher(Hero):
    def __init__(self, name, health, damage,):
        super().__init__(name, health, damage,'REVIVE')
        self.__has_revived = False

    def apply_super_power(self, boss, heroes):
        if not self.__has_revived:
            for hero in heroes:
                if hero.health <= 0:
                    hero.health = self.health
                    self.health = 0
                    self.__has_revived = True
                    print(f'Witcher {self.name} revived {hero.name} and sacrificed himself.')
                    break

class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'HACK')

    def apply_super_power(self, boss, heroes):
        health_stolen = randint(1, 20)  # Steal 1 to 20 health points
        boss.health -= health_stolen
        hero_to_heal = choice(heroes)
        hero_to_heal.health += health_stolen
        print(f'Hacker {self.name} stole {health_stolen} health from boss and gave it to'
              f' {hero_to_heal.name}.')

class Kamikadze(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, 0, 'SACRIFICE')

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            damage = self.health
            if randint(0, 1):  # 50% шанс попасть точно
                boss.health -= damage
                print(f'Kamikadze {self.name} hit the boss and sacrificed himself dealing {damage} damage.')
            else:
                boss.health -= damage // 2
                print(f'Kamikadze {self.name} missed and only dealt {damage // 2} damage.')
            self.health = 0

class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'SHURIKEN')

    def apply_super_power(self, boss, heroes):
        shuriken_type = choice(['virus', 'vaccine'])
        if shuriken_type == 'virus':
            damage = randint(10, 30)  # Вред наносит N-е количество урона
            boss.health -= damage
            print(f'Samurai {self.name} hit the boss with a virus shuriken dealing {damage} damage.')
        else:
            heal = randint(10, 30)  # Вакцина лечит на N-е количество здоровья босса
            boss.health += heal
            print(f'Samurai {self.name} hit the boss with a vaccine shuriken healing {heal} health.')

round_number = 0

def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!')
        return True
    return False

def show_statistics(boss, heroes):
    print(f'ROUND - {round_number} ----------------')
    print(boss)
    for hero in heroes:
        print(hero)

def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if (hero.health > 0 and boss.health > 0
                and hero.ability != boss.defence):
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)

def start_game():
    boss = Boss(' Diablo', 1000,  50)
    warrior_1 = Warrior('Rubi', 280, 10)
    warrior_2 = Warrior('Reksar', 270, 15)
    magic = Magic('Hendolf', 290, 10)
    berserk = Berserk('Guts', 260, 5)
    doc = Medic('Jojo', 250, 5, 15)
    assistant = Medic('Lily', 300, 5, 5)
    witcher = Witcher('Roxi', 200, 0)
    hacker = Hacker('Sid', 240, 5)
    kamikadze = Kamikadze('Daki', 300)
    samurai = Samurai('Hattori', 280, 10)

    heroes_list = [warrior_1, warrior_2, doc, magic, berserk, assistant,
                   witcher, hacker, kamikadze, samurai]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()










