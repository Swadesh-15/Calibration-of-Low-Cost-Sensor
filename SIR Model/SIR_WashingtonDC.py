import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population =N
N = 706000
# Initial number of infected individuals =I0 
I0 = 7
# Initial number of recovered individuals =R0
R0 = 0
# Individuals susceptible to infection initially =S0, everyone left after the initial condition
S0 = N - I0 - R0
# Transmiability rate constant =r
r = 0.3
# Recovery rate constant =a
a = 0.2
# Plot for the time axis(in days), till now
t = np.linspace(0, 150, 150)

# Differential equations for the SIR model
def eqn(y, t, N, r, a):
    S, I, R = y
    dSdt = -r * S * I / N
    dIdt = r * S * I / N - a * I
    dRdt = a * I
    return dSdt, dIdt, dRdt

# Initial condition vectors
y0 = S0, I0, R0
ret = odeint(eqn, y0, t, args=(N, r, a))
S, I, R = ret.T

# Plots for the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/100000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/100000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/100000, 'g', alpha=0.5, lw=2, label='Recovered')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (100000s)')
ax.set_ylim(0,8)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
