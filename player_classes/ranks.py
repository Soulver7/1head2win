from enum import Enum
import random


class Ranks(Enum):
    UNRANKED = 1
    BRONZE = 2
    SILVER = 3
    GOLD = 4
    PLATINUM = 5
    DIAMOND = 6
    RUBY = 7

def get_rank_evasion_pool(rank):
    match rank:
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
        case Ranks.RUBY:
            self.evasion = random.choice(get_rank_evasion_pool(Ranks.RUBY))
        case _:
            raise ValueError("Invalid rank provided. Must be one of the defined Ranks enum values.")