import random, time
from player_information.weapons.weapons_enum import Weapons
from player_information.weapons.misc_weapon_functions import zero_health_adjustment, evasion_modifiers, melee_defense_modifier


def alt_melee_action(self, target):
    accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    match self.weapon:
        case Weapons.DUAL_BLADES:
            time.sleep(2)
            self.melee_rep_count = 0
            self.alt_stance = True
            print(f"{self.name} assumes a defensive stance. Ready to deflect bullets!")
        
        case Weapons.RIOT_SHIELD:
            time.sleep(2)
            self.alt_stance = True
            print(f"{self.name} assumes a defensive stance. Ready to block incoming damage!")
        
        case Weapons.SLEDGEHAMMER:
            time.sleep(2)
            
            if self.alt_stance:
                self.alt_stance = False
                hit_chance = random.choice(accuracy_pool)
                damage = 175

                if hit_chance >= evasion_modifiers(target):
                    target.health -= damage
                    print(f"{self.name}'s hammer comes crashing down! {target.name} takes a tremendous {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.")

                else:
                    print(f"{self.name} whiffs their big swing! {target.name} has gotta be whipping the sweat off their brow now.")
            
            else:
                self.alt_stance = True
                print(f"{self.name} readies a big attack!")
        
        case Weapons.SPEAR:
            time.sleep(2)
            self.alt_stance = True
            self.melee_rep_count = 0
            hit_chance = random.choice(accuracy_pool)
            damage = 105

            if hit_chance >= evasion_modifiers(target):
                target.health -= damage
                print(f"{self.name}'s dancing spear elegantly cleaves {target.name}! {target.name} takes a solid {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.")

            else:
                print(f"Elegant movements doesn't automatically mean elegant accuracy. {target.name} dodges gracefully, and is left unscathed.")
        
        case Weapons.DAGGER:
            time.sleep(2)

            if self.alt_stance:
                self.alt_stance = False
                hit_chance = random.choice(accuracy_pool)

                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 320
                    target.health -= damage
                    print(f"{self.name} slips behind {target.name}, and delivers a devastating {damage} damage! {target.name} is left with {zero_health_adjustment(target)} health remaining.")

                elif hit_chance >= evasion_modifiers(target):
                    damage = 75
                    target.health -= damage
                    print(f"{self.name} stabs with conviction! {target.name} takes a solid {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.")

                else:
                    print(f"{self.name} stabs forward with gusto, but seems to have been blinded with fervor. {target.name} side steps the attack with ease.")
            
            else:
                self.alt_stance = True
                print(f"{self.name} readies themself for a critical strike!")
        
        case Weapons.SWORD:
            time.sleep(2)

            if self.alt_stance:
                self.alt_stance = False
                hit_chance = random.choice(accuracy_pool)

                if hit_chance >= evasion_modifiers(target):
                    damage = 120
                    target.health -= damage
                    print(f"{self.name} lunges forward! {target.name} takes a solid {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.")

                else:
                    print(f"{self.name} flies right by their target! {target.name} side steps the attack with ease.")
            
            else:
                self.alt_stance = True
                print(f'{self.name} prepares a daring lunge!')
        
        case Weapons.THROWING_KNIVES:
            time.sleep(2)

            if self.alt_stance:
                self.alt_stance = False
                hit_chance = random.choice(accuracy_pool)

                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 140, hit_chance)
                        return
                    
                if hit_chance >= 10 and hit_chance >= evasion_modifiers(target):
                    damage = 210
                    target.health -= damage
                    print(f"{self.name} lands a bullseye! Both knives land right in {target.name}'s cranium, dealing a critical {damage} damage, and leaving them with {zero_health_adjustment(target)} health remaining.")

                elif hit_chance >= evasion_modifiers(target):
                    damage = 140
                    target.health -= damage
                    print(f"{self.name}'s swift throw finds their mark! {target.name} takes a respectable {damage} damage, and is left with {zero_health_adjustment(target)} health remaining.")
                    
                else:
                    print(f"{self.name}'s prepared strike clinks sadly to the ground. {target.name} is left unharmed.")
            
            else:
                self.alt_stance = True
                print(f'{self.name} readies their knives for a decisive throw')
        
        case _:
            raise ValueError(f"That sure is an interesting way to use a gun, but we'll need a weapon that's classified as a melee weapon in The Finals.")