import numpy as np
import matplotlib.pyplot as plt

def lancer_de():
    return np.random.randint(1, 7)

def _simulate(nb_lance):
    return np.array([lancer_de() for _ in range(nb_lance)])

def plot(lance):
    plt.title(f"Distribution des résultats des lancers de dés avec {lance} lancés")

    simulate = _simulate(lance)
    simulate_mean = np.mean(simulate)
    simulate_sig = np.std(simulate)

    x = np.linspace(min(simulate), max(simulate), 101)
    y = 1 / (simulate_sig * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - simulate_mean) / simulate_sig) ** 2)

    plt.plot(x, y, color='r', label=f"Distribution gaussienne : moyenne = {simulate_mean}")
    plt.xlabel("Valeur")
    plt.ylabel("Fréquence")

    plt.grid()
    plt.legend(loc="best")

plt.figure(figsize=(15.15, 8.8))

plt.subplot(2, 2, 1)
plot(5)

plt.subplot(2, 2, 2)
plot(10)

plt.subplot(2, 2, 3)
plot(100)

plt.subplot(2, 2, 4)
plot(1000)

plt.show()

