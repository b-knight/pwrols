import numpy as np
from statistics import mean 

def derive_candidate_mdes(dv, rel_mde, rel_mde_lb, rel_mde_ub, steps=11):
    
    """Returns a list of candidate absolute MDE and relative MDE tuples.
  
    This function takes a list of values of the dependent variable, the target
    change in the dependent variable, an upper and lower bound for the MDE space
    to be explored, and the number of candidate MDEs the ultimate power curve will 
    consist of. 
  
    Parameters: 
    dv (list): A list of values of the dependent variable drawn from an empirical sample
    rel_mde (float): The initial desired relative MDE to ground the power analysis on
    rel_mde_lb (float): The lower bound of the power analysis curve
    rel_mde_ub (float): The upper bound of the power analysis curve
    steps (int): The total number of candidate MDE values to be estimated
  
    Returns: 
    list of tuples: Required sample size given the specified power and significance level
    """    
    
    if steps % 2 == 0:
        print("The specified number of candidate MDEs must be odd. Please enter an odd integer.")
        return None
    
    lower_half = list(np.linspace(rel_mde_lb, 
                                  rel_mde, 
                                  math.floor(steps/2)+1))[0:math.floor(steps/2)]
    
    upper_half = list(np.linspace(rel_mde, rel_mde_ub, math.floor(steps/2)+1))

    rel_mdes = []
    for i in (lower_half + upper_half):
        rel_mdes.append(round(i, 5))   
        
    dv_mean = mean(dv) 
    
    abs_mdes = []
    for j in rel_mdes:
        abs_mdes.append(dv_mean*j)    
    
    return list(zip(rel_mdes, abs_mdes))
