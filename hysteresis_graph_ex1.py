import numpy as np
import matplotlib.pyplot as plt

# 1. Constants (Matching your derived model)
A_derived = 202.0
B_derived = 2.15
T_mid = 265
width = 10

# Values calculated from dQ/dT = 0
Q_high, T_freeze = 486.2, 251.0  # Glaciation Point
Q_low, T_melt = 316.9, 276.5    # Deglaciation Point

# 2. Define the Functions
def albedo(T):
    return 0.5 - 0.2 * np.tanh((T - T_mid) / width)

def Q_eq(T):
    return (A_derived + B_derived * T) / (1 - albedo(T))

# 3. Data Generation (Creating the curve)
T_full = np.linspace(230, 310, 2000)
Q_full = Q_eq(T_full)

# Plotting setup
plt.figure(figsize=(10, 7), facecolor='white')
ax = plt.gca()

# 4. Create the "Hysteresis Window" (Shaded Area)
# Define the indices for the unstable branch between the critical points
unstable_idx = (T_full >= T_freeze) & (T_full <= T_melt)

# Fill the loop area to mimic the "magnetic" image style
plt.fill_betweenx(T_full[unstable_idx], Q_full[unstable_idx], Q_high, color='yellow', alpha=0.3, label='Hysteresis Loop')

# 5. Plot the Equilibrium States (The "S-Curve")
# We use a gradient effect on the stable branches to show strength
plt.plot(Q_full[T_full > T_melt], T_full[T_full > T_melt], color='#2ecc71', linewidth=4, label='Warm State') # Green
plt.plot(Q_full[T_full < T_freeze], T_full[T_full < T_freeze], color='#3498db', linewidth=4, label='Snowball State') # Blue
plt.plot(Q_full[unstable_idx], T_full[unstable_idx], color='black', linestyle='--', linewidth=2, alpha=0.3, label='Unstable Branch')

# 6. Plot the Intersection Points (Red Dots where dQ/dT = 0)
plt.scatter([Q_high, Q_low], [T_freeze, T_melt], color='red', s=120, zorder=5)

# 7. ADD THE ARROWS SHOWING THE 'JUMPS'
arrow_style = dict(arrowstyle='simple,head_width=10,head_length=10', facecolor='black', edgecolor='black', lw=1.5)

# Glaciation jump at Q=486 (Warm -> Snowball)
plt.annotate('', xy=(Q_high, 230), xytext=(Q_high, T_freeze - 5), arrowprops=arrow_style)
plt.text(Q_high + 5, T_freeze - 15, 'Glaciation!\nJump Down', color='red', weight='bold')

# Deglaciation jump at Q=317 (Snowball -> Warm)
plt.annotate('', xy=(Q_low, 310), xytext=(Q_low, T_melt + 5), arrowprops=arrow_style)
plt.text(Q_low - 70, T_melt + 15, 'Deglaciation!\nJump Up', color='blue', weight='bold')

# Labels for key thresholds
plt.axvline(Q_low, color='black', linestyle=':', alpha=0.3)
plt.axvline(Q_high, color='black', linestyle=':', alpha=0.3)
plt.text(Q_low - 5, 235, f'{Q_low:.0f} W/m²', color='gray', rotation=90, ha='right')
plt.text(Q_high - 5, 235, f'{Q_high:.0f} W/m²', color='gray', rotation=90, ha='right')

# Formatting
plt.title('Climate Hysteresis Showcase', fontsize=16, weight='bold')
plt.xlabel('Solar Forcing $Q$ ($W/m^2$)', fontsize=13)
plt.ylabel('Surface Temperature $T$ (Kelvin)', fontsize=13)
plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(loc='lower right', frameon=True, framealpha=0.9)

plt.savefig('climate_hysteresis_best.png', dpi=300, bbox_inches='tight')
print("Graph saved as 'climate_hysteresis_best.png'")
plt.show()