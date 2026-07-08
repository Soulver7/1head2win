import time
from weapons_enum import Weapons
from ammo_mgmt import get_ammo


def reload_action(self):
    time.sleep(1)
    self.tactical_reload_evasion_modifier = False

    if self.weapon == Weapons.SA1216:
        if min(-2, self.ammo) == self.ammo:
            self.ammo = get_ammo(self.weapon)
            print("Reloading...")
            time.sleep(2)
            print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and ready to fight again!")

        elif max(self.ammo, 15) == self.ammo:
            print("You can't reload a mag that's already full! Try a different action")
            
        else:
            self.ammo = get_ammo(self.weapon)
            self.tactical_reload_evasion_modifier = True
            print("Reloading...")
            time.sleep(2)
            print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and seems to be more evasive with their tactical reload!")
    
    elif self.weapon == Weapons.RECURVE_BOW:
        print("The recurve bow has infinite arrows, so you don't have to reload. Try a different action.")

    else:
        if min(1, self.ammo) == self.ammo:
            self.ammo = get_ammo(self.weapon)
            print("Reloading...")
            time.sleep(2)
            print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and ready to fight again!")

        elif max(self.ammo, get_ammo(self.weapon)-1) == self.ammo:
            print("You can't reload a mag that's already full! Try a different action")

        else:
            self.ammo = get_ammo(self.weapon)
            self.tactical_reload_evasion_modifier = True
            print("Reloading...")
            time.sleep(2)
            print(f"Reload complete! {self.name} is back to a full {self.ammo}/{self.ammo}, and seems to be more evasive with their tactical reload!")