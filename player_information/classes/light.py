from player_template import Ranged_Player, Melee_Player
from ranks import init_evasion_calc
from enum_checks import is_valid_weapon
from weapons.ammo_mgmt import get_ammo


class Ranged_Light(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.evasion = init_evasion_calc(self) + 1
        self.health = 150
        self.weapon = is_valid_weapon("Ranged_Light", weapon)
        self.ammo = get_ammo(self)

    def __repr__(self):
        return f"Ranged_Light(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tatical_reload_evasion_modifier}, health={self.health}, weapon={self.weapon}, ammo={self.ammo})"
    
class Melee_Light(Melee_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.evasion = init_evasion_calc(self.rank) + 2
        self.health = 150
        self.weapon = is_valid_weapon("Melee_Light", weapon)

    def __repr__(self):
        return f"Melee_Light(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance}, health={self.health}, weapon={self.weapon})"