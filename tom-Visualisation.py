import matplotlib.pyplot as plt
season = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
amountscored = [73,58,93,66,100,84,71,80,106,95,102,83,99]
fig, (left) = plt.subplots(1)
left.set_title("Manchester City Goals Over Every Year (2000s)")
left.bar(season, amountscored)
plt.show()

