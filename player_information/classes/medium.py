from player_information.classes.player_template import Ranged_Player, Melee_Player
from player_information.ranks import init_evasion_calc
from player_information.enum_checks import is_valid_weapon
from player_information.weapons.ammo_mgmt import get_ammo


class Ranged_Medium(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 1
        self.health = 250 
        self.weapon = is_valid_weapon(self.id, weapon)
        self.ammo = get_ammo(self)

    def __repr__(self):
        return f"Ranged_Medium(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tactical_reload_evasion_modifier}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon}, ammo={self.ammo})"

class Melee_Medium(Melee_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 4
        self.health = 250
        self.weapon = is_valid_weapon(self.id, weapon)

    def __repr__(self):
        return f"Melee_Medium(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon})"