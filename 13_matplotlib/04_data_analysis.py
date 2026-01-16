import numpy as np
from matplotlib import pyplot as plt
from snippets import ages_x, py_dev_y, js_dev_y

width = 0.25
plt.style.use("seaborn-v0_8-bright")
x_indexes = np.arange(len(ages_x))
# plt.xticks(ticks=x_indexes, labels=ages_x)
plt.bar(x_indexes, py_dev_y, width=width, color="#0000FF", label="Python devs")
plt.bar(x_indexes + width, js_dev_y, width=width, color="#F0EE00", label="JS devs")
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Median salary in USD by age")
plt.legend()
plt.grid()
plt.show()
