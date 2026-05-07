import numpy as np
import matplotlib.pyplot as plt

A = 203.3
B = 2.09
Q = 250  # low Q chosen to show snowball-only regime

T = np.linspace(-100, 100, 20000)

def alpha(T_celsius):
    T_kelvin = T_celsius + 273.15
    return 0.5 - 0.2 * np.tanh((T_kelvin - 265) / 10)

incoming = Q * (1 - alpha(T))
outgoing = A + B * T
f = incoming - outgoing

# Find intersections
equilibria = []
for i in range(len(T) - 1):
    if f[i] * f[i + 1] < 0:
        T_eq = (T[i] + T[i + 1]) / 2
        equilibria.append(T_eq)

if len(equilibria) == 0:
    raise ValueError("No equilibrium found. Increase T range or adjust Q.")

T_eq = equilibria[0]
y_eq = A + B * T_eq

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(T, incoming, label=r"$Q(1-\alpha(T))$", linewidth=2)
ax.plot(T, outgoing, label=r"$A+BT$", linewidth=2)

# Mark intersection
ax.plot(T_eq, y_eq, "ko", markersize=8)

ax.annotate(
    rf"$T_{{\mathrm{{cold}}}}$",
    xy=(T_eq, y_eq),
    xytext=(T_eq + 15, y_eq + 45),
    arrowprops=dict(arrowstyle="->"),
    fontsize=11,
    bbox=dict(facecolor="white", alpha=0.85, edgecolor="none")
)

# Same style/range as warm-state graph
ax.set_xlim(-100, 100)
ax.set_ylim(0, 450)

ax.set_xlabel(r"Temperature $T$ [$^\circ$C]")
ax.set_ylabel(r"Energy flux [W/m$^2$]")
ax.set_title("Snowball State Equilibrium with S-Shaped Incoming Radiation Curve")
ax.grid(True)
ax.legend()

plt.show()

print("Equilibrium:", T_eq)