import random, time
from player_information.weapons.weapons_enum import Weapons
from player_information.weapons.ammo_mgmt import get_ammo
from player_information.weapons.misc_weapon_functions import zero_health_adjustment, evasion_modifiers, melee_defense_modifier

    
def shoot_dmg_calc(self, target):
    accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.tactical_reload_evasion_modifier = False

    match self.weapon:
        case Weapons.AKM:
            for i in range(10):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 20, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 30
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 10)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 20
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 10)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 10)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.CB_01_REPEATER:
            time.sleep(2)

            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)

            if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 84, hit_chance)
                        return
                    
            if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                damage = 126
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            elif hit_chance >= evasion_modifiers(target):
                damage = 84
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.CERBERUS_12GA:
            on_hit_dot = 0

            for i in range(2):
                if self.ammo <= 0:
                    time.sleep(2)
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1

                for j in range(13):
                    time.sleep(2)
                    hit_chance = random.choice(accuracy_pool)

                    if target.health <= 0:
                        return

                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            if melee_defense_modifier(self, target, 4, hit_chance):
                                on_hit_dot += 1
                                continue

                            else:
                                continue

                    if hit_chance >= evasion_modifiers(target):
                        damage = 4
                        target.health -= damage
                        on_hit_dot += 1
                        print(f'{self.name} lands a pellet! {target.name} took {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Pellet {j+1} of 13 in shot string{i+1} of 2)')

                    else:
                        print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Pellet {j+1} of 13 in shot string {i+1} of 2)')

            if on_hit_dot >= 8:
                time.sleep(2)
                burn_damage = random.randint(15, 45)
                target.health -= burn_damage
                print(f'{target.name} has taken an additional {burn_damage} damage from being set aflame! {target.name} is now left with {zero_health_adjustment(target)} health remaining.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.CHIMERA_XB:
            for i in range(4):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 45, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 67.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 4)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 45
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 4)')

                elif hit_chance < evasion_modifiers(target):
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 4)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.CL_40:
            time.sleep(2)

            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)

            if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, random.randint(11, 79), hit_chance)
                        return
            
            if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                damage = 105
                target.health -= damage
                print(f'{self.name} lands a direct hit! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            elif hit_chance >= evasion_modifiers(target):
                damage = random.randint(11, 79)
                target.health -= damage
                print(f'{self.name} blasts {target.name}! {target.name} took {damage} damage from the impact, and is left with {zero_health_adjustment(target)} health remaining.')

            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.FAMAS:
            for i in range(4):
                for j in range(3):
                    time.sleep(2)

                    if self.ammo <= 0:
                        print(f'{self.name} is out of ammo and cannot shoot anymore!')
                        return

                    if target.health <= 0:
                        return
                    
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)

                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            melee_defense_modifier(self, target, 23, hit_chance)
                            continue

                    if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                        damage = 34.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')

                    elif hit_chance >= evasion_modifiers(target):
                        damage = 23
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')

                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {j+1} of 3 in burst {i+1} of 4)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.FCAR:
            for i in range(9):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 23, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 34.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 9)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 23
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 9)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 9)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.MODEL_1887:
            for i in range(9):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 12, hit_chance)
                        continue

                if hit_chance >= evasion_modifiers(target):
                    damage = 12
                    target.health -= damage
                    print(f'{self.name} lands a pellet! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Pellet {i+1} of 9)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Pellet {i+1} of 9)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.P90:
            for i in range(15):
                time.sleep(2)
                
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 14, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 21
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 15)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 14
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 15)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 15)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.PIKE_556:
            for i in range(3):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 49, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 73.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 3)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 49
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 3)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 3)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.R_357:
            for i in range(2):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 74, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 148
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 2)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 74
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 2)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 2)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons._50_AKIMBO:
            for i in range(4):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 44, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 88
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 4)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 44
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 4)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 4)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.BFR_TITAN:
            time.sleep(2)

            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)

            if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 88, hit_chance)
                        return
                    
            if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                damage = 132
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            elif hit_chance >= evasion_modifiers(target):
                damage = 88
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.FLAMETHROWER:
            burn_stacks = 0

            for i in range(3):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of gas and cannot spray anymore flames!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if hit_chance >= evasion_modifiers(target):
                    burn_stacks += 1
                    damage = 30
                    target.health -= damage
                    print(f"{self.name} engulfs {target.name} in flames! {target.name} took {damage} damage, and there's more where that came from. {target.name} is left with {zero_health_adjustment(target)} health remaining, for now. (Spray {i+1} of 3)")

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Spray {i+1} of 3)')

            if burn_stacks > 0:
                time.sleep(2)
                burn_damage = burn_stacks * 7.5
                target.health -= burn_damage
                print(f'{target.name} has taken an additional {burn_damage} damage due to thier burns! {target.name} is now left with {zero_health_adjustment(target)} health remaining.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} amount of gas left in the tank.')
        
        case Weapons.KS_23:
            time.sleep(2)

            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)

            if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 100, hit_chance)
                        return
                    
            if hit_chance >= evasion_modifiers(target):
                damage = 100
                target.health -= damage
                print(f'{self.name} hits their target! {target.name} takes a solid {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.LEWIS_GUN:
            for i in range(8):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 23, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 34.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 8)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 23
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 8)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 8)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.M134_MINIGUN:
            for i in range(25):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 11, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 14.63
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 25)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 11
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 25)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 25)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.M60:
            for i in range(10):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 20, hit_chance)
                        return
                    
                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 30
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 10)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 20
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 10)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 10)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.MGL32:
            for i in range(2):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, random.randint(10, 75), hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 83
                    target.health -= damage
                    print(f'{self.name} lands a direct hit! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

                elif hit_chance >= evasion_modifiers(target):
                    damage = random.randint(10, 75)
                    target.health -= damage
                    print(f'{self.name} blasts {target.name}! {target.name} took {damage} damage from the impact, and is left with {zero_health_adjustment(target)} health remaining.')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.SA1216:
            for i in range(3):
                if self.ammo <= -3:
                    time.sleep(2)
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                if self.ammo == 12 or self.ammo == 7 or self.ammo == 2:
                    time.sleep(2)
                    print(f'Rotating the magazine!')
                    self.ammo -= 1
                    continue

                self.ammo -= 1

                for j in range(12):
                    time.sleep(2)
                    hit_chance = random.choice(accuracy_pool)

                    if target.health <= 0:
                        return
                    
                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            melee_defense_modifier(self, target, 6, hit_chance)
                            continue

                    if hit_chance >= evasion_modifiers(target):
                        damage = 6
                        target.health -= damage
                        print(f'{self.name} lands pellet! {target.name} took {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Pellet {j+1} of 12 in shot string {i+1} of 3)')

                    else:
                        print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Pellet {j+1} of 12 in shot string {i+1} of 3)')

            time.sleep(2)

            if min(max(12, self.ammo), 16) == self.ammo:
                print(f'{self.name} has 4 magazine tubes left, and {self.ammo}/{get_ammo(self)} ammo remaining.')

            elif min(max(7, self.ammo), 11) == self.ammo:
                print(f'{self.name} has 3 magazine tubes left, and {self.ammo+1}/{get_ammo(self)} ammo remaining.')

            elif min(max(2, self.ammo), 6) == self.ammo:
                print(f'{self.name} has 2 magazine tubes left, and {self.ammo+2}/{get_ammo(self)} ammo remaining.')

            elif min(max(-3, self.ammo), 1) == self.ammo:
                print(f'{self.name} has 1 magazine tube left, and {self.ammo+3}/{get_ammo(self)} ammo remaining.')

        case Weapons.SHAK_50:
            for i in range(7):
                for j in range(2):
                    time.sleep(2)

                    if self.ammo <= 0:
                        print(f'{self.name} is out of ammo and cannot shoot anymore!')
                        return

                    if target.health <= 0:
                        return
                    
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)

                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            melee_defense_modifier(self, target, 15, hit_chance)
                            continue

                    if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                        damage = 22.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {j+1} of 2 in burst {i+1} of 7)')

                    elif hit_chance >= evasion_modifiers(target):
                        damage = 15
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {j+1} of 2 in burst {i+1} of 7)')

                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {j+1} of 2 in burst {i+1} of 7)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons._93R:
            for i in range(4):
                for j in range(3):
                    time.sleep(2)

                    if self.ammo <= 0:
                        print(f'{self.name} is out of ammo and cannot shoot anymore!')
                        return

                    if target.health <= 0:
                        return
                    
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)

                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            melee_defense_modifier(self, target, 25, hit_chance)
                            continue

                    if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                        damage = 37.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')

                    elif hit_chance >= evasion_modifiers(target):
                        damage = 25
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')

                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {j+1} of 3 in burst {i+1} of 4)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.ARN_220:
            for i in range(12):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                if self.ammo == 31:
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)

                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            melee_defense_modifier(self, target, 17, hit_chance)
                            print(f'End of first magazine! Switching to second magazine...')
                            break

                    if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                        damage = 25.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 12)')

                    elif hit_chance >= evasion_modifiers(target):
                        damage = 17
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 12)')

                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 12)')

                    print(f'End of first magazine! Switching to second magazine...')
                    break

                else:
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)

                    if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                        if target.alt_stance:
                            melee_defense_modifier(self, target, 17, hit_chance)
                            continue

                    if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                        damage = 25.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 12)')

                    elif hit_chance >= evasion_modifiers(target):
                        damage = 17
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 12)')

                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 12)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.LH1:
            for i in range(5):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 44, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 88
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 5)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 44
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 5)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 5)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.M11:
            for i in range(17):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 16, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 24
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 17)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 16
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 17)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 17)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.M26_MATTER:
            if self.ammo <= 0:
                time.sleep(2)
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1

            for i in range(11):
                time.sleep(2)
                hit_chance = random.choice(accuracy_pool)

                if target.health <= 0:
                    return
                
                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 11, hit_chance)
                        continue

                if hit_chance >= evasion_modifiers(target):
                    damage = 11
                    target.health -= damage
                    print(f"One of {self.name}'s pellets hits! {target.name} took {damage} damage. (Pellet {i+1} of 11)")

                else:
                    print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Pellet {i+1} of 11)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.RECURVE_BOW:
            time.sleep(2)
            hit_chance = random.choice(accuracy_pool)

            if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, random.randint(60, 124), hit_chance)
                        return
                    
            if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                damage = random.randint(90, 186)
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            elif hit_chance >= evasion_modifiers(target):
                damage = random.randint(60, 124)
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')
        
        case Weapons.SH1900:
            if self.ammo <= 0:
                time.sleep(2)
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1

            for i in range(15):
                time.sleep(2)
                hit_chance = random.choice(accuracy_pool)

                if target.health <= 0:
                    return

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 12, hit_chance)
                        continue

                if hit_chance >= evasion_modifiers(target):
                    damage = 12
                    target.health -= damage
                    print(f"One of {self.name}'s pellets hits! {target.name} took {damage} damage. (Pellet {i+1} of 15)")

                else:
                    print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Pellet {i+1} of 15)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')

        case Weapons.SR_84:
            time.sleep(2)

            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)

            if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 118, hit_chance)
                        return
                    
            if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                damage = 236
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            elif hit_chance >= evasion_modifiers(target):
                damage = 118
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.')

            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact.')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.V9S:
            for i in range(6):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 38, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 57
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 6)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 38
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 6)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 6)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case Weapons.XP_54:
            for i in range(15):
                time.sleep(2)

                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    return

                if target.health <= 0:
                    return
                
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 16, hit_chance)
                        continue

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 24
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 15)')

                elif hit_chance >= evasion_modifiers(target):
                    damage = 16
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {zero_health_adjustment(target)} health remaining. (Shot {i+1} of 15)')

                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {zero_health_adjustment(target)} health intact. (Shot {i+1} of 15)')

            time.sleep(2)
            print(f'{self.name} has {self.ammo}/{get_ammo(self)} ammo remaining.')
        
        case _:
            raise ValueError("Try inputing a valid ranged weapon from the The Finals, and don't go crazy looking for a trigger on a melee weapon.")