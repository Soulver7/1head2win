# 1Head2Win

A One-Versus-One Turn-Based RPG Based On "The Finals" By Embark Studios

### Table of Contents

- [About](#about)
    - [Tools](#tools)
    - [Lessons Learnt](#lessons-learnt)
- [Gameplay](#gameplay)
    - [Character Creation](#character-creation)
        - [Name](#name)
        - [Rank](#rank)
        - [Weight Class](#weight-class)
        - [Weapon](#weapon)
        - [Creation](#creation)
    - [Behind The Scenes](#behind-the-scenes)
        - [Ranged Player](#ranged-player)
        - [Melee Player](#melee-player)
        - [Weight Class Changes](#weight-class-changes)
    - [Battle](#battle)
        - [Turn Order](#turn-order)
        - [Rounds](#rounds)
            - [Round Logic](#round-logic)
            - [Example Round](#example-round)
    - [Post-Game](#post-game)
- [How To Set Up](#how-to-set-up)
- [Special Thanks](#special-thanks)


# About

My first solo project, started to complete the "Personal Project 1" course for Boot.dev. This project aims to faithfully recreate a one versus one battle in a video game named "The Finals" in an turn-based format. I used the version 10.9.0 of The Finals as the basis of my project, so the numbers may not correlate to the live version of the official game. I would also like to state that I have no affiliation with Embark Studios, or any of their associates. I am but a humble fan of their work.

### Tools

<img src='https://www.pngmart.com/files/23/Python-Logo-PNG-Clipart.png' width='100px'/> <img src='https://logospng.org/download/visual-studio-code/visual-studio-code-4096.png' width='100px'>

### Lessons Learnt

- Formatting data types
    - Turning integers into enums into attributes sure was an experience. I'm happy with how I handled it, and this experience has certainly taught me how to reverse engineer large amounts of previously written code. 
- Proper code formatting
    - From within each file, to folders for specificity. I made a large amount of progress in ensuring that my code is easy to read, and solidified my preferred route to do so.
- Objects
    - I feel this is the first time I've truly been able to work with objects at full comprehension of what everything was doing.
- Inputs
    - Learning how to implement inputs into functions was rather fun. It's surprisingly intuitive
    - Clamping. This is the first time I've had to be thorough with my inputs and outputs of functions and methods, due to people outside of myself being able to interact with my code.
- Text formatting
    - Formatting print text is surprisingly difficult. I got the hang of the time functions and spacing of lines by the end of this.

# Gameplay

## Character Creation

At the beginning players will choose various attributes of their character to go to battle with, such as:
- Name
- Rank
- Weight Class
- Weapon

### Name

Grabbing a player's name is rather simple.

```py
def player1_name_get(team1: str) -> str:
    time.sleep(2)
    print("Speaking of our contestants, let's hear their names!\n")
    time.sleep(2)
    return input(f"Representing {team1}, we have ")
```

### Rank

Rank is somewhat more complicated. It grabs an integer as an input.

```py
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
```

Then that integer goes into a function used to turn it into an enum value.

```py
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
```

After that, these enums then go into another function to return a player's evasion stat.

```py
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
```

### Weight Class

This one is a simpler integer to grab.

```py
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
```

### Weapon

The integer for the weight class will be used to determine which weapons you can select from. I handled the input the same way I did for the previous two.

```py
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
```

I had to fix some of the weapon names due to the restrictions of Enum names, so that's why it shows a few changes to the initial weapons list after it was created.

### Creation

Once we have all of the components of a player, all that's left is to put them together.

```py
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
```

This process is then repeated again to create the second player as well.

## Behind The Scenes

In the previous section, you may've been wondering how the player characters actually work, and where all of the inputs we made are actually going. Here's where the player objects come in.

### Ranged Player

This is the base class for any ranged weapon in the game, side from the Throwing Knives due to their logic working better with our next category. This naturally makes it have the highest volume of weapons to account for.

```py
class Ranged_Player: # Template for ranged player classes
    def __init__(self, name: str, rank: int):
        self.name = name
        self.rank = is_valid_rank(rank) # Checks if the number selected is valid, and assigns rank to the player based on the number chosen
        self.evasion = init_evasion_calc(self) # Chooses from a pool of evasion values based on the player's rank
        self.tactical_reload_evasion_modifier = False # Adds a temporary +1 evasion boost in exchange for skipping a turn for an earlier reload
        self.is_faster = False # Determines start order
        self.rounds_won = 0 # Tracks the score for the best of three

    def shoot(self, target): # Sorts by weapon type, and handles the shooting logic to calculate damage
        if self.tactical_reload_evasion_modifier:
            time.sleep(2)
            self.tactical_reload_evasion_modifier = False
            print(f"{self.name} has finished their tactical reload, and is now back to their normal evasion")
        
        shoot_dmg_calc(self, target)
    
    def reload(self) -> bool: # Cannot reload at full ammo. It will make you reselect action if attempted. This is also how self.tatical_reload_evasion_modifier is set to True
        return reload_action(self)
    
    def quick_melee(self, target): # A strike that does 40 damage on hit. Proves useful for low health, low ammo situations
        if self.tactical_reload_evasion_modifier:
            time.sleep(2)
            self.tactical_reload_evasion_modifier = False
            print(f"{self.name} has finished their tactical reload, and is now back to their normal evasion")

        time.sleep(2)
        accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hit_chance = random.choice(accuracy_pool)
        damage = 40

        if hit_chance >= evasion_modifiers(target):
            target.health -= damage
            print(f"{self.name} delivers a swift strike to {target.name} for {damage} damage! {target.name} has {zero_health_adjustment(target)} health remaining.")

        else:
            print(f"{self.name} attempts a quick strike, but {target.name} dodges out of the way!")
    
    def action_list(self) -> list: # Handles the printing of actions at time of input selection
        if self.ammo == get_ammo(self):
            return ["Shoot", "Quick Melee"]

        else:
            return ["Shoot", "Quick Melee", "Reload"]
```

### Melee Player

This is the other base class. This one is to handle any melee weapon logic, which can get surprisingly complex the further you get into it.

```py
class Melee_Player: # Template for melee player classes
    def __init__(self, name: str, rank: int):
        self.name = name
        self.rank = is_valid_rank(rank)
        self.evasion = init_evasion_calc(self) + 1 # All melee players start with a +1 to their evasion to compensate for having to move into melee range
        self.in_melee_range = False # Balances the higher evasion and damage output of melee weapons
        self.melee_rep_count = 0 # Handles various weapon combos that require multiple turns to execute
        self.alt_stance = False # Handles the attacks that require a "wind-up" turn, or defensive stances that reduce damage taken or deflect attacks. Nullifes the evasion bonus for melee players when True
        self.is_faster = False
        self.rounds_won = 0

    def move_in(self, target) -> bool: # Simulates the movement between the two parties to properly engage a melee distanced fight. It's how self.in_melee_range is set to True
        time.sleep(2)
        if (self.evasion + random.randint(-2, 2)) > (target.evasion + random.randint(-2, 2)): # Adds variability to the "move in" action's success rate
            self.in_melee_range = True

            if target.weapon in melee_list():
                target.in_melee_range = True
                
            print(f'{self.name} is now in range! Let the beatdown commence!')
            return True
        
        else:
            print(f"{target.name} gracefully moves about the arena, thwarting {self.name}'s attempts at getting in close!")
            return False

    def main_melee(self, target): # The left click function of the selected melee weapon
        main_melee_dmg_calc(self, target)

    def alt_melee(self, target): # The right click function of the selected melee weapon
        alt_melee_action(self, target)
    
    def quick_melee(self, target): # Ignores the need to have the self.in_melee_range set to True, so that Melee players won't be penalized for the same action ranged players have access to
        if self.alt_stance:
                time.sleep(2)
                self.alt_stance = False
                print(f'{self.name} drops their stance, and is now on the offensive!')

        time.sleep(2)
        accuracy_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hit_chance = random.choice(accuracy_pool)
        damage = 40

        if hit_chance >= evasion_modifiers(target):
            target.health -= damage
            print(f"{self.name} delivers a swift strike to {target.name} for {damage} damage! {target.name} has {zero_health_adjustment(target)} health remaining.")

        else:
            print(f"{self.name} attempts a quick strike, but {target.name} dodges out of the way!")
    
    def action_list(self) -> list:
        if not self.in_melee_range:
            return ["Move In", "Quick Melee"]
        
        else:
            return ["Main Attack", "Alternate Stance", "Quick Melee"]
```

### Weight Class Changes

Here's an example of a Heavy class player that uses the ranged player base template.

```py
class Ranged_Heavy(Ranged_Player):
    def __init__(self, name: str, rank: int, weapon: int):
        super().__init__(name, rank)
        self.id = 2 # Managed classes from input
        self.evasion = init_evasion_calc(self) - 1 # Evasion changes depending on weight and choice of range or melee
        self.health = 350
        self.weapon = is_valid_weapon(self.id, weapon) # Checks if the number fits withing the Weapon enum's criteria for the role and class, and assigns it if it is
        self.ammo = get_ammo(self) # Gives the selected weapon's full ammo count
        if self.weapon == Weapons.KS_23:
            self.reload_chain = False # Checks if tactical reload reloads one or two slugs on KS-23
```

## Battle

Now here's where the fun begins. Both players are put into a simulation of a one-versus-one fight, and there's several mechanisms that make that function.

### Turn Order

I use both players' evasion stats to determine who goes first. If they are both the same, it comes down to a fifty/fifty chance to go first.

```py
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
```

Then I use another function to simulate that start without having to constantly check every round for the .is_faster boolean.

```py
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
```

### Rounds

#### Round Logic

Before we get into the rounds proper, I must explain how I handle the actual fighting first. What I do is I take the input of the person who moves first that round via an integer. Then, I use that integer to determine which method will be used by the player class. After that, I check to see if the slower player has any health remaining, and if they do, I let them do the same.

```py
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
```

#### Example Round

With that information out of the way, we'll use Round Two as an example. It first displays the current score with the results of the first round. After that, it displays a message that shows who will go first for the round, and then displays their actions. Once someone looses all of their health, a message will be displayed that indicates the end of the round, and the current state of the series.

```py
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
```

## Post-Game

After everything is said and done, I have a system that facilitates the ability to replay.

```py
def replay_prompt(player1, player2) -> int:
    y_list = [player1.name, player2.name, "Both", "Neither"]

    while True:
        time.sleep(2)
        print("\nWould you like to play another round of 1Head2Win? [Y/N]")
        answer = input()

        if answer.capitalize() == "Y":
            while True:
                try:
                    time.sleep(2)
                    print("\nWould you like to reuse your characters?")
                    time.sleep(2)
                    print("\n===========")

                    for i, choice in enumerate(y_list):
                        print(f"{choice} = {i+1}")
                    
                    print("===========\n")
                    answer_int = int(input())

                    if min(max(1, answer_int), 4) != answer_int:
                        print("The number must be between 1 and 4.")
                        continue

                    return answer_int
                
                except ValueError:
                    print("The input must be a number.")
        
        elif answer.capitalize() == "N":
            print("That wraps up all the matches we had scheduled for today.")
            time.sleep(2)
            print("Thank you to everyone who tuned in, and we'll see you in the next broadcast!")
            time.sleep(2)
            print("\n--- Signal lost ---\n")
            return 5
        
        else:
            print("Input must be either Y or N.")
            continue
```

If you choose to do so, you can reuse either both, neither, or one of the player characters from the previous series, saving time in between games.

```py
answer_int = replay_prompt(player1, player2)

        if answer_int == 1:
            player1, player2 = intro(player1)
        
        elif answer_int == 2:
            player1, player2 = intro(None, player2)
        
        elif answer_int == 3:
            player1, player2 = intro(player1, player2)
        
        elif answer_int == 4:
            player1, player2 = intro()
        
        elif answer_int == 5:
            playing = False
```

# How To Set Up

1. Install Python 3.12.2 or higher

2. Clone the repository to your local machine:

```
git clone https://github.com/Soulver7/1Head2Win.git
```

3. Change your directory to "1Head2Win":

```
cd 1Head2Win
```

4. Run the code using main.py:

```py
python3 main.py
```

5. Enjoy

# Special Thanks

I'd love to credit two groups for the massive amount of help for this project

- The team at Boot.Dev
    - I learned many fundamental coding skils through their course work, and they're the main reason why I love coding today
- Michael Short a.k.a. mshortcodes
    - Micael's project "Dragon Slayer" was a massive inspiration to how I formatted my own project, and I would've been lost for a good amount of time without his work to guide me.