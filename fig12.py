import numpy as np
import matplotlib.pyplot as plt

# Warm equilibrium from your warm-state intersection graph
T_warm = 84.0  # replace with your exact computed T_warm if different

fig, ax = plt.subplots(figsize=(10, 2.5))
ax.axhline(0, color="black", linewidth=1.2)

# Wider domain so the equilibrium appears in the correct x-position
x_min = -100
x_max = 100

arrow_positions = np.linspace(x_min, x_max, 35)

for xi in arrow_positions:
    if xi < T_warm:
        dx = 3      # move right toward warm equilibrium
    else:
        dx = -3     # move left toward warm equilibrium

    ax.arrow(
        xi, 0, dx, 0,
        head_width=0.05,
        head_length=2,
        fc="black",
        ec="black",
        length_includes_head=True
    )

# Equilibrium point
ax.plot(T_warm, 0, "o", color="green", markersize=10)

# Label
ax.text(T_warm, 0.32, r"$T_{\mathrm{warm}}$ stable", ha="center", fontsize=10)

# Formatting
ax.set_xlim(x_min, x_max)
ax.set_ylim(-0.5, 0.7)
ax.set_yticks([])
ax.set_xlabel(r"Temperature $T$ [$^\circ$C]")
ax.set_title("Phase Line Diagram: Warm-State Regime")

plt.show()