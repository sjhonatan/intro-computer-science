"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 19:26:59 2017
Number of code lines: 
15
"""
#teste
import matplotlib.pyplot as plt
import numpy as np
import time
x_axis = np.arange(9)
y_axis = np.arange(9)

plt.scatter(x_axis,y_axis)
plt.show()

print('acabou')
print('isso só vai ser printado depois de eu fechar a imagem')
time.sleep(2)

plt.scatter(x_axis,y_axis)
plt.show()
