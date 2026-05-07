import numpy as np
import matplotlib.pyplot as plt

# Time domain
t = np.linspace(0, 350, 1200)

# Snowball equilibrium from your graph
T_cold = -62

# Representative solutions
def approach_equilibrium(t, T0, Teq, rate=0.025):
    return Teq + (T0 - Teq) * np.exp(-rate * t)

T_above = approach_equilibrium(t, 20, T_cold, rate=0.025)
T_below = approach_equilibrium(t, -88, T_cold, rate=0.025)

fig, ax = plt.subplots(figsize=(8, 5))

# Equilibrium line
ax.axhline(T_cold, color="red", linewidth=1.5)

# Curves
ax.plot(t, T_above, color="orange", linewidth=2)
ax.plot(t, T_below, color="deeppink", linewidth=2)

# Arrows
def add_arrows(T):
    for i in [150, 350, 600, 850]:
        ax.annotate(
            "",
            xy=(t[i+8], T[i+8]),
            xytext=(t[i], T[i]),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.3)
        )

add_arrows(T_above)
add_arrows(T_below)

# Label
ax.text(240, T_cold + 3, r"$T_{\mathrm{cold}}$ stable", color="red", fontsize=11)

# Formatting
ax.set_xlim(0, 250)
ax.set_ylim(-150, 100)
ax.set_xlabel("Time [years]")
ax.set_ylabel(r"Temperature $T$ [$^\circ$C]")
ax.set_title("Representative Solutions in the Snowball-State Regime")
ax.grid(True)

plt.show()