# 问题: 1D wave equation

$$
\begin{aligned}
\frac{\partial^{2} u}{\partial t^{2}} &=c^{2} \frac{\partial^{2} u}{\partial x^{2}} + f(x,t), & x \in(0, L), & t \in(0, T] \\
u(x, 0) &=I(x), & x & \in[0, L] \\
\frac{\partial}{\partial t} u(x, 0) &= V(x), & x & \in[0, L] \\
u(0, t) &=0, & t & \in(0, T] \\
u(L, t) &=0, & t & \in(0, T]
\end{aligned}
$$


# 离散化

$$
\frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{\Delta t ^2} = c^2 \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{\Delta x^2} + f_i^n
$$

$$
   u_i^{n+1} = c^2 \frac{\Delta t^2}{\Delta x^2} u_{i-1}^n - u_i^{n-1} + (2 - 2c^2 \frac{\Delta t^2}{\Delta x^2}) u_i^n + c^2 \frac{\Delta t^2}{\Delta x^2} u_{i+1}^n + \Delta t^2 f_i^n
$$

即, 
$$
u_{i}^{n+1}=-u_{i}^{n-1}+2 u_{i}^{n}+C^{2}\left(u_{i+1}^{n}-2 u_{i}^{n}+u_{i-1}^{n}\right) + \Delta t^2 f_i^n
$$
其中 $C= c\frac{\Delta t}{\Delta x}$ 是 **Courant number**. 在波动方程中, Courant number 是关键参数, 并且 Courant number 是无量纲的。

当 $n=0$ 时, 我们会遇到 $u_i^{-1}$。求解该项的方法是利用初始条件中的导数项。即,

$$
D_{2t}u_i^n = \frac{u_{i}^{n+1} - u_{i}^{n-1}}{2\Delta t} = V(x_i)
$$
当$n=0$时, 有:
$$
D_{2t}u_i^0 = \frac{u_{i}^{1} - u_{i}^{-1}}{2\Delta t} = V(x_i)
$$
即:
$$
u_i^{-1} = u_i^1 - 2\Delta t V_i
$$
把上式代入离散后的波动方程表达式, 有:
$$
u_{i}^{1}=-u_i^1 + 2\Delta t V_i+2 u_{i}^{0}+C^{2}\left(u_{i+1}^{0}-2 u_{i}^{0}+u_{i-1}^{0}\right) + \Delta t^2 f_i^0 \\
u_{i}^{1}= \Delta t V_i+ u_{i}^{0}+\frac{C^{2}}{2}\left(u_{i+1}^{0}-2 u_{i}^{0}+u_{i-1}^{0}\right) + \frac{1}{2}\Delta t^2 f_i^0 \\
$$


# 构造解析解测试收敛率

我们解析解的约束是: $u(0,t)=u(L,t)=0$, 于是我们选择解析解的形式为:
$$
u_e(x,t)  = x(L-x) \mathrm{sin}t
$$

把 $u_e$ 代入原方程$u_{tt}=c^2 u_{xx}+f$, 得到
$$
f(x,t) = 2c^2 \mathrm{sin} t-(L-x)x\mathrm{sin}t
$$












