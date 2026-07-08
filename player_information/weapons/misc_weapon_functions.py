import time, random
from weapons_enum import Weapons


def zero_health_adjustment(self) -> int:
    return max(0, self.health)

def alt_melee_stance_list() -> list:
    return [Weapons.DUAL_BLADES, Weapons.RIOT_SHIELD, Weapons.SLEDGEHAMMER, Weapons.SPEAR, Weapons.DAGGER, Weapons.SWORD, Weapons.THROWING_KNIVES]

def evasion_modifiers(target) -> int:
    if target.weapon not in alt_melee_stance_list():
        if target.tactical_reload_evasion_modifier:
            target.tactical_reload_evasion_modifier = False
            return target.evasion + 1
        
        else:
            return target.evasion
        
    else:
        if target.alt_stance:
            return target.evasion - 1
        
        else:
            return target.evasion

def melee_defense_modifier(self, target, base_damage: int, hit_chance: int) -> bool:
    accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if target.weapon == Weapons.DUAL_BLADES:
        if hit_chance >= evasion_modifiers(target):
            deflect_hit_chance = random.choice(accuracy_pool)
            target.health -= base_damage / 10

            if deflect_hit_chance >= evasion_modifiers(self):
                self.health -= base_damage
                print(f"{self.name} has their shot deflected back at them! {self.name} takes {base_damage} damage, and is left with {zero_health_adjustment(self)} health remaining.")
                time.sleep(2)
                print(f"{target.name} still takes some recoil damage from the deflection! {target.name} took {base_damage / 10} damage, and is left with {zero_health_adjustment(target)} health remaining.")
                return True
            
            else:
                print(f"{target.name} deflects the shot, but narrowly misses the trajectory! {target.name} takes {base_damage / 10} damage from the recoil, and is left with {zero_health_adjustment(target)} health remaining.")
                return True
            
        else:
            print(f"{target.name} adeptly evades the shot!")
            return False
    
    elif target.weapon == Weapons.RIOT_SHIELD:
        new_hit_chance = hit_chance - 3

        if new_hit_chance >= evasion_modifiers(target):
            target.health -= base_damage
            print(f"{target.name}'s feet have been shot! {self.name} masterfully finds the angle to shoot under {target.name}'s shield.")
            time.sleep(2)
            print(f"{target.name} takes {base_damage} damage, and is left with {zero_health_adjustment(target)} health remaining.")
            return True
        
        else:
            print(f"{target.name} blocks the shot!")
            return False