# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

#def player(prev_play, opponent_history=[]):
#    opponent_history.append(prev_play)
#
#    guess = "R"
#    if len(opponent_history) > 2:
#        guess = opponent_history[-2]
#
#    return guess

Q = {}

def player(prev_opponent_play, opponent_history=[]):
    global Q
    opponent_history.append(prev_opponent_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = "S"
    if len(opponent_history)>4:
      last_four = "".join(opponent_history[-4:])
      if last_four in Q.keys():
        Q[last_four] += 1 
      else:
        Q[last_four] = 1

      last_three = "".join(opponent_history[-3:])
      possible =[last_three+"R", last_three+"P", last_three+"S"]

      for p in possible:
        if not p in Q.keys():
          Q[p] = 0
        
      predict=max(possible, key=lambda key:Q[key])

      guess = ideal_response[predict[-1:]]
  
    return guess
