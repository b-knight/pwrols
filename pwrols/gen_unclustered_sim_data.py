import numpy as np
import pandas as pd

def gen_unclustered_sim_data(df, dv, mde_abs = None, mde_rel = None, dichotomous = False, frac = 0.5):
    """Returns a dataframe with a specified change in mean.
  
    This function takes a dataframe and a relative or absolute change
    in the dependent variable, and returns a dataframe with double the
    amount of rows - half of which have a mean value of the dependent 
    variable corresponding with the specified change. In addition,
    a new boolean corresponding to the treatment is appended. 
  
    Parameters: 
    df (Pandas dataframe): Pandas dataframe containing the model data
    dv (string): Dependent/response variable 
    mde_abs (float): Absolute change in the dependent variable
    mde_rel (float): Relative change in the dependent variable
    dichotomous (boolean): Boolean value equals 'True' if the dependent variable is dichotomous
    frac (float): Proportion of the simulated data to be returned 
  
    Returns: 
    Pandas dataframe: A new dataframe containing the simulated data. 
    """

    if mde_abs is None and mde_rel is None:
        print("Either an absolute ('mde_abs') or relative ('mde_rel') change in" +
              " the dependent variable must be specified.")
        return None        
    
    if mde_abs is not None and mde_rel is not None:
        print("Only absolute ('mde_abs') OR relative ('mde_rel') change in" +
              " the dependent variable may be specified. Please supply only one argument.")
        return None            
    
    dvmean   = df[dv].mean()
    dflength = len(df)
    if dichotomous is False:  
        print("The continuous dependent variable '{}' has a ".format(dv) +
              "mean of {} over {:,} observations.".format(dvmean, dflength))
    else:
        print("The dichotomous dependent variable '{}' has a ".format(dv) +
              "proportion of {} over {:,} observations.".format(dvmean, dflength))
        
    new_df = df.copy()
    
    if (mde_abs is not None) & (dichotomous is False):
        new_df[dv] = new_df[dv] + mde_abs
        print("The new value of the continuous dependent variable is {}.".format(new_df[dv].mean()))
        
    elif (mde_rel is not None) & (dichotomous is False):
        new_df[dv] = new_df[dv]*(1+mde_rel)
        print("The new value of the continuous dependent variable is {}.".format(new_df[dv].mean()))
        
    elif (mde_abs is not None) & (dichotomous is True):    
        new_prop = dvmean + mde_abs
        print("The new value of the dichotomous dependent variable is {}.".format(new_prop))   
        new_df['rand'] = np.random.uniform(low = 0.0, high = 1.0, size=len(new_df))
        new_df[dv] = np.where(new_df['rand'] <= new_prop, 1, 0)
        new_df.index = np.arange(len(new_df))
        del new_df['rand']
        
    elif (mde_rel is not None) & (dichotomous is True):    
        new_prop = dvmean*(1 + mde_rel)
        print("The new value of the dichotomous dependent variable is {}.".format(new_prop))   
        new_df['rand'] = np.random.uniform(low = 0.0, high = 1.0, size=len(new_df))
        new_df[dv] = np.where(new_df['rand'] <= new_prop, 1, 0)  
        new_df.index = np.arange(len(new_df))
        del new_df['rand']
        
    new_df['Treated'] = 1
    df['Treated'] = 0
    final_data = pd.concat([df, new_df], ignore_index = True, sort = False)
    return final_data.sample(frac = frac)
