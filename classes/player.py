import random
from weapons import Weapons, get_ammo
from ranks import Ranks, init_evasion_calc

class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank # I could make this an enum to ensure it's validity

    def shoot(self, target): # General notes; Melee will take one turn to "move into range" / I'll simulate turns as one second each, so spray weapons will have to be tested for that
        raise NotImplementedError("Will be implemented by Player subclasses")
    
    def tactical_reload(self): # I could use this as a "defensive" action, where the player reloads and gains a temporary evasion boost / Be mindful of reload types per weapon / 
        # Melees can use this as a "wind up" to deal additional damage, but should be punished for overuse by giving opponent extra crit chance after first use, and escalate further with consecutive uses
        raise NotImplementedError("Will be implemented by Player subclasses")
    
    def empty_reload(self): # A punishment for forgetting to manage ammo. No evasion boost
        raise NotImplementedError("Will be implemented by Player subclasses")
    
    def __repr__(self):
        return f"Player(name={self.name}, rank={self.rank})"
    
class Medium(Player):
    def __init__(self, name, rank, weapon):
        super().__init__(name, rank)
        self.health = 250
        self.weapon = weapon # Make a function that checks for weapon validity and returns the appropriate enum value, or raises an error if invalid.
        self.evasion = init_evasion_calc(rank)
        self.ammo = get_ammo(weapon)

    def shoot(self, target):
        if self.ammo <= 0:
            print(f"{self.name} is out of ammo and cannot shoot!")
            return
    
