from ranks import Ranks
from weapons.weapons_enum import Weapons


def is_valid_rank(rank: int) -> Ranks:
    if min(max(0, rank), 7) == rank:
        return Ranks(rank)
    
    else:
        raise ValueError("That rank isn't valid. Please choose an integer between 0 and 7.")

def is_valid_weapon(player_class: str, weapon: int) -> Weapons:
    if player_class == "Ranged_Medium" and min(max(0, weapon), 11) == weapon:
        return Weapons(weapon)
    elif player_class == "Ranged_Heavy" and min(max(12, weapon), 21) == weapon:
        return Weapons(weapon)
    elif player_class == "Ranged_Light" and min(max(22, weapon), 31) == weapon:
        return Weapons(weapon)
    elif player_class == "Melee_Medium" and min(max(32, weapon), 33) == weapon:
        return Weapons(weapon)
    elif player_class == "Melee_Heavy" and min(max(34, weapon), 35) == weapon:
        return Weapons(weapon)
    elif player_class == "Melee_Light" and min(max(36, weapon), 38) == weapon:
        return Weapons(weapon)
    else:
        raise ValueError(f"That weapon isn't valid for the {player_class} class.")