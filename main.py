from utils import creer_grille, champ_rotation, champ_radial, champ_spiral
from visualisation import afficher_champ

def menu():
    print("=== Visualisation de champs vectoriels ===")
    print("1 - Champ rotation")
    print("2 - Champ radial")
    print("3 - Champ spirale")
    choix = input("Choisissez un champ à visualiser (1/2/3) : ")
    return choix

def main():
    X, Y = creer_grille()

    choix = menu()

    if choix == "1":
        U, V = champ_rotation(X, Y)
        titre = "Champ de rotation"
    elif choix == "2":
        U, V = champ_radial(X, Y)
        titre = "Champ radial"
    elif choix == "3":
        U, V = champ_spiral(X, Y)
        titre = "Champ spirale"
    else:
        print("❌ Choix invalide.")
        return

    afficher_champ(X, Y, U, V, titre)

if __name__ == "__main__":
    main()
