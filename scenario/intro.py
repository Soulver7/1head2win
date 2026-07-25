import time, random
from scenario.misc_scenario_functions import team_names_list, team_names_no_overlap
from player_information.ranks import Ranks
from player_information.weapons.weapons_enum import Weapons
from player_information.classes.medium import Ranged_Medium, Melee_Medium
from player_information.classes.heavy import Ranged_Heavy, Melee_Heavy
from player_information.classes.light import Ranged_Light, Melee_Light


def intro(player1=None, player2=None) -> tuple:
    team1 = team_names_list()[random.randint(0, 15)]
    team2 = team_names_no_overlap(team_names_list(), team1)

    if player1 == None and player2 == None:
        intro_start()
    
    if player1 == None:
        player1_name = player1_name_get(team1)
        player1_rank_int = player1_rank_get(player1_name)
        player1_class_int = player1_class_get(player1_name)
        player1_weapon_int = player1_weapon_get(player1_name, player1_class_int)
        player1 = make_player1(player1_name, player1_rank_int, player1_class_int, player1_weapon_int)
    
    if player2 == None:
        player2_name = player2_name_get(team2, player1)
        player2_rank_int = player2_rank_get(player2_name)
        player2_class_int = player2_class_get(player2_name)
        player2_weapon_int = player2_weapon_get(player2_name, player2_class_int)
        player2 = make_player2(player2_name, player2_rank_int, player2_class_int, player2_weapon_int)
    
    intro_end(player1, player2)
    return player1, player2


def intro_start():
    print("\n--- Welcome to 1Head2Win! ---\n")
    time.sleep(2)
    print("In this limited time game mode, we'll be appreciating the finer aspects of solo combat in our arena.")
    time.sleep(2)
    print("Today we are going to be witnessing a battle of wits and grit between two individuals. Deathmatch style!")
    time.sleep(2)
    print("Our contestants will be competing in a best of three format. Whoever gets the first elimination will be rewarded the round!")
    time.sleep(2)
    print("These two will only be equipped with their weapons. Gadgets and Specializations are off limits in this format.")

def player1_name_get(team1: str) -> str:
    time.sleep(2)
    print("Speaking of our contestants, let's hear their names!\n")
    time.sleep(2)
    return input(f"Representing {team1}, we have ")

def player1_rank_get(player1_name: str) -> int:
    time.sleep(2)
    print(f"\nAs for {player1_name}'s rank, they are-")

    while True:
        try:
            time.sleep(2)
            print(f"(To choose your rank, please enter the corresponding number)")
            time.sleep(2)
            print("\n============")
            rank_list = [r.name for r in Ranks]

            for i, rank in enumerate(rank_list):
                print(f"{rank} = {i+1}")

            print("============\n")
            rank_int = int(input("Rank number: "))

            if min(max(1, rank_int), 7) != rank_int:
                print("The number must be between 1 and 7.")
                continue

            return rank_int
        
        except ValueError:
            print("The input must be a number.")

def player1_class_get(player1_name: str) -> int:
    time.sleep(2)
    classes = ["Ranged Medium", "Ranged Heavy", "Ranged Light", "Melee Medium", "Melee Heavy", "Melee Light"]
    print(f"\nAnd for {player1_name}'s class, they play-")

    while True:
        try:
            time.sleep(2)
            print("(Same process as last time)")
            time.sleep(2)
            print("\n=================")

            for i, role in enumerate(classes):
                print(f"{role} = {i+1}")   

            print("=================\n")
            class_int = int(input("Class number: "))

            if min(max(1, class_int), 6) != class_int:
                print("The number must be between 1 and 6.")
                continue

            return class_int
        
        except ValueError:
            print("The input must be a number.")

def player1_weapon_get(player1_name: str, player1_class_int) -> int:
    time.sleep(2)
    print(f"\nToday {player1_name} brought their famous-")

    while True:
        try:
            time.sleep(2)
            print("(You know what to do by now)")
            time.sleep(2)
            print("\n===================")
            weapons_list = [w.name for w in Weapons]

            if player1_class_int == 1:
                weapons = weapons_list[:11]
                weapons[1] = "CB-01 REPEATER"
                weapons[3] = "CHIMERA-XB"
                weapons[4] = "CL-40"
                weapons[9] = "PIKE-556"
                weapons[10] = "R.357"

            elif player1_class_int == 2:
                weapons = weapons_list[11:21]
                weapons[0] = ".50 Akimbo"
                weapons[3] = "KS-23"
                weapons[9] = "SHAK-50"
            
            elif player1_class_int == 3:
                weapons = weapons_list[21:31]
                weapons[0] = "93R"
                weapons[1] = "ARN-220"
                weapons[7] = "SR-84"
                weapons[9] = "XP-54"
            
            elif player1_class_int == 4:
                weapons = weapons_list[31:33]
            
            elif player1_class_int == 5:
                weapons = weapons_list[33:35]
            
            elif player1_class_int == 6:
                weapons = weapons_list[35:38]
            
            for i, weapon in enumerate(weapons):
                print(f"{weapon.replace('_', ' ')} = {i+1}")
            
            print("===================\n")
            weapon_int = int(input("Weapon Number: "))

            if player1_class_int == 1:
                if min(max(1, weapon_int), 11) != weapon_int:
                    print("The number must be between 1 and 11.")
                    continue
            
            elif player1_class_int == 2:
                if min(max(1, weapon_int), 10) != weapon_int:
                    print("The number must be between 1 and 10.")
                    continue
            
            elif player1_class_int == 3:
                if min(max(1, weapon_int), 10) != weapon_int:
                    print("The number must be between 1 and 10.")
                    continue
            
            elif player1_class_int == 4:
                if min(max(1, weapon_int), 2) != weapon_int:
                    print("The number must be between 1 and 2.")
                    continue
            
            elif player1_class_int == 5:
                if min(max(1, weapon_int), 2) != weapon_int:
                    print("The number must be between 1 and 2.")
                    continue
            
            elif player1_class_int == 6:
                if min(max(1, weapon_int), 3) != weapon_int:
                    print("The number must be between 1 and 3.")
                    continue
            
            return weapon_int
        
        except ValueError:
            print("The input must be a number.")

def make_player1(player1_name: str, player1_rank_int, player1_class_int, player1_weapon_int):
    if player1_class_int == 1:
        return Ranged_Medium(player1_name, player1_rank_int, player1_weapon_int)
    
    elif player1_class_int == 2:
        return Ranged_Heavy(player1_name, player1_rank_int, player1_weapon_int+11)
    
    elif player1_class_int == 3:
        return Ranged_Light(player1_name, player1_rank_int, player1_weapon_int+21)
    
    elif player1_class_int == 4:
        return Melee_Medium(player1_name, player1_rank_int, player1_weapon_int+31)
    
    elif player1_class_int == 5:
        return Melee_Heavy(player1_name, player1_rank_int, player1_weapon_int+33)
    
    elif player1_class_int == 6:
        return Melee_Light(player1_name, player1_rank_int, player1_weapon_int+35)

def player2_name_get(team2: str, player1) -> str:
    time.sleep(2)
    print(f"\nEnough about {player1.name}! We have another promising contestent as well!")
    time.sleep(2)
    return input(f"Representing {team2}, we have ")

def player2_rank_get(player2_name: str) -> int:
    time.sleep(2)
    print(f"For {player2_name}'s rank, they are-")

    while True:
        try:
            time.sleep(2)
            print("\n============")
            rank_list = [r.name for r in Ranks]

            for i, rank in enumerate(rank_list):
                print(f"{rank} = {i+1}")

            print("============\n")
            rank_int = int(input("Rank number: "))

            if min(max(1, rank_int), 7) != rank_int:
                print("The number must be between 1 and 7.")
                continue

            return rank_int
        
        except ValueError:
            print("The input must be a number.")

def player2_class_get(player2_name: str) -> int:
    time.sleep(2)
    classes = ["Ranged Medium", "Ranged Heavy", "Ranged Light", "Melee Medium", "Melee Heavy", "Melee Light"]
    print(f"\nAs for {player2_name}'s class, they play-")

    while True:
        try:
            time.sleep(2)
            print("\n=================")

            for i, role in enumerate(classes):
                print(f"{role} = {i+1}")   

            print("=================\n")
            class_int = int(input("Class number: "))

            if min(max(1, class_int), 6) != class_int:
                print("The number must be between 1 and 6.")
                continue

            return class_int
        
        except ValueError:
            print("The input must be a number.")

def player2_weapon_get(player2_name: str, player2_class_int) -> int:
    time.sleep(2)
    print(f"\nToday {player2_name} brought their trusty-")

    while True:
        try:
            time.sleep(2)
            print("\n===================")
            weapons_list = [w.name for w in Weapons]

            if player2_class_int == 1:
                weapons = weapons_list[:11]
                weapons[1] = "CB-01 REPEATER"
                weapons[3] = "CHIMERA-XB"
                weapons[4] = "CL-40"
                weapons[9] = "PIKE-556"
                weapons[10] = "R.357"

            elif player2_class_int == 2:
                weapons = weapons_list[11:21]
                weapons[0] = ".50 Akimbo"
                weapons[3] = "KS-23"
                weapons[9] = "SHAK-50"
            
            elif player2_class_int == 3:
                weapons = weapons_list[21:31]
                weapons[0] = "93R"
                weapons[1] = "ARN-220"
                weapons[7] = "SR-84"
                weapons[9] = "XP-54"
            
            elif player2_class_int == 4:
                weapons = weapons_list[31:33]
            
            elif player2_class_int == 5:
                weapons = weapons_list[33:35]
            
            elif player2_class_int == 6:
                weapons = weapons_list[35:38]
            
            for i, weapon in enumerate(weapons):
                print(f"{weapon.replace("_", " ")} = {i+1}")
            
            print("===================\n")
            weapon_int = int(input("Weapon Number: "))

            if player2_class_int == 1:
                if min(max(1, weapon_int), 11) != weapon_int:
                    print("The number must be between 1 and 11.")
                    continue
            
            elif player2_class_int == 2:
                if min(max(1, weapon_int), 10) != weapon_int:
                    print("The number must be between 1 and 10.")
                    continue
            
            elif player2_class_int == 3:
                if min(max(1, weapon_int), 10) != weapon_int:
                    print("The number must be between 1 and 10.")
                    continue
            
            elif player2_class_int == 4:
                if min(max(1, weapon_int), 2) != weapon_int:
                    print("The number must be between 1 and 2.")
                    continue
            
            elif player2_class_int == 5:
                if min(max(1, weapon_int), 2) != weapon_int:
                    print("The number must be between 1 and 2.")
                    continue
            
            elif player2_class_int == 6:
                if min(max(1, weapon_int), 3) != weapon_int:
                    print("The number must be between 1 and 3.")
                    continue
            
            return weapon_int
        
        except ValueError:
            print("The input must be a number.")

def make_player2(player2_name: str, player2_rank_int, player2_class_int, player2_weapon_int):
    if player2_class_int == 1:
        return Ranged_Medium(player2_name, player2_rank_int, player2_weapon_int)
    
    elif player2_class_int == 2:
        return Ranged_Heavy(player2_name, player2_rank_int, player2_weapon_int+11)
    
    elif player2_class_int == 3:
        return Ranged_Light(player2_name, player2_rank_int, player2_weapon_int+21)
    
    elif player2_class_int == 4:
        return Melee_Medium(player2_name, player2_rank_int, player2_weapon_int+31)
    
    elif player2_class_int == 5:
        return Melee_Heavy(player2_name, player2_rank_int, player2_weapon_int+33)
    
    elif player2_class_int == 6:
        return Melee_Light(player2_name, player2_rank_int, player2_weapon_int+35)

def intro_end(player1, player2):
    time.sleep(2)
    print("\nIt seems that both contestants have finished up their preparations, and the crowd is in an uproar!")
    time.sleep(2)
    print(f"I'm certainly interested to see how both {player1.name} and {player2.name} will hold up against each other. Let's get to it!")