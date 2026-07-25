import time, random
from player_information.classes.player_template import Ranged_Player, Melee_Player
from player_information.ranks import init_evasion_calc
from player_information.enum_checks import is_valid_weapon
from player_information.weapons.ammo_mgmt import get_ammo
from player_information.weapons.weapons_enum import Weapons
from player_information.weapons.shoot_action import shoot_dmg_calc
from player_information.weapons.misc_weapon_functions import zero_health_adjustment, evasion_modifiers


class Ranged_Heavy(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 2 # Managed classes from input
        self.evasion = init_evasion_calc(self) - 1 # Evasion changes depending on weight and choice of range or melee
        self.health = 350
        self.weapon = is_valid_weapon(self.id, weapon) # Checks if the number fits withing the Weapon enum's criteria for the role and class, and assigns it if it is
        self.ammo = get_ammo(self) # Gives the selected weapon's full ammo count
        if self.weapon == Weapons.KS_23:
            self.reload_chain = False # Checks if tactical reload reloads one or two slugs on KS-23
    
    def shoot(self, target):
        if self.tactical_reload_evasion_modifier:
            time.sleep(2)
            self.tactical_reload_evasion_modifier = False
            print(f"{self.name} has finished their tactical reload, and is now back to their normal evasion")
        
        if self.weapon == Weapons.KS_23:
            self.reload_chain = False
        
        shoot_dmg_calc(self, target)
    
    def quick_melee(self, target):
        if self.tactical_reload_evasion_modifier:
            time.sleep(2)
            self.tactical_reload_evasion_modifier = False
            print(f"{self.name} has finished their tactical reload, and is now back to their normal evasion")
        
        if self.weapon == Weapons.KS_23:
            self.reload_chain = False

        time.sleep(2)
        accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hit_chance = random.choice(accuracy_pool)
        damage = 40

        if hit_chance >= evasion_modifiers(target):
            target.health -= damage
            print(f"{self.name} delivers a swift strike to {target.name} for {damage} damage! {target.name} has {zero_health_adjustment(target)} health remaining.")

        else:
            print(f"{self.name} attempts a quick strike, but {target.name} dodges out of the way!")

    def __repr__(self) -> str:
        if self.weapon == Weapons.KS_23:
            return f"Ranged_Heavy(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tactical_reload_evasion_modifier}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon}, ammo={self.ammo}, reload_chain={self.reload_chain})"

        return f"Ranged_Heavy(name={self.name}, rank={self.rank}, evasion={self.evasion}, tatical_reload_evasion_modifier={self.tactical_reload_evasion_modifier}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon}, ammo={self.ammo})"
    
class Melee_Heavy(Melee_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 5
        self.evasion = init_evasion_calc(self)
        self.health = 350
        self.weapon = is_valid_weapon(self.id, weapon)

    def __repr__(self):
        return f"Melee_Heavy(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance}, is_faster={self.is_faster}, rounds_won={self.rounds_won}, id={self.id}, health={self.health}, weapon={self.weapon})"