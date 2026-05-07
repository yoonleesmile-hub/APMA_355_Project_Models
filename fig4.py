import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 4, 500)
stable_branch = np.sqrt(r)
unstable_branch = -np.sqrt(r)

plt.figure(figsize=(7, 5))

plt.plot(r, stable_branch, label="Stable equilibrium: $x = +\\sqrt{r}$")
plt.plot(r, unstable_branch, linestyle="--", label="Unstable equilibrium: $x = -\\sqrt{r}$")
plt.scatter([0], [0], s=60, label="Bifurcation point")

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.title("Saddle-Node Bifurcation Diagram for $x' = r - x^2$")
plt.xlabel("Parameter $r$")
plt.ylabel("Equilibrium $x^*$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()