"""
Ce programme permet d'optimiser la découpe de poutres métallique ou bois dans des longueurs de poutres standard 
et ainsi connaître le nombre minimal de poutre à acheter.
Exemple : 
Poutres achetées dans le commerce : longueur 5000 mm
Poutres à découper : 10 longueurs de 400mm, 20 longueurs de 1600mm, etc...
"""

"""Variables de calcul"""
longueur = 1
nombre = 0
ma_liste = []
i = 0
barre = 0
resultat_a = 0
total_a = 0
end = 'n'

epaisseur_lame = input("Epaisseur de la lame (mm) : ")
epaisseur_lame = int(epaisseur_lame)
section_barre = input("Type de barre (TCAR50x3) : ") #Ex : TCAR 50x3
longueur_barre = input("Longueurs des barres achetées (mm) : ")
longueur_barre = int(longueur_barre)

"""Recupération du nombre et longueurs des barres"""
print("\n\nMise en barre")
print("Liste des barres à découper\n")

while end != 'o':
    nombre = input("Nombre de barre(s) : ")
    nombre = int(nombre)
    longueur = input("Longueur barre(s) : ")
    longueur = int( longueur )
    end = input("Fin o/n : ")
    for i in range(nombre):
        if longueur != 0:
            ma_liste.append(longueur)
ma_liste.sort(reverse=True)
#ma_liste.reverse()

print ("\nListe des barres à découper :", ma_liste)

"""Fait le cumule des longueurs"""
for i in range(len(ma_liste)):
    total_a = total_a + ma_liste[i]
print ("Linéaire des ", section_barre, " :", total_a, "ml")

"""Boucle de mise en barre"""
while total_a != 0:
    """Incrémente les No des Barres"""
    barre += 1
    print("Barre No : ", barre)
    """Boucle for qui cumule les barres"""
    for i in range (len(ma_liste)):
        """Incrémente le résultat"""
        resultat_a = resultat_a + ma_liste[i] + epaisseur_lame
        """Conditions de triage des barres"""
        if resultat_a <= longueur_barre :
            if ma_liste[i] != 0:
                print (" -", ma_liste[i], end = "")
            """Remplace la longueur de la barre par 0 pour indiquer qu elle est utilisé"""
            ma_liste[i] = 0
        elif resultat_a > longueur_barre:
            resultat_a = resultat_a - ma_liste[i]
    print(end =" -")
    print()
    
    """Boucle for fini retour à 0 pour résultat_a"""
    resultat_a = 0

    """Boucle qui contrôle si toutes les barres ont été utilisé"""
    total_a = 0
    for i in range (len(ma_liste)):
        total_a = total_a + ma_liste[i]

quit = input("Quitter")





