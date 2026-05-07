import numpy as np
import matplotlib.pyplot as plt

# Parameter (adjust to show 1 or 3 equilibria)
Q = 340
A = 203.3
B = 2.09

# Temperature range (Celsius)
T = np.linspace(-70, 40, 2000)

# Smooth albedo function
def alpha(T_celsius):
    T_kelvin = T_celsius + 273.15
    return 0.5 - 0.2 * np.tanh((T_kelvin - 265) / 10)

# Curves
incoming = Q * (1 - alpha(T))
outgoing = A + B * T
f = incoming - outgoing

# Find equilibria (sign changes)
equilibria = []
for i in range(len(T) - 1):
    if f[i] * f[i + 1] < 0:
        T_eq = (T[i] + T[i + 1]) / 2
        equilibria.append(T_eq)

# Sort equilibria (important!)
equilibria = sorted(equilibria)

# Assign names based on number of equilibria
labels = []
if len(equilibria) == 3:
    labels = [r"$T_{\mathrm{cold}}$", r"$T_{\mathrm{medium}}$", r"$T_{\mathrm{warm}}$"]
elif len(equilibria) == 1:
    # Determine if warm or cold
    if equilibria[0] > 0:
        labels = [r"$T_{\mathrm{warm}}$"]
    else:
        labels = [r"$T_{\mathrm{cold}}$"]

# Plot
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(T, incoming, label=r"$Q(1-\alpha(T))$", linewidth=2)
ax.plot(T, outgoing, label=r"$A+BT$", linewidth=2)

# Label equilibria carefully
for i, T_eq in enumerate(equilibria):
    y_eq = A + B * T_eq
    ax.plot(T_eq, y_eq, "ko", markersize=6)

    # Smart offsets to avoid overlap
    if i == 0:  # cold
        dx, dy = -8, -15
    elif i == 1 and len(equilibria) == 3:  # middle
        dx, dy = 5, 10
    else:  # warm
        dx, dy = 5, -10

    ax.text(T_eq + dx, y_eq + dy,
            f"{labels[i]}\n({T_eq:.1f}°C)",
            fontsize=10,
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

ax.set_xlabel(r"Temperature $T$ [$^\circ$C]")
ax.set_ylabel(r"Energy flux [W/m$^2$]")
ax.set_title("Equilibria as Intersections of Incoming and Outgoing Radiation (3 Equilibria)")
ax.grid(True)
ax.legend()

plt.show()