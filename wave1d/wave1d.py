import numpy as np
from sympy import jacobi

def my_user_action_func(u, x, t, n):
    return (np.abs(u).max() > 10)

def solver_wave1d(func_i, func_v, func_f,  \
                  c, L, dt, C, T, \
                  user_action=None):
    """
    wave eqn 1d solver
    u_tt = c^2 u_xx + f on (0,L]x(0,T]
    warning: this is not a general function for wave1d
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
    Nt = int(round(T/dt))  # time space number
    t = np.linspace(0, T, Nt+1)  # Nt+1: time node number
    dx = c*dt/C
    Nx = int(round(L/dx))  # domain space number
    x = np.linspace(0, L, Nx)
    C2 = C**2
    # make sure dx and dt are compatible with x and t
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    if func_f is None or func_f == 0:
        func_f = lambda x, t: 0
    if func_v is None or func_v == 0:
        func_v = lambda x: 0
    
    u = np.zeros(Nx+1)  # solution array at new time level
    u_n = np.zeros(Nx+1) # 1 time level back
    u_nm1 = np.zeros(Nx+1) # 2 time level back

    import time;  t0 = time.clock()

    # Load initial condition to u_n
    for i in range(0, Nx+1):
        u_n[i] = func_i(x[i])
    
    if user_action is not None:
        user_action(u_n, x, t, 0)
    
    # special formula for the 1st step
    n = 0
    for i in range(1, Nx):
        u[i] = u_n[i] + dt*func_v(x[i]) + \
            0.5*C2*(u_n[i+1] -2*u_n[i]+u_n[i-1]) + \
            0.5*dt**2*func_f(x[i], t[n])
    u[0] = 0; u[Nx] = 0
    
    if user_action is not None:
        user_action(u, x, t, 1)

    # switch vars before next step
    u_nm1 = u_n;  u_n = u

    for n in range(1, Nt):
        # update all inner points at time t[n+1]
        for i in range(1, Nx):
            u[i] = -u_nm1[i] + 2*u_n[i] + \
                C2*(u_n[i+1] -2*u_n[i] + u_n[i-1]) + \
                    dt**2 * func_f(x[i], t[n])
    
        # insert boundary conditions
        u[0] = 0;  u[Nx] = 0
        if user_action is not None:
            if user_action(u, x, t, n+1):
                break

        # switch var before next step
        u_nm1 = u_n;    u_n = u
    
    cpu_time = time.clock() - t0
    return u, x, t, cpu_time
    
    
    
    
    

    