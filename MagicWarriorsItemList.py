import random
# TC = Treasure Class, higher = more rare, better
class RandomLoot:
    TC1ITEMLIST = []
    TC2ITEMLIST = []
    TC3ITEMLIST = []
    def __init__(self, item_name, lvl_req, attack_power, defense):
        self.item_name = item_name
        self.lvl_req = lvl_req
        self.attack_power = attack_power
        self.defense = defense
    def pick_Lootclass(self):
        TCs = ['EmptyLoot', 'TC1', 'TC2', 'TC3']
        probabilities = [0.4, 0.35, 0.2, 0.05]
        chosen_lootclass = random.choices(TCs, weights=probabilities, k=1)
        if chosen_lootclass == 'EmptyLoot':
            return None
        elif chosen_lootclass == 'TC1':
            rolled_item = random.choice(RandomLoot.TC1ITEMLIST)
            return rolled_item
        elif chosen_lootclass == 'TC2':
            rolled_item = random.choice(RandomLoot.TC2ITEMLIST)
            return rolled_item
        elif chosen_lootclass == 'TC3':
            rolled_item = random.choice(RandomLoot.TC3ITEMLIST)
            return rolled_item


