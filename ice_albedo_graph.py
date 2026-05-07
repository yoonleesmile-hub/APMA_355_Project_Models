import matplotlib.pyplot as plt
import numpy as np

def calc_alpha(T, alpha0, alphai=0.55):
    if T < -15:
        return alphai
    elif -15 <= T < 5:
        return alphai + (alpha0 - alphai) * (T + 15) / 20
    else:  # T >= 5
        return alpha0

calc_alpha_vec = np.vectorize(calc_alpha)

T_example = np.linspace(-25, 27, 500)

plt.plot(T_example, calc_alpha_vec(T_example, 0.28), color="black")

plt.ylim(0.24, 0.65)
plt.xlim(-27.5, 28.5)

# Updated shaded regions
plt.fill_between([-25, -15], y1=0.24, y2=0.65, color="lightblue", alpha=0.2)
plt.fill_between([5, 27], y1=0.24, y2=0.65, color="red", alpha=0.12)

plt.ylabel("albedo $\\alpha$ \n(planetary reflectivity)")
plt.xlabel("Temperature [°C]")

# Updated labels
plt.text(-21, 0.27, s="completely\nfrozen", size=10, color="darkblue")
plt.text(-2, 0.27, s="partially frozen", size=10, color="darkgrey")
plt.text(15, 0.255, s="no ice", size=10, color="darkred")

plt.show()