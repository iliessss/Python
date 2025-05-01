import numpy as np
import matplotlib.pyplot as plt

def Fn(n):
    return 1./np.sqrt(5) * (((1+np.sqrt(5)) / 2.)**n - ((1-np.sqrt(5)) / 2.)**n)

def phi(n):
    return Fn(n+1) / Fn(n)

n = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.figure(figsize=(14.25, 8.15))

plt.title("Suite de Fibonacci")
plt.plot(n, Fn(n))

plt.show()

plt.figure(figsize=(14.25, 8.15))
plt.title("Nombre d'Or : $\phi=1,618...$")

n1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
phi_ex = np.ones_like(n1) * (1 + np.sqrt(5)) / 2.

plt.plot(n1, phi(n1), "r-o",label="Termes successif de $F_n$")
plt.plot(n1, phi_ex, label="$\\phi_{ex}$")

plt.legend()
plt.show()