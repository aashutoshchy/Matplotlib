import matplotlib.pyplot as plt
import numpy as np

hours_studied = np.array([0, 1, 1, 2, 3, 4])
grades = np.array([1, 23, 22, 34, 46, 52])

plt.scatter(hours_studied, grades, color="red", alpha=0.9, s=10, label="Class A")

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")

plt.legend()
plt.show()