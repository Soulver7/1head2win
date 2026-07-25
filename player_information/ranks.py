import random
from enum import Enum


class Ranks(Enum):
    UNRANKED = 1
    BRONZE = 2
    SILVER = 3
    GOLD = 4
    PLATINUM = 5
    DIAMOND = 6
    RUBY = 7

def get_rank_evasion_pool(self) -> list:
    match self.rank:
        case Ranks.UNRANKED:
            return [1, 2, 3, 4, 5, 6, 7, 8]
        
        case Ranks.BRONZE:
            return [1, 2, 3]
        
        case Ranks.SILVER:
            return [2, 3, 4]
        
        case Ranks.GOLD:
            return [3, 4, 5]
        
        case Ranks.PLATINUM:
            return [4, 5, 6]
        
        case Ranks.DIAMOND:
            return [5, 6, 7]
        
        case Ranks.RUBY:
            return [6, 7, 8]
        
        case _:
            raise ValueError("Invalid rank provided. Must be one of the defined Ranks enum values.")
        
def init_evasion_calc(self) -> int:
    match self.rank:
        case Ranks.UNRANKED:
            return random.choice(get_rank_evasion_pool(self))
        
        case Ranks.BRONZE:
            return random.choice(get_rank_evasion_pool(self))
        
        case Ranks.SILVER:
            return random.choice(get_rank_evasion_pool(self))
        
        case Ranks.GOLD:
            return random.choice(get_rank_evasion_pool(self))
        
        case Ranks.PLATINUM:
            return random.choice(get_rank_evasion_pool(self))
        
        case Ranks.DIAMOND:
            return random.choice(get_rank_evasion_pool(self))
        
        case Ranks.RUBY:
            return random.choice(get_rank_evasion_pool(self))
        
        case _:
            raise ValueError("Invalid rank provided. Must be one of the defined Ranks enum values.")