def extract_rsqr_delta(df, dv, t, iv = None, cluster_key = None):
    """Returns delta of r-squared with and without treatment variable.
  
    This function 
  
    Parameters: 
    df (Pandas dataframe): Pandas dataframe containing the model data
    dv (string): Dependent/response variable 
    t (string): Column of dataframe denoting assignment of the treatment
    iv (list): List of independent variables 
    cluster_key (string): Column of dataframe data is clustered on if data is clustered    
  
    Returns: 
    float: estimated r-squared     
    """
    
    if iv is not None:
        X = df[t + iv]
    else:
        X = df[t]
    X = sm.add_constant(X)
    Y = df[dv]
    model1 = sm.OLS(Y.astype(float), X.astype(float)).fit()


    if iv is not None:
        X = df[iv]
        X = sm.add_constant(X)
    else:
        X['X'] = 1
        X = X['X']
    model2 = sm.OLS(Y.astype(float), X.astype(float)).fit()

    return max(model1.rsquared, 0) - max(model2.rsquared, 0) 
