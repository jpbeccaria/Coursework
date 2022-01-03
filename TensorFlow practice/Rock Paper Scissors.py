# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:41:00 2022

@author: Juan
"""

# Selected strategy goes foward into abbey strategy, which is aparently the better
# defeat the other ones.


def player(prev_play, opponent_history=[], combinations= {}):
  opponent_history.append(prev_play)
  
  n = 3 # n value can be changed for a longer history evaluation

  guess = "R" #defalt value

  if len(opponent_history)>n:    
    last_n = "".join(opponent_history[-n:])

# if the last combination does not exist, it is created, if it does, +1 occurency

    if "".join(opponent_history[-(n+1):]) in combinations.keys():
      combinations["".join(opponent_history[-(n+1):])]+=1
    else:
      combinations["".join(opponent_history[-(n+1):])]=1

     # stablish posible future plays 

    potential_plays = [last_n + "R", last_n + "P", last_n + "S"]

    for i in potential_plays:
      if not i in combinations.keys():
       combinations[i] = 0

    prediction = max(potential_plays, key=lambda key: combinations[key])

    if prediction[-1] == "P":
      guess = "S"
    if prediction[-1] == "R":
      guess = "P"
    if prediction[-1] == "S":
      guess = "R"


  return guess