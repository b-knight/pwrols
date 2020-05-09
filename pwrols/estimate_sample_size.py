def estimate_sample_size(u, f2, sig_level = 0.05, power = 0.8):
    """Returns recommended sample size using the f-test.

    Keyword arguments:
    u  -- DF Numerator = (k-1) where k is the number of covariates + 1 for the intercept  
    f2 -- R2/(1−R2) where R2 is the coefficient of determination
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
