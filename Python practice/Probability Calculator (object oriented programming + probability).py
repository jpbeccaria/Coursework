# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:52:10 2022

Instruction cand be found in:
    
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

@author: Juan
"""
import copy 
from collections import Counter
import random

class Hat:

    
    def __init__(self, **kwargs):
        'definition of the content of the had '
        contents = []
        for k, v in kwargs.items():
            for i in range(v):
                contents.append(k)
        self.contents = contents
        
    def draw(self, number_balls):     
        'method to take a sample of the balls in the had'
        if len(self.contents) <= number_balls:
            return self.contents
        else:
            removed_list = random.sample(self.contents, k=number_balls)
            # disagree with the fact that actual removal of balls is required, but it was ask in on of the excersices.
            
            for e in removed_list:
                self.contents.remove(e)
            return removed_list
        
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    'experiment consis of taking a num_balls_draw balls of the had, define certain "configuration" of balls expected and see if it is accomplish'
    
    'probability is calculated gathering num_experiments number of experiments '
    results_list = []
    expected_copy = copy.deepcopy(expected_balls)

    for i in range(num_experiments):
        expected_grater_than_extracted = 0
        hat_copy = copy.deepcopy(hat)
        extracted = hat_copy.draw(num_balls_drawn)
        dict_extracted = Counter(extracted)
        for k , v in expected_copy.items():
            if expected_copy [k] > dict_extracted[k]:
                expected_grater_than_extracted += 1
        if expected_grater_than_extracted > 0:
            results_list.append(0)
        else:
            results_list.append(1)
    result = sum(results_list)/len(results_list)
    return result
            
            
        
# Example        
hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)   

probability = experiment(hat=hat, 
                  expected_balls={"yellow":2,"blue":3,"test":1},
                  num_balls_drawn=5,
                  num_experiments=1000)
