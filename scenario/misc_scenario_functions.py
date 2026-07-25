import time, random
from player_information.weapons.misc_weapon_functions import melee_list
from player_information.weapons.ammo_mgmt import get_ammo


def team_names_list() -> list:
    return [
        "The Big Splash",
        "The Boundless", 
        "The High Notes", 
        "The Jet Setters", 
        "The Kingfish",
        "The Live Wires",
        "The Mighty",
        "The Powerhouses",
        "The Overdogs",
        "The Retros",
        "The Socialites",
        "The Shock and Awe",
        "The Steamrollers",
        "The Tough Shells",
        "The Ultra-Rares",
        "The Vouges"
        ]

def team_names_no_overlap(team_names_list: list, team1: str) -> list:
    while(team1 in team_names_list):
        team_names_list.remove(team1)
        
    return team_names_list[random.randint(0, 14)]

def action_int_check(player) -> int:
    while True:
        try:
            action_int = int(input(f"{player.name}'s turn: "))
            if player.weapon not in melee_list():
                if min(max(1, action_int), 3) != action_int:
                    time.sleep(2)
                    print("\nThe number must be between 1 and 3.")
                    continue
            
            else:
                if player.in_melee_range:
                    if min(max(1, action_int), 3) != action_int:
                        time.sleep(2)
                        print("\nThe number must be between 1 and 3.")
                        continue

                else:
                    if min(max(1, action_int), 2) != action_int:
                        time.sleep(2)
                        print("\nThe number must be between 1 and 2.")
                        continue
            
            return action_int
        
        except ValueError:
            print("\nThe input must be a number.")

def take_action(player, action_int, target):
    invalid = True

    while invalid:
        if player.weapon not in melee_list():
            if action_int == 1:
                player.shoot(target)
                invalid = False
        
            elif action_int == 2:
                if player.reload():
                    continue

                else:
                    invalid = False
        
            elif action_int == 3:
                player.quick_melee(target)
                invalid = False
    
        else:
            if player.in_melee_range:
                if action_int == 1:
                    player.main_melee(target)
                    invalid = False
            
                elif action_int == 2:
                    player.alt_melee(target)
                    invalid = False
            
                elif action_int == 3:
                    player.quick_melee(target)
                    invalid = False
        
            else:
                if action_int == 1:
                    if player.move_in(target):
                        continue

                    else:
                        invalid = False
            
                elif action_int == 2:
                    player.quick_melee(target)
                    invalid = False

def reset_player(self):
    if self.id == 1:
        self.health = 250
        self.ammo = get_ammo(self)
    
    elif self.id == 2:
        self.health = 350
        self.ammo = get_ammo(self)
    
    elif self.id == 3:
        self.id = 150
        self.ammo = get_ammo(self)
    
    elif self.id == 4:
        self.health = 250
        self.in_melee_range = False
        self.melee_rep_count = 0
        self.alt_stance = False
    
    elif self.id == 5:
        self.health = 350
        self.in_melee_range = False
        self.melee_rep_count = 0
        self.alt_stance = False
    
    elif self.id == 6:
        self.health = 150
        self.in_melee_range = False
        self.melee_rep_count = 0
        self.alt_stance = False


def round_logic(first_player, second_player):
    reset_player(first_player)
    reset_player(second_player)

    while first_player.health != 0 and second_player.health != 0:
        time.sleep(2)
        print("\n====================")

        for i, ability in enumerate(first_player.action_list()):
            print(f"{ability} = {i+1}")
            
        print("=====================\n")
        action_int = action_int_check(first_player)
        print("")
        take_action(first_player, action_int, second_player)

        if second_player.health != 0:
            time.sleep(2)
            print("\n====================")

            for i, ability in enumerate(second_player.action_list()):
                print(f"{ability} = {i+1}")
            
            print("===================\n")
            action_int = action_int_check(second_player)
            print("")
            take_action(second_player, action_int, first_player)