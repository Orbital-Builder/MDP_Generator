import random

"""


Code by Orbital-Builder.
Aide : Github Copilot.
Aide : UDEMY - Jean-Philippe Parein. 
Version 1.4.
-----------------------------------


"""


def generer_mot_de_passe(longueur):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    mot_de_passe = "".join(random.sample(caracteres, longueur))
    return mot_de_passe

def generer_mot_de_passe_caractere(long):
    carac_spe = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    mdp = "".join(random.sample(carac_spe, long))
    return mdp

def extraire_mdp_fichier(nom_fichier, longueur, nb_mdp, special=False):
    with open(nom_fichier, "w") as fichier:
        for i in range(nb_mdp):
            if special:
                mdp = generer_mot_de_passe_caractere(longueur)
            else:
                mdp = generer_mot_de_passe(longueur)
            fichier.write(f"{mdp}\n")

if __name__ == "__main__":
    extraire_mdp_fichier("mot_de_passe.txt", 18, 15)
    print("Les mots de passe ont été générés et enregistrés dans le fichier mot_de_passe.txt")
    
    extraire_mdp_fichier("mot_de_passe_caractères.txt", 18, 15, special=True)
    print("Les mots de passe avec caractères spéciaux ont été générés et enregistrés dans le fichier mot_de_passe_caractères.txt")







