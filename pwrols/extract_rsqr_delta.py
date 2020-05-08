import pandas as pd
import statsmodels.api as sm

def extract_r_delta(df, dv, t, iv = None):
    """Returns delta of r-squared with and without treatment variable.
  
    This function performs 2 OLS regressions, with and without the treatment
    variable, in order to infer the change in r-squared as a function of treatment.
  
    Parameters: 
    df (Pandas dataframe): Pandas dataframe containing the model data
    dv (string): Dependent/response variable 
    t (string): Column of dataframe denoting assignment of the treatment
    iv (list): List of independent variables  
  
    Returns: 
    float: estimated r-squared     
    """

    Y = df[dv]
    
    if iv is not None:
        iv.append(t)
        X1 = df[iv]
    else:
        X1 = df[t]
    X1 = sm.add_constant(X1)
    X2 = X1['const']
    
    model1 = sm.OLS(Y.astype(float), X1.astype(float)).fit()
    model2 = sm.OLS(Y.astype(float), X2.astype(float)).fit()
    
    return max(model1.rsquared, 0) - max(model2.rsquared, 0) 
