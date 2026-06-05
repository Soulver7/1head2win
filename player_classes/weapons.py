import random
from enum import Enum


class Weapons(Enum):
    # Medium Weapons
    AKM = 1
    CB_01_REPEATER = 2 # Had to adjust for enum naming constraints, but this is the CB-01 REPEATER
    CERBERUS_12GA = 3
    CHIMERA_XB = 4
    CL_40 = 5
    FAMAS = 6
    FCAR = 7
    MODEL_1887 = 8
    P90 = 9
    PIKE_556 = 10
    R_357 = 11
    # Medium Melee Weapons
    DUAL_BLADES = 12
    RIOT_SHIELD = 13
    # Heavy Weapons
    _50_AKIMBO = 14 # Had to adjust for enum naming constraints, but this is the .50 Akimbo
    BFR_TITAN = 15
    FLAMETHROWER = 16
    KS_23 = 17 # Had to adjust for enum naming constraints, but this is the KS-23
    LEWIS_GUN = 18
    M134_MINIGUN = 19
    M60 = 20
    MGL32 = 21
    SA1216 = 22
    SHAK_50 = 23 # Had to adjust for enum naming constraints, but this is the SHAK-50
    # Heavy Melee Weapons
    SLEDGEHAMMER = 24
    SPEAR = 25
    # Light Weapons
    _93R = 26 # Had to adjust for enum naming constraints, but this is the 93R
    ARN_220 = 27 # Had to adjust for enum naming constraints, but this is the ARN-220
    LH1 = 28
    M11 = 29
    M26_MATTER = 30
    RECURVE_BOW = 31
    SH1900 = 32
    SR_84 = 33 # Had to adjust for enum naming constraints, but this is the SR-84
    THROWING_KNIVES = 34
    V9S = 35
    XP_54 = 36 # Had to adjust for enum naming constraints, but this is the XP-54
    # Light Melee Weapons
    DAGGER = 37
    SWORD = 38

def get_ammo(weapon):
    match weapon:
        case Weapons.AKM:
            return 34
        case Weapons.CB_01_REPEATER:
            return 8
        case Weapons.CERBERUS_12GA:
            return 3
        case Weapons.CHIMERA_XB:
            return 15
        case Weapons.CL_40:
            return 5
        case Weapons.FAMAS:
            return 27
        case Weapons.FCAR:
            return 25
        case Weapons.MODEL_1887:
            return 7
        case Weapons.P90:
            return 50
        case Weapons.PIKE_556:
            return 12
        case Weapons.R_357:
            return 6
        case Weapons._50_AKIMBO:
            return 14
        case Weapons.BFR_TITAN:
            return 5
        case Weapons.FLAMETHROWER:
            return 30
        case Weapons.KS_23:
            return 6
        case Weapons.LEWIS_GUN:
            return 47
        case Weapons.M134_MINIGUN:
            return 300
        case Weapons.M60:
            return 70
        case Weapons.MGL32:
            return 6
        case Weapons.SA1216:
            return 16
        case Weapons.SHAK_50:
            return 20
        case Weapons._93R:
            return 24
        case Weapons.ARN_220:
            return 60
        case Weapons.LH1:
            return 15
        case Weapons.M11:
            return 40
        case Weapons.M26_MATTER:
            return 8
        case Weapons.RECURVE_BOW:
            return 1 # Infinite ammo, but I'll give it a "fake" ammo count of 1 for the sake of not having to reload
        case Weapons.SH1900:
            return 2
        case Weapons.SR_84:
            return 6
        case Weapons.THROWING_KNIVES:
            return 1 # Infinite ammo, but I'll give it a "fake" ammo count of 1 for the sake of not having to reload
        case Weapons.V9S:
            return 20
        case Weapons.XP_54:
            return 34
        case _:
            raise ValueError("Invalid weapon provided to get_ammo")
        
accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
def shoot_dmg_calc(self, target):
    match self.weapon:
        case Weapons.AKM:
            for i in range(10):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 30
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 10)')
                elif hit_chance >= target.evasion:
                    damage = 20
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 10)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 10)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.CB_01_REPEATER:
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)
            if hit_chance >= 9 and hit_chance >= target.evasion:
                damage = 126
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining.')
            elif hit_chance >= target.evasion:
                damage = 84
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining.')
            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.CERBERUS_12GA:
            on_hit_dot = 0
            for i in range(2):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                for j in range(13):
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= target.evasion:
                        damage = 4
                        target.health -= damage
                        on_hit_dot += 1
                        print(f'{self.name} lands a pellet! {target.name} took {damage} damage, and is left with {target.health} health remaining. (Pellet {j+1} of 13 in shot {i+1} of 2)')
                    else:
                        print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {target.health} health intact. (Pellet {j+1} of 13 in shot {i+1} of 2)')
            if on_hit_dot >= 8:
                burn_damage = random.randint(15, 45)
                target.health -= burn_damage
                print(f'{target.name} has taken an additional {burn_damage} damage from being set aflame! {target.name} is now left with {target.health} health remaining.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.CHIMERA_XB:
            for i in range(4):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 67.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 4)')
                elif hit_chance >= target.evasion:
                    damage = 45
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 4)')
                elif hit_chance < target.evasion:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 4)')
                print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.CL_40:
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)
            if hit_chance >= 9 and hit_chance >= target.evasion:
                damage = 105
                target.health -= damage
                print(f'{self.name} lands a direct hit! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining.')
            elif hit_chance >= target.evasion:
                damage = random.randint(11, 79)
                target.health -= damage
                print(f'{self.name} blasts {target.name}! {target.name} took {damage} damage from the impact, and is left with {target.health} health remaining.')
            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.FAMAS:
            for i in range(4):
                for j in range(3):
                    if self.ammo <= 0:
                        print(f'{self.name} is out of ammo and cannot shoot anymore!')
                        break
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= 9 and hit_chance >= target.evasion:
                        damage = 34.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')
                    elif hit_chance >= target.evasion:
                        damage = 23
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')
                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {j+1} of 3 in burst {i+1} of 4)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.FCAR:
            for i in range(9):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 34.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 9)')
                elif hit_chance >= target.evasion:
                    damage = 23
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 9)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 9)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.MODEL_1887:
            for i in range(9):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= target.evasion:
                    damage = 12
                    target.health -= damage
                    print(f'{self.name} lands a pellet! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Pellet {i+1} of 9)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Pellet {i+1} of 9)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.P90:
            for i in range(15):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 21
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 15)')
                elif hit_chance >= target.evasion:
                    damage = 14
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 15)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 15)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.PIKE_556:
            for i in range(3):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 73.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 3)')
                elif hit_chance >= target.evasion:
                    damage = 49
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 3)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 3)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.R_357:
            for i in range(2):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 148
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 2)')
                elif hit_chance >= target.evasion:
                    damage = 74
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 2)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 2)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons._50_AKIMBO:
            for i in range(4):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 88
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 4)')
                elif hit_chance >= target.evasion:
                    damage = 44
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 4)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 4)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.BFR_TITAN:
            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)
            if hit_chance >= 9 and hit_chance >= target.evasion:
                damage = 132
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining.')
            elif hit_chance >= target.evasion:
                damage = 88
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining.')
            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.FLAMETHROWER:
            burn_stacks = 0
            for i in range(3):
                if self.ammo <= 0:
                    print(f'{self.name} is out of gas and cannot spray anymore flames!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= target.evasion:
                    burn_stacks += 1
                    damage = 30
                    target.health -= damage
                    print(f"{self.name} engulfs {target.name} in flames! {target.name} took {damage} damage, and there's more where that came from. {target.name} is left with {target.health} health remaining, for now. (Spray {i+1} of 3)")
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Spray {i+1} of 3)')
            burn_damage = burn_stacks * 7.5
            target.health -= burn_damage
            print(f'{target.name} has taken an additional {burn_damage} damage due to thier burns, and is now left with {target.health} health remaining.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} amount left in the tank.')
        
        case Weapons.KS_23:
            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)
            if hit_chance >= target.evasion:
                damage = 100
                target.health -= damage
                print(f'{self.name} hits their target! {target.name} takes a solid {damage} damage, and is left with {target.health} health remaining.')
            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.LEWIS_GUN:
            for i in range(8):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 34.5
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 8)')
                elif hit_chance >= target.evasion:
                    damage = 23
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 8)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 8)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.M134_MINIGUN:
            for i in range(25):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 14.63
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 25)')
                elif hit_chance >= target.evasion:
                    damage = 11
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 25)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 25)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.M60:
            for i in range(10):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 30
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 10)')
                elif hit_chance >= target.evasion:
                    damage = 20
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 10)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 10)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.MGL32:
            for i in range(2):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 83
                    target.health -= damage
                    print(f'{self.name} lands a direct hit! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining.')
                elif hit_chance >= target.evasion:
                    damage = random.randint(10, 75)
                    target.health -= damage
                    print(f'{self.name} blasts {target.name}! {target.name} took {damage} damage from the impact, and is left with {target.health} health remaining.')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.SA1216:
            for i in range(3):
                if self.ammo <= -3:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                if self.ammo == 12 or self.ammo == 7 or self.ammo == 2:
                    print(f'Rotating the magazine!')
                    self.ammo -= 1
                    continue
                self.ammo -= 1
                for j in range(12):
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= target.evasion:
                        damage = 6
                        target.health -= damage
                        print(f'{self.name} lands pellet! {target.name} took {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 12 in shot {i+1} of 3)')
                    else:
                        print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {target.health} health intact. (Shot {j+1} of 12 in shot {i+1} of 3)')
            if self.ammo <= 16 and self.ammo >= 12:
                print(f'{self.name} has 4 magazine tubes left, and {self.ammo}/{self.get_ammo()} ammo remaining.')
            elif self.ammo < 12 and self.ammo >= 7:
                print(f'{self.name} has 3 magazine tubes left, and {self.ammo+1}/{self.get_ammo()} ammo remaining.')
            elif self.ammo < 7 and self.ammo >= 2:
                print(f'{self.name} has 2 magazine tubes left, and {self.ammo+2}/{self.get_ammo()} ammo remaining.')
            elif self.ammo < 2 and self.ammo >= -3:
                print(f'{self.name} has 1 magazine tube left, and {self.ammo+3}/{self.get_ammo()} ammo remaining.')

        case Weapons.SHAK_50:
            for i in range(7):
                for j in range(2):
                    if self.ammo <= 0:
                        print(f'{self.name} is out of ammo and cannot shoot anymore!')
                        break
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= 9 and hit_chance >= target.evasion:
                        damage = 22.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 2 in burst {i+1} of 7)')
                    elif hit_chance >= target.evasion:
                        damage = 15
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 2 in burst {i+1} of 7)')
                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {j+1} of 2 in burst {i+1} of 7)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons._93R:
            for i in range(4):
                for j in range(3):
                    if self.ammo <= 0:
                        print(f'{self.name} is out of ammo and cannot shoot anymore!')
                        break
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= 9 and hit_chance >= target.evasion:
                        damage = 37.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')
                    elif hit_chance >= target.evasion:
                        damage = 25
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {j+1} of 3 in burst {i+1} of 4)')
                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {j+1} of 3 in burst {i+1} of 4)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.ARN_220:
            for i in range(12):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                if self.ammo == 31:
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= 9 and hit_chance >= target.evasion:
                        damage = 25.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 12)')
                    elif hit_chance >= target.evasion:
                        damage = 17
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 12)')
                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 12)')
                    print(f'End of first magazine! Reloading...')
                    break
                else:
                    self.ammo -= 1
                    hit_chance = random.choice(accuracy_pool)
                    if hit_chance >= 9 and hit_chance >= target.evasion:
                        damage = 25.5
                        target.health -= damage
                        print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 12)')
                    elif hit_chance >= target.evasion:
                        damage = 17
                        target.health -= damage
                        print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 12)')
                    else:
                        print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 12)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.LH1:
            for i in range(5):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 88
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 5)')
                elif hit_chance >= target.evasion:
                    damage = 44
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 5)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 5)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.M11:
            for i in range(17):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 24
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 17)')
                elif hit_chance >= target.evasion:
                    damage = 16
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 17)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 17)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.M26_MATTER:
            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            self.ammo -= 1
            for i in range(11):
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= target.evasion:
                    damage = 11
                    target.health -= damage
                    print(f"One of {self.name}'s pellets hits {target.name} took {damage} damage! (Pellet {i+1} of 11)")
                else:
                    print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {target.health} health intact. (Pellet {i+1} of 11)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')

        case Weapons.RECURVE_BOW:
            hit_chance = random.choice(accuracy_pool)
            if hit_chance >= 9 and hit_chance >= target.evasion:
                damage = random.randint(90, 186)
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining.')
            elif hit_chance >= target.evasion:
                damage = random.randint(60, 124)
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining.')
            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
        
        case Weapons.SH1900:
            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            self.ammo -= 1
            for i in range(15):
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= target.evasion:
                    damage = 12
                    target.health -= damage
                    print(f"One of {self.name}'s pellets hits {target.name} took {damage} damage! (Pellet {i+1} of 15)")
                else:
                    print(f'{self.name} missed a pellet! {target.name} gets off scot-free with their {target.health} health intact. (Pellet {i+1} of 15)')

        case Weapons.SR_84:
            if self.ammo <= 0:
                print(f'{self.name} is out of ammo and cannot shoot!')
                return
            self.ammo -= 1
            hit_chance = random.choice(accuracy_pool)
            if hit_chance >= 9 and hit_chance >= target.evasion:
                damage = 236
                target.health -= damage
                print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining.')
            elif hit_chance >= target.evasion:
                damage = 118
                target.health -= damage
                print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining.')
            else:
                print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact.')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.V9S:
            for i in range(6):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 57
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 6)')
                elif hit_chance >= target.evasion:
                    damage = 38
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 6)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 6)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case Weapons.XP_54:
            for i in range(15):
                if self.ammo <= 0:
                    print(f'{self.name} is out of ammo and cannot shoot anymore!')
                    break
                self.ammo -= 1
                hit_chance = random.choice(accuracy_pool)
                if hit_chance >= 9 and hit_chance >= target.evasion:
                    damage = 24
                    target.health -= damage
                    print(f'{self.name} hits a headshot! {target.name} takes a critical {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 15)')
                elif hit_chance >= target.evasion:
                    damage = 16
                    target.health -= damage
                    print(f'{self.name} lands a clean shot! {target.name} took a smooth {damage} damage, and is left with {target.health} health remaining. (Shot {i+1} of 15)')
                else:
                    print(f'{self.name} missed their shot! {target.name} gets off scot-free with their {target.health} health intact. (Shot {i+1} of 15)')
            print(f'{self.name} has {self.ammo}/{self.get_ammo()} ammo remaining.')
        
        case _:
            raise ValueError("Can't shoot with that weapon. Try inputing a valid gun from the game, and don't go crazy looking for a trigger on a melee weapon.")
