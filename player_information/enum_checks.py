from player_information.ranks import Ranks
from player_information.weapons.weapons_enum import Weapons


def is_valid_rank(rank: int) -> Ranks:
    if min(max(0, rank), 7) == rank:
        return Ranks(rank)
    
    else:
        raise ValueError("That rank isn't valid. Please choose an integer between 0 and 7.")

def is_valid_weapon(player_class: int, weapon: int) -> Weapons:
    if player_class == 1 and min(max(0, weapon), 11) == weapon:
        return Weapons(weapon)
    
    elif player_class == 2 and min(max(12, weapon), 21) == weapon:
        return Weapons(weapon)
    
    elif player_class == 3 and min(max(22, weapon), 31) == weapon:
        return Weapons(weapon)
    
    elif player_class == 4 and min(max(32, weapon), 33) == weapon:
        return Weapons(weapon)
    
    elif player_class == 5 and min(max(34, weapon), 35) == weapon:
        return Weapons(weapon)
    
    elif player_class == 6 and min(max(36, weapon), 38) == weapon:
        return Weapons(weapon)
    
    else:
        raise ValueError(f"That weapon isn't valid for the {player_class} class.")