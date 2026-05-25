import matplotlib.pyplot as plt
import numpy as np


x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 31, 45])
y2 = np.array([25, 18, 21, 28])
y3 = np.array([12, 10, 17, 24])

plt.title("Class Size", fontsize=20, family="Poppins", fontweight="bold", color="blue")

plt.xlabel("Year", fontsize=10, family="Arial")
plt.ylabel("Year", fontsize=10, family="Arial", color="red")

plt.tick_params(axis="both", colors="orange")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()