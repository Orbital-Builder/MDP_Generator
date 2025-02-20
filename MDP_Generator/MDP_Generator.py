import random

def generer_mot_de_passe(longueur):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    mot_de_passe = "".join(random.sample(caracteres, longueur))
    return mot_de_passe

def extraire_mdp_fichier(nom_fichier, longueur, nb_mdp):
    with open(nom_fichier, "w") as fichier:
        for i in range(nb_mdp):
            mdp = generer_mot_de_passe(longueur)
            fichier.write(f"{mdp}\n")

if __name__ == "__main__":
    extraire_mdp_fichier("mot_de_passe.txt", 18, 15)
    print("Les mots de passe ont été générés et enregistrés dans le fichier mot_de_passe.txt")







