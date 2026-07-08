from player_template import Ranged_Player, Melee_Player
from ranks import init_evasion_calc
from enum_checks import is_valid_weapon
from weapons.ammo_mgmt import get_ammo


class Ranged_Medium(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.health = 250 
        self.weapon = is_valid_weapon("Ranged_Medium", weapon) # Checks if the number fits withing the Weapon enum's criteria for the role and class, and assigns it if it is
        self.ammo = get_ammo(self) # Gives the selected weapon's full ammo count

    def __repr__(self):
        return f"Ranged_Medium(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tatical_reload_evasion_modifier}, health={self.health}, weapon={self.weapon}, ammo={self.ammo})"

class Melee_Medium(Melee_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.evasion = init_evasion_calc(self.rank) + 1
        self.health = 250
        self.weapon = is_valid_weapon("Melee_Medium", weapon)

    def __repr__(self):
        return f"Melee_Medium(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance}, health={self.health}, weapon={self.weapon})"