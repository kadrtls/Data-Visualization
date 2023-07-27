import matplotlib.pyplot as plt
import numpy as np

#enter the x coordinates
x_points = np.array([1,2,6,8])
#enter the x coordinates
y_points = np.array([3,8,1,10])

plt.figure(figsize=(9,3))
plt.subplot(131)

plt.bar(x_points,y_points)
plt.show()