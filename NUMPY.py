import numpy as np

a = np.array([[1, 2, 3], [3, 5, 7]])
np.savetxt("massive.txt", a)

b = np.loadtxt("massive.txt")

c = np.array([1, 2, 3])

newArray = np.array([c, [10, 11, 12]])
print(newArray)