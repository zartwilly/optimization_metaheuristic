#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:02:54 2024

@author: willy

Genetic Algorithm for combinatorial Quadratic Assignement Problem
"""
import numpy as np
import pandas as pd


###############################################################################
# 
#                   Constances : start
#
###############################################################################
P_C = 1             # Probability of Crossover
P_M = 0.3           # Probability of Mutation
K = 3               # Tournament Selection
POPULATION = 100    # Population per generation
GENERATION = 30     # Number of Generation
###############################################################################
# 
#                   Constances : ennd
#
###############################################################################

###############################################################################
# 
#                   Variables : start
#
###############################################################################
Dist = pd.DataFrame([[0,1,2,3,1,2,3,4],
                     [1,0,1,2,2,1,2,3],
                     [2,1,0,1,3,2,1,2],
                     [3,2,1,0,4,3,2,1],
                     [1,2,3,4,0,1,2,3],
                     [2,1,2,3,1,0,1,2],
                     [3,2,1,2,2,1,0,1],
                     [4,3,2,1,3,2,1,0]], 
                    columns=["A","B","C","D","E","F","G","H"], 
                    index=["A","B","C","D","E","F","G","H"])
Flow = pd.DataFrame([[0,5,2,4,1,0,0,6],
                     [5,0,3,0,2,2,2,0],
                     [2,3,0,0,0,0,0,5],
                     [4,0,0,0,5,2,2,10],
                     [1,2,0,5,0,10,0,0],
                     [0,2,0,2,10,0,5,1],
                     [0,2,0,2,0,5,0,10],
                     [6,0,5,10,0,1,10,0]], 
                    columns=["A","B","C","D","E","F","G","H"], 
                    index=["A","B","C","D","E","F","G","H"])
###############################################################################
# 
#                   variables : ennd
#
###############################################################################



###############################################################################
# 
#                   fitness value : start
#
###############################################################################
chromosone = ["D","A","C","B","G","E","F","H"]
def fitness_value(chromosone):
    """
    compute the cost of the initial solution called chromosome

    Parameters
    ----------
    chromosone : list
        DESCRIPTION.
            list of departments
    Returns
    -------
    None.

    """
    re_dist_df = Dist.reindex(columns=chromosone, index=chromosone)
    re_flow_df = Flow.reindex(columns=chromosone, index=chromosone)
    cost_chromo = sum(sum(np.array(re_dist_df) * np.array(re_flow_df)))
    return cost_chromo
    
###############################################################################
# 
#                   fitness value : end
#
###############################################################################
if __name__ == "__main__":
    pass
