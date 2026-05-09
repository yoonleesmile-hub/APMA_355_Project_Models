import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Model parameters
# -----------------------------

A = 203.3
B = 2.09

# Temperature range
T = np.linspace(-100, 100, 10000)

# -----------------------------
# Smooth albedo function
# -----------------------------

def alpha(T_celsius):
    T_kelvin = T_celsius + 273.15
    return 0.5 - 0.2 * np.tanh((T_kelvin - 265) / 10)

# Equilibrium condition:
# Q(1 - alpha(T)) = A + BT
# Solve for Q as a function of T

Q_of_T = (A + B * T) / (1 - alpha(T))

# -----------------------------
# Find turning points
# -----------------------------

dQdT = np.gradient(Q_of_T, T)

turning_points = []

for i in range(len(T) - 1):
    if dQdT[i] * dQdT[i + 1] < 0:
        T_turn = (T[i] + T[i + 1]) / 2
        Q_turn = (A + B * T_turn) / (1 - alpha(T_turn))
        turning_points.append((T_turn, Q_turn))

# Sort by Q value
turning_points = sorted(turning_points, key=lambda x: x[1])

(T_low, Q_low), (T_high, Q_high) = turning_points

print(f"Lower critical point: Q = {Q_low:.2f}, T = {T_low:.2f} °C")
print(f"Upper critical point: Q = {Q_high:.2f}, T = {T_high:.2f} °C")

# -----------------------------
# Stability classification
# -----------------------------
# Stable branches: lower cold branch and upper warm branch
# Unstable branch: middle branch between turning points

stable_cold = T < T_low
unstable_middle = (T >= T_low) & (T <= T_high)
stable_warm = T > T_high

# -----------------------------
# Plot bifurcation diagram
# -----------------------------

fig, ax = plt.subplots(figsize=(8, 5))

# Plot Q on x-axis and equilibrium temperature on y-axis
ax.plot(Q_of_T[stable_cold], T[stable_cold],
        color="blue", linewidth=2, label="Stable cold branch")

ax.plot(Q_of_T[unstable_middle], T[unstable_middle],
        color="green", linestyle="--", linewidth=2, label="Unstable middle branch")

ax.plot(Q_of_T[stable_warm], T[stable_warm],
        color="orange", linewidth=2, label="Stable warm branch")

# Critical Q values
ax.axvline(Q_low, color="black", linestyle=":", linewidth=1.5)
ax.axvline(Q_high, color="black", linestyle=":", linewidth=1.5)

ax.text(Q_low, 90, r"$\min_T Q(T)$", ha="center", fontsize=10)
ax.text(Q_high, 90, r"$\max_T Q(T)$", ha="center", fontsize=10)

# Shaded three-equilibria region
ax.fill_betweenx(
    [-100, 100],
    Q_low,
    Q_high,
    color="lightblue",
    alpha=0.20
)

ax.text(
    (Q_low + Q_high) / 2,
    -30,
    "three-equilibria\nregime",
    ha="center",
    fontsize=10
)

# Labels for one-equilibrium regimes
ax.text(Q_low - 65, -85, "Snowball-only\nregime", ha="center", fontsize=10)
ax.text(Q_high + 65, 70, "Warm-only\nregime", ha="center", fontsize=10)

# Formatting
ax.set_xlabel(r"Solar forcing parameter $Q$")
ax.set_ylabel(r"Equilibrium temperature $T^*$ [$^\circ$C]")
ax.set_title("Bifurcation Diagram for the Budyko--Sellers Energy Balance Model")
ax.set_ylim(-100, 100)
ax.grid(True)
ax.legend(loc="lower right")

plt.show()