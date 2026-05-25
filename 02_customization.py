import matplotlib.pyplot as plt
import numpy as np


x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 31, 45])
y2 = np.array([25, 18, 21, 28])

line_style = dict(marker=".", markersize=10, markerfacecolor="cyan", linestyle="solid", linewidth=2, color="red")

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)

plt.show()