from matplotlib import pyplot as plt
from snippets import ages_x, dev_y, py_dev_y, js_dev_y


plt.plot(
    ages_x,
    dev_y,
    color="#000000",
    linestyle="--",
    linewidth=2,
    marker=".",
    label="All dev",
)
plt.plot(ages_x, py_dev_y, color="#0000FF", marker="o", label="Python dev")
plt.plot(ages_x, js_dev_y, color="#FFFF00", marker="o", label="JavaScript dev")

plt.legend()
plt.grid()
# plt.tight_layout()
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Median salary (USD) by age")
# plt.show()
plt.savefig("salary.svg")
