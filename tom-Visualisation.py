import matplotlib.pyplot as plt

goals = [55, 65, 75, 85, 95, 105, 115]
amountscored = [73,58,93,66,100,84,71,80,106,95,102,83,99]
fig, ax = plt.subplots()
fig.suptitle("Figure title", fontsize=20)
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)
ax.plot(goals, amountscored, 'mD:')
plt.show()