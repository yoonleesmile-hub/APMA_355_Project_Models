import numpy as np
import matplotlib.pyplot as plt

# Use the equilibrium location from YOUR graph
T_cold = -60  # approximate from your plotted intersection

fig, ax = plt.subplots(figsize=(10, 2.5))
ax.axhline(0, color="black", linewidth=1.2)

# Match domain of your graph
x_min = -100
x_max = 100

arrow_positions = np.linspace(x_min, x_max, 35)

# Arrows must point TOWARD the stable equilibrium
for xi in arrow_positions:
    if xi < T_cold:
        dx = 3      # move right toward T_cold
    else:
        dx = -3     # move left toward T_cold

    ax.arrow(
        xi, 0, dx, 0,
        head_width=0.05,
        head_length=2,
        fc="black",
        ec="black",
        length_includes_head=True
    )

# Plot equilibrium at EXACT x-position from graph
ax.plot(T_cold, 0, "o", color="blue", markersize=10)

# Label (slightly above, centered)
ax.text(T_cold, 0.32, r"$T_{\mathrm{cold}}$ stable", ha="center", fontsize=10)

# Formatting
ax.set_xlim(x_min, x_max)
ax.set_ylim(-0.5, 0.7)
ax.set_yticks([])

# ✅ Explicit meaning of x-axis
ax.set_xlabel(r"Global average temperature $T$ [$^\circ$C]")

ax.set_title("Phase Line Diagram: Snowball-State Regime")

plt.show()