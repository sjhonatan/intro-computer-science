"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:47:21 2017
Number of code lines: 
21
"""
import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(9)
y_axis = np.arange(9)

plt.figure(figsize=(20,20))
plt.scatter(x_axis,y_axis)
plt.grid(True)
plt.axes().set_aspect('equal', 'datalim')
plt.show()

print('done')
plt.figure(figsize=(20,20))
x_axis = np.arange(9)
y_axis = np.arange(9)
y_axis *= 3
plt.scatter(x_axis, y_axis)
plt.grid(True)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
