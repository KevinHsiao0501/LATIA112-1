import numpy as np
import matplotlib.pyplot as plt

epsilon = 0 
t = t1 = t2 =  1
a = a1 = a2 =  1

def dispersion_relation(kx, ky):
    return epsilon - 2 * t * (np.cos(kx * a) + np.cos(ky * a))

k_values = np.linspace(-np.pi/a, np.pi/a, 100)
KX, KY = np.meshgrid(k_values, k_values)

E_values = dispersion_relation(KX, KY)

plt.figure(figsize=(8, 6))
plt.contourf(KX, KY, E_values, cmap='viridis')
plt.colorbar(label='E')
plt.xlabel('$k_x$')
plt.ylabel('$k_y$')
plt.show()


