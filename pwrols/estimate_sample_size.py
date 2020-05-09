from scipy.stats import f
from scipy import special
from scipy.optimize import fsolve

def estimate_sample_size(u, f2, sig_level = 0.05, power = 0.8):
    """Returns recommended sample size using the f-test.
  
    This function takes the number of parameters estimated, the estimated change in the
    coefficient of determination, and the desired levels of power and statistical significance
    to provide a sample size recommendation.
  
    Parameters: 
    u (int): DF Numerator = (k-1) where k is the number of covariates + 1 for the intercept  
    f2 (float): R2/(1−R2) where R2 is the coefficient of determination
    sig_level (float): Desired statistical significance
    power (float): Desired statistical power
  
    Returns: 
    int: Required sample size given the specified power and significance level
    """
    
    def my_func(v, power):
        return 1-special.ncfdtr(u, v, f2*(u+v+1), f.ppf(1-sig_level, u, v))-power
        
    n = int(fsolve(my_func, 1000, power))
    if n == 1000:
        n = int(fsolve(my_func, 100, power))
    if n == 100:
        n = int(fsolve(my_func, 10, power))
    if n == 10:
        n = int(fsolve(my_func, 1, power))
    if n == 1:
        print("SciPy optimization failed to find a solution.")
        return None
    else:
        return n
