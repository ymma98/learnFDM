import numpy as np

def swave1d(x1d, t1d, c):
    """
    wave eqn 1d solver
    :param x1d: (np.1darray) mesh points in x dir
    :param t1d: (np.1darray) time points in time domain 
    :param c: (float) c in wave eqn
    """
    dx = x1d[1] - x1d[0]
    Nx = dx.shape[0] - 1
    dt = t1d[1] - t1d[0]
    Nt = dt.shape[0] - 1
    C = c*dt/dx
    C2 = C**2
    
    for i in range(0, Nx+1):
        
    
    