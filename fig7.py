import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# -----------------------------
# Model parameters
# -----------------------------

A = 203.3
B = 2.09
Q = 340
C = 80

# -----------------------------
# Smooth albedo function
# -----------------------------

def alpha(T_celsius):
    T_kelvin = T_celsius + 273.15
    return 0.5 - 0.2 * np.tanh((T_kelvin - 265) / 10)

def net_energy(T):
    return Q * (1 - alpha(T)) - (A + B * T)

def dTdt(T):
    return net_energy(T) / C

# -----------------------------
# Find equilibria numerically
# -----------------------------

def find_equilibria(Tmin=-70, Tmax=40, N=5000):
    Ts = np.linspace(Tmin, Tmax, N)
    Fs = np.array([net_energy(T) for T in Ts])

    roots = []

    for i in range(len(Ts) - 1):
        if Fs[i] * Fs[i + 1] < 0:
            a, b = Ts[i], Ts[i + 1]

            for _ in range(60):
                m = (a + b) / 2
                if net_energy(a) * net_energy(m) <= 0:
                    b = m
                else:
                    a = m

            roots.append((a + b) / 2)

    return roots

equilibria = find_equilibria()

if len(equilibria) != 3:
    raise ValueError(f"Expected 3 equilibria, but found {len(equilibria)}: {equilibria}")

T_cold, T_medium, T_warm = equilibria

print("Computed equilibria:")
print(f"T_cold   = {T_cold:.3f} °C")
print(f"T_medium = {T_medium:.3f} °C")
print(f"T_warm   = {T_warm:.3f} °C")

# -----------------------------
# RK4 solver
# -----------------------------

def solve_ode(T0, t):
    T = np.zeros_like(t)
    T[0] = T0
    dt = t[1] - t[0]

    for i in range(len(t) - 1):
        k1 = dTdt(T[i])
        k2 = dTdt(T[i] + 0.5 * dt * k1)
        k3 = dTdt(T[i] + 0.5 * dt * k2)
        k4 = dTdt(T[i] + dt * k3)

        T[i + 1] = T[i] + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

    return T

# -----------------------------
# Representative solutions
# -----------------------------

t = np.linspace(0, 350, 1200)

T_above_warm = solve_ode(T_warm + 12, t)
T_between_medium_warm = solve_ode(T_medium + 0.1, t)
T_between_cold_medium = solve_ode(T_medium - 0.1, t)
T_below_cold = solve_ode(T_cold - 15, t)

# -----------------------------
# Add arrows
# -----------------------------

def add_arrows(ax, t, T, spacing=60):
    arrow_times = np.arange(spacing, t[-1] - spacing, spacing)

    for at in arrow_times:
        i = np.argmin(np.abs(t - at))
        j = min(i + 8, len(t) - 1)

        ax.annotate(
            "",
            xy=(t[j], T[j]),
            xytext=(t[i], T[i]),
            arrowprops=dict(arrowstyle="->", linewidth=1.3, color="black"),
        )

# -----------------------------
# Plot
# -----------------------------

fig, ax = plt.subplots(figsize=(8, 5))

# Shaded regions
ax.fill_between([0, 350], y1=5, y2=30, color="red", alpha=0.10)
ax.fill_between([0, 350], y1=-60, y2=-15, color="lightblue", alpha=0.20)

ax.text(175, 23, "No ice", color="darkred", fontsize=11)
ax.text(165, -40, "Completely frozen", color="darkblue", fontsize=11)

# Equilibrium lines using computed values from same model as intersection graph
ax.axhline(T_warm, color="red", linewidth=1.4)
ax.axhline(T_medium, color="red", linewidth=1.4)
ax.axhline(T_cold, color="red", linewidth=1.4)

# Representative curves
ax.plot(t, T_above_warm, color="purple", linewidth=2)
ax.plot(t, T_between_medium_warm, color="green", linewidth=2)
ax.plot(t, T_between_cold_medium, color="orange", linewidth=2)
ax.plot(t, T_below_cold, color="deeppink", linewidth=2)

# Arrows
add_arrows(ax, t, T_above_warm)
add_arrows(ax, t, T_between_medium_warm)
add_arrows(ax, t, T_between_cold_medium)
add_arrows(ax, t, T_below_cold)

# Labels
ax.text(255, T_warm + 2.0, r"$T_{\mathrm{warm}}$ stable", color="red", fontsize=10)
ax.text(255, T_medium - 3.2, r"$T_{\mathrm{medium}}$ unstable", color="red", fontsize=10)
ax.text(255, T_cold - 4.0, r"$T_{\mathrm{cold}}$ stable", color="red", fontsize=10)

# Formatting
ax.set_xlim(0, 350)
ax.set_ylim(-60, 30)
ax.set_xlabel("Time [years]")
ax.set_ylabel(r"Temperature $T$ [$^\circ$C]")
ax.set_title("Representative Solutions in the Three-Equilibria Regime")
ax.grid(True)

# color legend

legend_elements = [
    Line2D([0], [0], color="purple",   linewidth=2, label=r"$T_0 > T_{\mathrm{warm}}$: cooling toward warm equilibrium"),
    Line2D([0], [0], color="green",    linewidth=2, label=r"$T_0$ just above $T_{\mathrm{medium}}$: warming toward $T_{\mathrm{warm}}$"),
    Line2D([0], [0], color="orange",   linewidth=2, label=r"$T_0$ just below $T_{\mathrm{medium}}$: cooling toward $T_{\mathrm{cold}}$"),
    Line2D([0], [0], color="deeppink", linewidth=2, label=r"$T_0 < T_{\mathrm{cold}}$: warming toward cold equilibrium"),
]

ax.legend(
    handles=legend_elements,
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    borderaxespad=0,
    fontsize=9,
    framealpha=0.85,
)

plt.tight_layout()
plt.savefig("plot.png", bbox_inches="tight")  # bbox_inches="tight" ensures the legend isn't clipped
plt.show()