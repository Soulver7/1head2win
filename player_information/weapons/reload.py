import time
from player_information.weapons.weapons_enum import Weapons
from player_information.weapons.ammo_mgmt import get_ammo
from player_information.weapons.misc_weapon_functions import max_ammo_adjustment


def reload_action(self) -> bool:
    time.sleep(2)
    self.tactical_reload_evasion_modifier = False

    match self.weapon:
        case Weapons.CB_01_REPEATER:
            if min(1, self.ammo) == self.ammo:
                self.ammo = 5
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} racked 5 bullets, and is ready to fight again!")
                return True

            elif max(self.ammo, get_ammo(self)-1) == self.ammo:
                print("You can't reload a mag that's already full! Try another action.")
                return False

            else:
                self.ammo = max_ammo_adjustment(self, 2)
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional 2 bullets, and seems to be more evasive with their tactical reload!")
                return True

        case Weapons.CL_40:
            if min(1, self.ammo) == self.ammo:
                self.ammo = 1
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional round, and is ready to fight again!")
                return True

            elif max(self.ammo, get_ammo(self)-1) == self.ammo:
                print("You can't reload a mag that's already full! Try another action.")
                return False

            else:
                self.ammo = max_ammo_adjustment(self, 2)
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional 2 rounds, and seems to be more evasive with their tactical reload!")
                return True
        
        case Weapons.MODEL_1887:
            if min(1, self.ammo) == self.ammo:
                self.ammo = 2
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional 2 bullets, and is ready to fight again!")
                return True

            elif max(self.ammo, get_ammo(self)-1) == self.ammo:
                print("You can't reload a mag that's already full! Try another action.")
                return False
            
            elif self.ammo == 5 or self.ammo == 6:
                self.ammo = 7
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional bullet, and seems to be more evasive with their tactical reload!")
                return True

            else:
                self.ammo = max_ammo_adjustment(self, 2)
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional 2 rounds, and seems to be more evasive with their tactical reload!")
                return True
        
        case Weapons.BFR_TITAN:
            if min(1, self.ammo) == self.ammo:
                self.ammo = 2
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional 2 bullets, and is ready to fight again!")
                return True
            
            elif max(self.ammo, get_ammo(self)-1) == self.ammo:
                print("You can't reload a mag that's already full! Try another action.")
                return False

            else:
                self.ammo = max_ammo_adjustment(self, 2)
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional 2 bullets, and seems to be more evasive with their tactical reload!")
                return True
        
        case Weapons.KS_23:
            if min(1, self.ammo) == self.ammo:
                self.ammo = 1
                self.reload_chain = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} reloads an additional slug, and is ready to fight again!")
                time.sleep(2)
                print("(You will recieve 2 slugs per reload until next action)")
                return True
            
            elif max(self.ammo, get_ammo(self)-1) == self.ammo:
                self.reload_chain = False
                print("You can't reload a mag that's already full! Try another action.")
                return False

            else:
                if self.reload_chain:
                    self.ammo = max_ammo_adjustment(self, 2)
                    self.tactical_reload_evasion_modifier = True
                    print("Reloading...")
                    time.sleep(2)
                    print(f"Reload complete! {self.name} reloads an additional 2 slugs, and seems to be more evasive with their tactical reload!")
                
                else:
                    self.ammo = max_ammo_adjustment(self, 1)
                    self.tactical_reload_evasion_modifier = True
                    print("Reloading...")
                    time.sleep(2)
                    print(f"Reload complete! {self.name} reloads an additional slug, and seems to be more evasive with their tactical reload!")

                return True

        case Weapons.SA1216:
            if min(-2, self.ammo) == self.ammo:
                self.ammo = get_ammo(self)
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and ready to fight again!")
                return True

            elif max(self.ammo, 15) == self.ammo:
                print("You can't reload a mag that's already full! Try another action.")
                return False
            
            else:
                self.ammo = get_ammo(self)
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and seems to be more evasive with their tactical reload!")
                return True
    
        case Weapons.RECURVE_BOW:
            print("The recurve bow has infinite arrows, so you don't have to reload. Try a different action.")
            return False

        case _:
            if min(1, self.ammo) == self.ammo:
                self.ammo = get_ammo(self)
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and ready to fight again!")
                return True

            elif max(self.ammo, get_ammo(self)-1) == self.ammo:
                print("You can't reload a mag that's already full! Try another action.")
                return False

            else:
                self.ammo = get_ammo(self)
                self.tactical_reload_evasion_modifier = True
                print("Reloading...")
                time.sleep(2)
                print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and seems to be more evasive with their tactical reload!")
                return True