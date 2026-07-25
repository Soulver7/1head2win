import time, random
from scenario.misc_scenario_functions import round_logic


def bo3_series(player1, player2):
    faster_player(player1, player2)
    round_manager(player1, player2)
    series_end(player1, player2)


def faster_player(player1, player2):
    time.sleep(2)

    if player1.evasion > player2.evasion:
        player1.is_faster = True
    
    elif player1.evasion < player2.evasion:
        player2.is_faster = True
    
    else:
        coin = random.randint(1, 2)

        if coin == 1:
            player1.is_faster = True
        
        elif coin == 2:
            player2.is_faster = True

def round_manager(player1, player2):
    if player1.is_faster:
        round1(player1, player2, player1, player2)
        round2(player2, player1, player1, player2)

        if player1.rounds_won < 2 and player2.rounds_won < 2:
            round3(player1, player2, player1, player2)
    
    elif player2.is_faster:
        round1(player2, player1, player1, player2)
        round2(player1, player2, player1, player2)

        if player1.rounds_won < 2 and player2.rounds_won < 2:
            round3(player2, player1, player1, player2)

def round1(fast_player, slow_player, player1, player2):
    time.sleep(2)
    print("\n--- Round One ---")
    time.sleep(2)
    print(f"{player1.name} - {player1.rounds_won} | {player2.name} - {player2.rounds_won}")
    time.sleep(2)
    print(f"\nIt seems {fast_player.name} is making the first move!")
    round_logic(fast_player, slow_player)

    if fast_player.health == 0:
        slow_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{fast_player.name} has been eliminated!")
        time.sleep(2)
        print(f"{slow_player.name} wins this round. Will they be able to keep this momentum up?")
    
    elif slow_player.health == 0:
        fast_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{slow_player.name} has been eliminated!")
        time.sleep(2)
        print(f"{fast_player.name} wins this round. Will they be able to keep this momentum up?")

def round2(slow_player, fast_player, player1, player2):
    time.sleep(2)
    print("\n--- Round Two ---")
    time.sleep(2)
    print(f"{player1.name} - {player1.rounds_won} | {player2.name} - {player2.rounds_won}")
    time.sleep(2)
    print(f"\n{slow_player.name} seems to be taking the initiative, and is starting our combat off this round!")
    round_logic(slow_player, fast_player)

    if fast_player.health == 0 and slow_player.rounds_won == 0:
        slow_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{fast_player.name} has been eliminated!")
        time.sleep(2)
        print(f"{slow_player.name} has tied the score up! This last round will be a nail biter.")
    
    elif fast_player.health == 0 and slow_player.rounds_won == 1:
        slow_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{fast_player.name} has been eliminated!")

    elif slow_player.health == 0 and fast_player.rounds_won == 0:
        fast_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{slow_player.name} has been eliminated!")
        time.sleep(2)
        print(f"{fast_player.name} has tied the score up! This last round will be a nail biter.")
    
    elif slow_player.health == 0 and fast_player.rounds_won == 1:
        fast_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{slow_player.name} has been eliminated!")
    
def round3(fast_player, slow_player, player1, player2):
    time.sleep(2)
    print("\n--- Round Three ---")
    time.sleep(2)
    print(f"{player1.name} - {player1.rounds_won} | {player2.name} - {player2.rounds_won}")
    time.sleep(2)
    print(f"\n{fast_player.name} has regained their gusto, and starts this round strong!")
    round_logic(fast_player, slow_player)

    if fast_player.health == 0:
        slow_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{fast_player.name} has been eliminated!")
    
    elif slow_player.health == 0:
        fast_player.rounds_won += 1
        time.sleep(2)
        print(f"\n{slow_player.name} has been eliminated!")

def series_end(player1, player2):
    time.sleep(2)

    if player1.rounds_won == 2:
        if player2.rounds_won == 0:
            print(f"\n{player1.name} has absolutely dominated this match!")
            time.sleep(2)
            print("They certainly put their all into it. A well executed effort indeed.")
            time.sleep(2)
            print(f"Better luck next time to {player2.name}. With a little more practice and analysis, they could take the win.")
        
        elif player2.rounds_won == 1:
            print(f"\n{player1.name} has narrowly grasped victory!")
            time.sleep(2)
            print("I'm on the edge on my seat! That was a thrilling battle from both of our contestants.")
            time.sleep(2)
            print(f"Let's not forget the effort of {player2.name}! Good showing from them as well.")
        
    elif player2.rounds_won == 2:
        if player1.rounds_won == 0:
            print(f"\n{player2.name} has absolutely dominated this match!")
            time.sleep(2)
            print("They certainly put their all into it. A well executed effort indeed.")
            time.sleep(2)
            print(f"Better luck next time to {player1.name}. With a little more practice and analysis, they could take the win in the future.")
        
        elif player1.rounds_won == 1:
            print(f"\n{player2.name} has narrowly grasped victory!")
            time.sleep(2)
            print("I'm on the edge on my seat! That was a thrilling battle from both of our contestants.")
            time.sleep(2)
            print(f"Let's not forget the effort of {player1.name}! Good showing from them as well.")