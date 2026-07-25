from player_information.classes.player_template import Ranged_Player, Melee_Player
from player_information.ranks import init_evasion_calc
from player_information.enum_checks import is_valid_weapon
from player_information.weapons.ammo_mgmt import get_ammo


class Ranged_Light(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 3
        self.evasion = init_evasion_calc(self) + 1
        self.health = 150
        self.weapon = is_valid_weapon(self.id, weapon)
        self.ammo = get_ammo(self)

    def __repr__(self):
        return f"Ranged_Light(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tactical_reload_evasion_modifier}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon}, ammo={self.ammo})"
    
class Melee_Light(Melee_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 6
        self.evasion = init_evasion_calc(self) + 2
        self.health = 150
        self.weapon = is_valid_weapon(self.id, weapon)

    def __repr__(self):
        return f"Melee_Light(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon})"