import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_toroide(R=3, r=1, resolution=100):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, 2 * np.pi, resolution)
    u, v = np.meshgrid(u, v)

    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)

    return x, y, z, "Toroide"

def plot_paraboloide(a=1, resolution=100):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, 2, resolution)
    u, v = np.meshgrid(u, v)

    x = v * np.cos(u)
    y = v * np.sin(u)
    z = a * v**2

    return x, y, z, "Paraboloide de Revolução"

def plot_hiperboloide(tipo='um_folha', resolution=100):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(-2, 2, resolution)
    u, v = np.meshgrid(u, v)

    if tipo == 'um_folha':
        x = np.cosh(v) * np.cos(u)
        y = np.cosh(v) * np.sin(u)
        z = np.sinh(v)
        title = "Hiperboloide de Uma Folha"
    else:
        x = np.sinh(v) * np.cos(u)
        y = np.sinh(v) * np.sin(u)
        z = np.cosh(v)
        title = "Hiperboloide de Duas Folhas"

    return x, y, z, title

def plot_superficie(x, y, z, title="Superfície"):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', alpha=0.9)
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    superficies = [
        plot_toroide(),
        plot_paraboloide(),
        plot_hiperboloide(tipo='um_folha'),
        plot_hiperboloide(tipo='duas_folhas')
    ]

    for x, y, z, titulo in superficies:
        plot_superficie(x, y, z, titulo)
