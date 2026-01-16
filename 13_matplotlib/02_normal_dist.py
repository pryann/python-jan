import matplotlib.pyplot as plt
import numpy as np


data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=25, density=True)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Normal distribution")
plt.show()
