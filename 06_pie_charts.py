import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([300, 231, 280, 213])
colors = ["Red", "Blue", "Green", "Yellow"]

plt.pie(values, labels=categories, autopct="%1.1f", colors=colors, explode=[0.1, 0.1, 0.1, 0.1])
plt.title("Herald College")

plt.show()