import matplotlib.pyplot as plt

x = [2023, 2024, 2025, 2026]
y1 = [15, 25, 30, 20]
y2 = [33, 23, 32, 25]
y3 = [13, 15, 20, 30]

line_style = dict(marker=".", markersize = 20, markerfacecolor="cyan", markeredgecolor="Black", linestyle = "dashed", linewidth= 4, color="#021A54")

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)

plt.show()
