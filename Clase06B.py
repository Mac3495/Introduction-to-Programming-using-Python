import matplotlib.pyplot as plt
import numpy as np


def lineal(x):
    # f(x) = a * x + b
    return 1 * x + 1


x = np.linspace(1, 5, 20)
print(x)
x1 = [1, 2, 3, 4, 5]
y1 = [8, 3, 2, 4, 3]

x2 = [1, 2, 3, 4, 5]
y2 = [7, 6, 8, 10, 6]

plt.plot(x1, y1, label='Gastos', linewidth=4, color='red')
plt.plot(x2, y2, label='Ingresos', linewidth=4, color='blue')

plt.plot(x, lineal(x))
plt.title('Estadisticas')
plt.xlabel('Dias transcurridos')
plt.ylabel('Costos')
plt.legend()
plt.grid()
plt.show()