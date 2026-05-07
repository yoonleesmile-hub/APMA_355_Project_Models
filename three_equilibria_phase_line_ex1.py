import numpy as np
import matplotlib.pyplot as plt

T_cold = -45
T_medium = -5
T_warm = 16

fig, ax = plt.subplots(figsize=(10, 2.5))
ax.axhline(0, color='black')

# Uniform arrow spacing
arrow_positions = np.linspace(-70, 40, 25)

for xi in arrow_positions:
    if xi < T_cold:
        direction = 1
    elif T_cold < xi < T_medium:
        direction = -1
    elif T_medium < xi < T_warm:
        direction = 1
    else:
        direction = -1

    dx = 2 * direction

    ax.arrow(
        xi, 0, dx, 0,
        head_width=0.05,
        head_length=1.5,
        fc='black',
        ec='black',
        length_includes_head=True
    )

# Equilibria points
ax.plot(T_cold, 0, 'o', color='blue', markersize=10)
ax.plot(T_medium, 0, 'o', markerfacecolor='white',
        markeredgecolor='orange', markersize=10, markeredgewidth=2)
ax.plot(T_warm, 0, 'o', color='green', markersize=10)

# Labels
ax.text(T_cold - 2, 0.3, r"$T_{\mathrm{cold}}$ (stable)", ha='right')
ax.text(T_medium, 0.3, r"$T_{\mathrm{medium}}$ (unstable)", ha='center')
ax.text(T_warm + 2, 0.3, r"$T_{\mathrm{warm}}$ (stable)", ha='left')

# Formatting
ax.set_xlim(-70, 40)
ax.set_ylim(-0.5, 0.7)
ax.set_yticks([])

# ✅ X-axis label added here
ax.set_xlabel(r"Temperature $T$ [$^\circ$C]")

ax.set_title("Phase Line Diagram: Three-Equilibria Regime")

ax.set_xlabel(r"Temperature $T$ [$^\circ$C]")

plt.show()