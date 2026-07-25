from scenario.intro import intro
from scenario.bo3_series import bo3_series
from scenario.replay_prompt import replay_prompt


def main():
    playing = True
    player1, player2 = intro()

    while playing:
        bo3_series(player1, player2)
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


main()