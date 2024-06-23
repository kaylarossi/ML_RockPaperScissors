# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    
    opponent_history.append(prev_play)
    guess = "R"

    if len(opponent_history) < 5:
        #cycle through R,P,S -- alone beats quincy and mrugesh over 60%
        if opponent_history[-1] == "R":
            guess = "P"
        elif opponent_history[-1] == "P":
            guess = "S"
        else:
            guess = "R"

    moves={'P':'R', 'R':'S', 'S':'P'}

    if len(opponent_history) >= 5:
        play_order = [''.join(opponent_history[k:k+5]) for k,v in enumerate(opponent_history[:-4])]
        possible_play = [''.join([*opponent_history[-4:],v]) for v in ['S','P','R'] ]
        
        order = {k: play_order.count(k) for k in possible_play}
        predict = max(order, key=order.get)[-1]
        guess = moves[predict]

   #look at most used then respond accordingly
    
        #R_val = opponent_history.count('R')
       # P_val = opponent_history.count('P')
        #S_val = opponent_history.count('S')
       # played={'R':R_val, 'P':P_val, 'S':S_val}
        #highest key(s)
       # max_key=[key for key, value in played.items() if value == max(played.values())][0] 
       # if 'R' in max_key:
       #     guess = 'P'
       # elif 'S' in max_key:
       #     guess = 'R'
       # else:
       #     guess = 'S'

    
    return guess




