import random
from enum import Enum

class Ranks(Enum):
    UNRANKED = 1
    BRONZE = 2
    SILVER = 3
    GOLD = 4
    PLATINUM = 5
    DIAMOND = 6
    EMERALD = 7
    RUBY = 8

def get_rank_evasion_pool(rank):
    match rank:
        case Ranks.UNRANKED:
            return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        case Ranks.BRONZE:
            return [1, 2, 3]
        case Ranks.SILVER:
            return [2, 3, 4]
        case Ranks.GOLD:
            return [3, 4, 5]
        case Ranks.PLATINUM:
            return [5, 6, 7]
        case Ranks.DIAMOND:
            return [6, 7, 8]
        case Ranks.EMERALD:
            return [7, 8, 9]
        case Ranks.RUBY:
            return [8, 9, 10]
        case _:
            raise ValueError("Invalid rank provided to get_rank_evasion_pool")
        
def init_evasion_calc(self, rank):
    match rank:
        case Ranks.UNRANKED:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.UNRANKED))
        case Ranks.BRONZE:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.BRONZE))
        case Ranks.SILVER:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.SILVER))
        case Ranks.GOLD:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.GOLD))
        case Ranks.PLATINUM:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.PLATINUM))
        case Ranks.DIAMOND:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.DIAMOND))
        case Ranks.EMERALD:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.EMERALD))
        case Ranks.RUBY:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.RUBY))
        case _:
            raise ValueError("Invalid rank provided to init_evasion_calc")