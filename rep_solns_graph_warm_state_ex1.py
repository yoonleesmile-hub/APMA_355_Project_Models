import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Model parameters
# -----------------------------

A = 203.3
B = 2.09
Q = 540   # warm-only regime
C = 80

# -----------------------------
# Smooth albedo
# -----------------------------

def alpha(T):
    T_K = T + 273.15
    return 0.5 - 0.2 * np.tanh((T_K - 265) / 10)

def dTdt(T):
    return (Q * (1 - alpha(T)) - (A + B*T)) / C

# -----------------------------
# Find warm equilibrium
# -----------------------------

def find_equilibrium():
    T_vals = np.linspace(-50, 150, 5000)
    f_vals = dTdt(T_vals)

    for i in range(len(T_vals)-1):
        if f_vals[i] * f_vals[i+1] < 0:
            a, b = T_vals[i], T_vals[i+1]
            for _ in range(50):
                m = (a + b) / 2
                if dTdt(a) * dTdt(m) <= 0:
                    b = m
                else:
                    a = m
            return (a + b)/2

T_warm = find_equilibrium()
print("T_warm =", T_warm)

# -----------------------------
# Solve ODE
# -----------------------------

def solve(T0, t):
    T = np.zeros_like(t)
    T[0] = T0
    dt = t[1] - t[0]

    for i in range(len(t)-1):
        T[i+1] = T[i] + dt * dTdt(T[i])

    return T

# -----------------------------
# Time grid
# -----------------------------

t = np.linspace(0, 350, 1000)

# Start NEAR equilibrium (fixes weird S-shape)
T_above = solve(T_warm + 15, t)
T_below = solve(T_warm - 40, t)

# -----------------------------
# Plot
# -----------------------------

fig, ax = plt.subplots(figsize=(8,5))

# Equilibrium line
ax.axhline(T_warm, color="red", linewidth=1.5)

# Trajectories (clean convergence)
ax.plot(t, T_above, color="purple", linewidth=2)
ax.plot(t, T_below, color="green", linewidth=2)

# Arrows
def add_arrows(T):
    for i in range(150, 800, 200):
        ax.annotate(
            "",
            xy=(t[i+5], T[i+5]),
            xytext=(t[i], T[i]),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.2)
        )

add_arrows(T_above)
add_arrows(T_below)

# Labels
ax.text(240, T_warm + 3, r"$T_{\mathrm{warm}}$ stable", color="red", fontsize=11)

# -----------------------------
# Formatting (KEY FIX)
# -----------------------------

ax.set_xlim(0, 350)
ax.set_ylim(0, 200)   # ← your requested interval

ax.set_xlabel("Time [years]")
ax.set_ylabel("Temperature T [°C]")
ax.set_title("Representative Solutions in the Warm-State Regime")

ax.grid(True)

plt.show()