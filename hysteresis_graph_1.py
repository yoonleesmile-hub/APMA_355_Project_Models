import numpy as np
import matplotlib.pyplot as plt

# 1. Constants from your image
A_tilde = -367.58
B = 2.09
T_mid = 265
width = 10

# 2. Define functions
def albedo(T):
    return 0.5 - 0.2 * np.tanh((T - T_mid) / width)

def albedo_prime(T):
    # Derivative: -0.2 * (1/10) * sech^2((T-265)/10)
    return -0.2 * (1/width) * (1 / np.cosh((T - T_mid) / width)**2)

def dQ_dT(T):
    u = A_tilde + B * T
    v = 1 - albedo(T)
    u_prime = B
    v_prime = -albedo_prime(T)
    return (u_prime * v - u * v_prime) / (v**2)

# 3. Generate data
T_range = np.linspace(240, 290, 2000)
dq_vals = dQ_dT(T_range)

# 4. Find the intersection points (roots) where the curve crosses y=0
# We look for where the sign flips from positive to negative (or vice versa)
idx = np.where(np.diff(np.sign(dq_vals)))[0]
root_temps = T_range[idx]
root_values = dq_vals[idx]

# 5. Plotting
plt.figure(figsize=(10, 6))

# Plot the main curve and the zero line
plt.plot(T_range, dq_vals, label=r'$\frac{dQ}{dT}$', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='-', linewidth=1.5)

# PLOT THE INTERSECTIONS IN RED
plt.plot(root_temps, root_values, 'ro', markersize=10, label='Critical Points ($dQ/dT=0$)')

# Annotate the red dots with their T values
for T_val in root_temps:
    plt.annotate(f'{T_val:.2f} K', (T_val, 0), xytext=(-15, 15), 
                 textcoords='offset points', color='red', fontweight='bold')

plt.title(r'Finding Critical Thresholds where $\frac{dQ}{dT} = 0$', fontsize=14)
plt.xlabel('Temperature $T$ (K)', fontsize=12)
plt.ylabel(r'Derivative $\frac{dQ}{dT}$', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# 6. SAVE AND SHOW
plt.savefig('dq_dt_intersections.png', dpi=300)
print(f"Graph saved! Intersections found at: {root_temps}")
plt.show()