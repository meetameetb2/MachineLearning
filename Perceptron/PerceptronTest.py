import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('iris.data', header=None)
# print(df.tail())

y = df.iloc[0:100, 4].values
# print(y)
y = np.where(y == 'Iris-setosa', -1,1) # if y == 'Iris-setosa', make class label as -1 else 1
# print(y)

X = df.iloc[0:100,[0,2]].values # petal length and sepal length are selected

# plt.scatter(X[:50, 0], X[:50, 1],color = 'red', marker = 'o', label = 'setosa')
# plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', marker = 'x', label = 'versicolor')
# plt.xlabel('sepal length [cm]')
# plt.ylabel('petal length [cm]')
# plt.legend(loc='upper left')
# plt.show()