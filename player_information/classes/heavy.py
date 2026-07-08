from player_template import Ranged_Player, Melee_Player
from ranks import init_evasion_calc
from enum_checks import is_valid_weapon
from weapons.ammo_mgmt import get_ammo


class Ranged_Heavy(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.evasion = init_evasion_calc(self) - 1
        self.health = 350
        self.weapon = is_valid_weapon("Ranged_Heavy", weapon)
        self.ammo = get_ammo(self)

    def __repr__(self):
        return f"Ranged_Heavy(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tatical_reload_evasion_modifier}, health={self.health}, weapon={self.weapon}, ammo={self.ammo})"
    
class Melee_Heavy(Melee_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.health = 350
        self.weapon = is_valid_weapon("Melee_Heavy", weapon)

    def __repr__(self):
        return f"Melee_Heavy(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance}, health={self.health}, weapon={self.weapon})"