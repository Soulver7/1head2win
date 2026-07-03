import random, time
from weapons_enum import Weapons
from misc_weapon_functions import *


def light_melee_dmg_calc(self, target):
    accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    match self.weapon:
        case Weapons.DUAL_BLADES:
            self.alt_stance = False
            if self.melee_rep_count == 0:
                for i in range(2):
                    time.sleep(1)
                    hit_chance = random.choice(accuracy_pool)
                    damage = 50
                    if hit_chance >= evasion_modifiers(target):
                        target.health -= damage
                        print(f"{self.name} slashes {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining. (Swing {i} of 2)")
                    else:
                        print(f"{self.name} swings and misses! {target.name} evades the attack with ease. (Swing {i} of 2)")
            if self.melee_rep_count == 1:
                for i in range(2):
                    time.sleep(1)
                    hit_chance = random.choice(accuracy_pool)
                    damage = 60
                    if hit_chance >= evasion_modifiers(target):
                        target.health -= damage
                        print(f"{self.name} slashes {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining. (Swing {i} of 2)")
                    else:
                        print(f"{self.name} swings and misses! {target.name} evades the attack with ease. (Swing {i} of 2)")
            if self.melee_rep_count == 2:
                time.sleep(1)
                self.melee_rep_count = 0
                hit_chance = random.choice(accuracy_pool)
                damage = 100
                if hit_chance >= evasion_modifiers(target):
                    target.health -= damage
                    print(f"{self.name} unleashes a devastating finisher on {target.name} for a massive {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
                else:
                    print(f"{self.name} attempts a powerful combo finisher, but {target.name} anticipates the move, and evades just in time!")
        
        case Weapons.RIOT_SHIELD:
            time.sleep(1)
            self.alt_stance = False
            hit_chance = random.choice(accuracy_pool)
            damage = 90
            if hit_chance >= evasion_modifiers(target):
                target.health -= damage
                print(f"{self.name} bludgeons {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
            else:
                print(f"{self.name} swings and misses! {target.name} evades the attack with ease.")
        
        case Weapons.SLEDGEHAMMER:
            time.sleep(1)
            self.alt_stance = False
            hit_chance = random.choice(accuracy_pool)
            damage = 100
            if hit_chance >= evasion_modifiers(target):
                target.health -= damage
                print(f"{self.name} bludgeons {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
            else:
                print(f"{self.name} swings and misses! {target.name} evades the attack with ease.")
        
        case Weapons.SPEAR:
            time.sleep(1)
            self.alt_stance = False
            if self.melee_rep_count == 0:
                hit_chance = random.choice(accuracy_pool)
                damage = 65
                if hit_chance >= evasion_modifiers(target):
                    target.health -= damage
                    print(f"{self.name} pierces {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
                else:
                    print(f"{self.name} thrusts their spear, but {target.name} evades the attack with ease.")
            if self.melee_rep_count == 1:
                hit_chance = random.choice(accuracy_pool)
                damage = 80
                if hit_chance >= evasion_modifiers(target):
                    target.health -= damage
                    print(f"{self.name} pierces {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
                else:
                    print(f"{self.name} thrusts their spear, but {target.name} evades the attack with ease.")
            if self.melee_rep_count == 2:
                self.melee_rep_count = 0
                hit_chance = random.choice(accuracy_pool)
                damage = 90
                if hit_chance >= evasion_modifiers(target):
                    target.health -= damage
                    print(f"{self.name} unleashes a devastating finisher on {target.name} for a massive {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
                else:
                    print(f"{self.name} attempts a powerful finisher, but {target.name} anticipates the move, and evades just in time!")

        case Weapons.DAGGER:
            time.sleep(1)
            self.alt_stance = False
            hit_chance = random.choice(accuracy_pool)
            damage = 60
            if hit_chance >= evasion_modifiers(target):
                target.health -= damage
                print(f"{self.name} stabs {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
            else:
                print(f"{self.name} stabs forward, but {target.name} evades the attack with ease.")
        
        case Weapons.SWORD:
            time.sleep(1)
            self.alt_stance = False
            hit_chance = random.choice(accuracy_pool)
            damage = 88
            if hit_chance >= evasion_modifiers(target):
                target.health -= damage
                print(f"{self.name} slashes {target.name} for a solid {damage} damage! {target.name} has {zero_health_adjustment(target.health)} health remaining.")
            else:
                print(f"{self.name} swings and misses! {target.name} evades the attack with ease.")
        
        case Weapons.THROWING_KNIVES:
            self.alt_stance = False
            self.melee_rep_count = 0
            for i in range(2):
                time.sleep(1)
                hit_chance = random.choice(accuracy_pool)
                if target.weapon == Weapons.RIOT_SHIELD or target.weapon == Weapons.DUAL_BLADES:
                    if target.alt_stance:
                        melee_defense_modifier(self, target, 60, hit_chance)
                        return
                if hit_chance >= 9 and hit_chance >= evasion_modifiers(target):
                    damage = 90
                    target.health -= damage
                    print(f"{self.name} stuck them right in the head! {target.name} took a devestating {damage} damage, and is left with {zero_health_adjustment(target.health)} remaining. (Knife {i} of 2)")
                elif hit_chance >= evasion_modifiers(target):
                    damage = 60
                    target.health -= damage
                    print(f"{self.name}'s knife strikes true! {target.name} took {damage} damage, and is left with {zero_health_adjustment(target.health)} health remaining. (Knife {i} of 2)")
                else:
                    print(f"{self.name}'s knife whiffs! {target.name} remains unharmed. (Knife {i} of 2)")
        
        case _:
            raise ValueError(f"That sure is an interesting way to use a gun, but we'll need a weapon that's classified as a melee weapon in The Finals.")