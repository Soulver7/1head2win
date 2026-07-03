from time import time
from player_template import Ranged_Player, Melee_Player
from ranks import Ranks, init_evasion_calc
from weapons.shoot_action import shoot_dmg_calc
from weapons.ammo_mgmt import get_ammo


class Medium(Ranged_Player):
    def __init__(self, name, rank, weapon):
        super().__init__(name, rank)
        self.health = 250
        self.weapon = weapon # Make a function that checks for weapon validity and returns the appropriate enum value. Raise an error if invalid.
        self.ammo = get_ammo(weapon)
        self.evasion = init_evasion_calc(rank)
        self.tatical_reload_evasion_modifier = False

    def reload(self):
        time.sleep(1)
        if self.ammo <= 0:
            self.ammo = get_ammo(self.weapon)
            print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and ready to fight again!")
        else:
            self.ammo = get_ammo(self.weapon)
            self.evasion += 1
            self.tatical_reload_evasion_modifier = True
            print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and seems to be moving more adeptly!")
    
    def __repr__(self):
        return f"Medium(name={self.name}, rank={self.rank}, health={self.health}, weapon={self.weapon}, ammo={self.ammo}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tatical_reload_evasion_modifier})"

class Medium_Melee(Melee_Player):
    def __init__(self, name, rank, weapon):
        super().__init__(name, rank)
        self.health = 250
        self.weapon = weapon
        self.evasion = init_evasion_calc(rank) + 1
        self.in_melee_range = False
        self.defensive_stance = False

    def light_melee(self, target):
        raise NotImplementedError("Will be implemented by Medium_Melee subclasses")
    
    def heavy_melee(self):
        raise NotImplementedError("Will be implemented by Medium_Melee subclasses")
    
    def __repr__(self):
        return f"Medium_Melee(name={self.name}, rank={self.rank}, health={self.health}, weapon={self.weapon}, evasion={self.evasion}, in_melee_range={self.in_melee_range})"