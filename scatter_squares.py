import matplotlib.pyplot as plt

plt.style.use('seaborn')

x_values = range(1, 100)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)
plt.show()
