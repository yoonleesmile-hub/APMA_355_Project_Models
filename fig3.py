import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)
r_values = [-1, 0, 1]

plt.figure(figsize=(7, 5))

for r in r_values:
    f = r - x**2
    plt.plot(x, f, label=f"r = {r}")

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.title("Canonical Saddle-Node Equation: $x' = r - x^2$")
plt.xlabel("x")
plt.ylabel("$f(x;\\ r) = r - x^2$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()