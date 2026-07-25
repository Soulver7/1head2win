import time

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