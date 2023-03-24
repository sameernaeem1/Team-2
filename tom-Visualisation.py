import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
fig.suptitle("Figure title", fontsize=20)
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)
ax.plot(input_values, squares, 'mD:')
plt.show()