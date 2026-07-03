import random, time
from weapons import Weapons, get_ammo
from ranks import Ranks, init_evasion_calc
from weapons.shoot_action import shoot_dmg_calc


class Ranged_Player: # Make function that uses input() to take weapon choice # Remember time.sleep() as well for turn simulation
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank # I could make this an enum to ensure it's validity
        self.evasion = init_evasion_calc(rank)
        self.tatical_reload_evasion_modifier = False # Adds a temp +1 evasion boost and reload in exchange for skipping a turn

    def shoot(self, target):
        shoot_dmg_calc(self, target)
    
    def reload(self): # I could use this as a "defensive" action, where the player reloads and gains a temporary evasion boost
        raise NotImplementedError("Will be implemented by Ranged_Player subclasses") # SA1216 sucks
    
    def __repr__(self):
        return f"Ranged_Player(name={self.name}, rank={self.rank}, self.evasion={self.evasion})"

class Melee_Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.evasion = init_evasion_calc(rank)
        self.in_melee_range = False # This will balance out the higher evasion and damage of melee weapons. Will add "move in" function that sets this to True, and takes up a turn.
        self.melee_rep_count = 0
        self.alt_stance = False

    def move_in(self, target):
        time.sleep(1)
        self_situational_movement_modifier = random.randint(-2, 2) # This will add some variability to the move in action
        target_situational_movement_modifier = random.randint(-2, 2)
        if (self.evasion + self_situational_movement_modifier) > (target.evasion + target_situational_movement_modifier):
            self.in_melee_range = True
            print(f'{self.name} is now in range! Let the beatdown commence!')

    def main_melee(self, target):
        raise NotImplementedError("Will be implemented by Melee_Player subclasses")
    
    def alt_melee(self):
        raise NotImplementedError("Will be implemented by Melee_Player subclasses")
    
    def __repr__(self):
        return f"Melee_Player(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range})"