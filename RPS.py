# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    
    opponent_history.append(prev_play)

    guess = "S"
    if len(opponent_history) > 2:
        #guess = opponent_history[-2]
        #cycle through R,P,S
        if opponent_history[-1] == "R":
            guess = "P"
        elif opponent_history[-1] == "P":
            guess = "S"
        else:
            guess = "R"


    return guess
