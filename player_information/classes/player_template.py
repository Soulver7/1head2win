import random, time
from ranks import init_evasion_calc
from enum_checks import is_valid_rank
from weapons.shoot_action import shoot_dmg_calc
from weapons.reload import reload_action
from weapons.main_melee_action import main_melee_dmg_calc
from weapons.alt_melee_action import alt_melee_action
from weapons.misc_weapon_functions import zero_health_adjustment, evasion_modifiers


class Ranged_Player: # Template for ranged player classes
    def __init__(self, name: str, rank: int):
        self.name = name
        self.rank = is_valid_rank(rank) # Checks if the number selected is valid, and assigns rank to the player based on the number chosen
        self.evasion = init_evasion_calc(self) # Chooses from a pool of evasion values based on the player's rank
        self.tatical_reload_evasion_modifier = False # Adds a temporary +1 evasion boost in exchange for skipping a turn and wasting ammo for an earlier reload

    def shoot(self, target): # Sorts by weapon type, and handles the shooting logic to calculate damage
        shoot_dmg_calc(self, target) 
    
    def reload(self): # Cannot reload at full ammo. If it's used at full ammo, it will skip their turn. This is also how self.tatical_reload_evasion_modifier is set to True
        reload_action(self)
    
    def quick_melee(self, target): # A strike that does 40 damage on hit. Proves useful for low health, low ammo situations
        time.sleep(1)
        self.tatical_reload_evasion_modifier = False
        accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hit_chance = random.choice(accuracy_pool)
        damage = 40

        if hit_chance >= evasion_modifiers(target):
            target.health -= damage
            print(f"{self.name} delivers a swift strike to {target.name} for {damage} damage! {target.name} has {zero_health_adjustment(target)} health remaining.")

        else:
            print(f"{self.name} attempts a quick strike, but {target.name} dodges out of the way!")
    
    def __repr__(self):
        return f"Ranged_Player(name={self.name}, rank={self.rank}, self.evasion={self.evasion}, self.tatical_reload_evasion_modifier={self.tatical_reload_evasion_modifier})"

class Melee_Player: # Template for melee player classes
    def __init__(self, name: str, rank: int):
        self.name = name
        self.rank = is_valid_rank(rank)
        self.evasion = init_evasion_calc(self) + 1 # All melee players start with a +1 to their evasion to compensate for having to move into melee range
        self.in_melee_range = False # Balances the higher evasion and damage output of melee weapons
        self.melee_rep_count = 0 # Handles various weapon combos that require multiple turns to execute
        self.alt_stance = False # Handles the attacks that require a "wind-up" turn, or defensive stances that reduce damage taken or deflect attacks. Nullifes the evasion bonus for melee players when True

    def move_in(self, target): # Simulates the movement between the two parties to properly engage a melee distanced fight. It's how self.in_melee_range is set to True
        time.sleep(1)
        if (self.evasion + random.randint(-2, 2)) > (target.evasion + random.randint(-2, 2)): # Adds variability to the "move in" action's success rate
            self.in_melee_range = True
            print(f'{self.name} is now in range! Let the beatdown commence!')

    def main_melee(self, target): # The left click function of the selected melee weapon
        main_melee_dmg_calc(self, target)

    def alt_melee(self, target): # The right click function of the selected melee weapon
        alt_melee_action(self, target)
    
    def quick_melee(self, target): # Ignores the need to have the self.in_melee_range set to True, so that Melee players won't be penalized for the same action ranged players have access to
        if self.alt_stance:
                time.sleep(1)
                self.alt_stance = False
                print(f'{self.name} drops their stance, and is now on the offensive!')

        time.sleep(1)
        accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hit_chance = random.choice(accuracy_pool)
        damage = 40

        if hit_chance >= evasion_modifiers(target):
            target.health -= damage
            print(f"{self.name} delivers a swift strike to {target.name} for {damage} damage! {target.name} has {zero_health_adjustment(target)} health remaining.")

        else:
            print(f"{self.name} attempts a quick strike, but {target.name} dodges out of the way!")


    def __repr__(self):
        return f"Melee_Player(name={self.name}, rank={self.rank}, evasion={self.evasion}, in_melee_range={self.in_melee_range}, melee_rep_count={self.melee_rep_count}, alt_stance={self.alt_stance})"