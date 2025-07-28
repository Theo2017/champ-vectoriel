import matplotlib.pyplot as plt
import numpy as np

def afficher_champ(X, Y, U, V, titre="Champ vectoriel"):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.quiver(X, Y, U, V, color='blue', pivot='mid', scale=20)
    ax.set_title(titre)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")
    ax.grid(True)
    plt.show()