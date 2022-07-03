import numpy as np

def solver_wave1d(func_i, func_v, func_f,  \
                  c, L, dt, C, T, \
                  user_action=None):
    """
    wave eqn 1d solver
    u_tt = c^2 u_xx + f on (0,L]x(0,T]
    :param func_i: (function) func_i(x)=u(x,t=0), i.e. 
                   initial value function 
    :param func_v: (function) func_v(x) = du(x,t=0)/dt
    :param func_f: (function) func_f(x,t) on the r.h.s. of eqn
    :param c: (float) constant on the r.h.s. of eqn
    :param L: (float) solver range: (0,L]
    :param dt: (float) time step
    :param C: (float) Courant number
    :param T: (float) end time, t\in (0,T]
    :param uer_action: (bool)
    """
    
    