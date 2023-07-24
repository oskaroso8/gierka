import random


class Char:
    def __init__(self, name, stre, dex, intel, exp, lvl, hitpoints, skillpoints, statpoints):
        self.name = name
        self.stre = stre
        self.dex = dex
        self.int = intel
        self.exp = exp
        self.lvl = lvl
        self.hitpoints = hitpoints
        self.skillpoints = skillpoints
        self.statpoints = statpoints


    def exp_lvl_up(self):
        global difficulty
        if difficulty == "Hard":
            self.exp += 10
        elif difficulty == "Medium":
            self.exp += 2
        elif difficulty == "Easy":
            self.exp += 1
        if self.exp >= 10:
            self.exp = 0
            self.lvl += 1
            self.skillpoints += 1
            self.statpoints += 3
            print(f"""
Congrats! You've just leveled up to level: {self.lvl}!
You have {self.skillpoints} skillpoints and {self.statpoints} statpoints!
                 """)
        return

    def character_info(self, skillpoints, statpoints):
        print(f'You are {self.name} lvl {self.lvl} {self.exp}exp')
        if self.skillpoints > 0:
            print(f'You have {skillpoints} skillpoints to spend!')
        if self.statpoints > 0:
            print(f'You have {statpoints} statpoints to spend!')


class Enemy(Char):
    def __init__(self, name, stre, dex, intel, lvl, hitpoints):
        super().__init__(name, stre, dex, intel, 0, lvl, hitpoints, 0, 0)

    @staticmethod
    def pick_random():
        enemy_list = [mag, war, archer, zombie]
        enemy = random.choice(enemy_list)
        return enemy

    def fight_random(self, champion):
        while self.hitpoints > 0 and champion.hitpoints > 0:
            x = input(f"""choose skill to attack with
fireball
                """)
            if x == 'fireball':
                print(f'zadajesz 5 obrazen, przeciwnik ma teraz {self.hitpoints - 5} hp!')
                self.hitpoints = self.hitpoints - 5
        if self.hitpoints <= 0:
            print(f'gratulacje, pokonujesz {self.name}, zdobywasz x expa i item!')
            return 'win'
        elif champion.hitpoints <= 0:
            print(f"Przegrywasz z {self.name} mozesz okryc sie hanba!")
            return 'lose'


class Skills:
    def __init__(self):
        ...

    def skill(self, stre, dex, intel):
        if player == mag:
            print(f'You shot your fireball and deal {3 + (0.5 * intel)} damage!')
        elif player == war:
            print(f'You hit with your tremendous axe and deal {2 + (0.4 * stre)} damage!')
        elif player == archer:
            print(f'You shot your incredible bow and deal {2 + (0.5 * dex)} damage')


class Loot:
    def __init__(self, item_name, lvl_req, attack_power, defense):
        self.item_name = item_name
        self.lvl_req = lvl_req
        self.attack_power = attack_power
        self.defense = defense


class LootTable:
    ...


def print_intro_pick_champ():
    while True:
        champion = input("""
    Welcome to the 'Magic Warriors' game!
    Pick your champion:
    Warrior - powerful muscles, specializes specializes in combat with an axe
    Archer - very fast, shots arrow from bow
    Mage - op asf, throws fireballs and other shit
    """)
        if champion.capitalize() == "Warrior":
            print("nice you are warrior now")
            return war
        elif champion.capitalize() == "Archer":
            return archer
        elif champion.capitalize() == "Mage":
            print("nice you are mage!! now you can go on and fight enemies, get stronger and richer!")
            return mag
        print("choose correct champion!")


def choose_difficulty():
    global difficulty
    while True:
        difficulty = input("Choose your difficulty: Easy Medium or Hard")
        if difficulty.capitalize() in ['Easy', 'Medium', 'Hard']:
            return difficulty.capitalize()
        else:
            print('Type in a correct difficulty')


def main_game_logic():
    champion = print_intro_pick_champ()
    global difficulty
    difficulty = choose_difficulty()
    while True:
        Char.character_info(champion, champion.skillpoints, champion.statpoints)
        decision = input(f"""
Write:
fight 
sks (skills and stats)
shop 
difficulty (current: {difficulty})
close
""")
        if decision == 'fight':
            enemy = Enemy.pick_random()
            print(f'your enemy is {enemy.name, enemy.hitpoints}hp')
            result = Enemy.fight_random(enemy, champion)
            if result == 'win':
                Char.exp_lvl_up(champion)
        elif decision == 'sks':
            print('here you can spend your skillpoints and statpoints')
        elif decision == 'difficulty':
            difficulty = choose_difficulty()
        elif decision == 'close':
            print('closing the game, see you again!')
            break
        else:
            print('Type in a correct command!')


if __name__ == '__main__':
    mag = Char('Mage', 2, 4, 10, 0, 1, 10, 0, 0)
    war = Char('Warrior', 10, 4, 2, 0, 1, 15, 0, 0)
    archer = Char('Archer', 2, 10, 4, 0, 1, 12, 0, 0)
    zombie = Enemy('Zombie', 5, 1, 0, 1, 20)
    main_game_logic()
