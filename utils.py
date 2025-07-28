import numpy as np

def creer_grille(xmin=-5, xmax=5, ymin=-5, ymax=5, pas=0.5):
    x = np.arange(xmin, xmax + pas, pas)
    y = np.arange(ymin, ymax + pas, pas)
    X, Y = np.meshgrid(x, y)
    return X, Y

def champ_rotation(X, Y):
    U = -Y
    V = X
    return U, V

def champ_radial(X, Y):
    norme = np.sqrt(X**2 + Y**2) + 1e-8  # pour éviter la division par zéro
    U = X / norme
    V = Y / norme
    return U, V

def champ_spiral(X, Y):
    norme = np.sqrt(X**2 + Y**2) + 1e-8
    U = -Y / norme
    V = X / norme
    return U, V