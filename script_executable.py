#!/usr/bin/env python3

# script executable 
# le rendre executable : chmod +x script_executable.py ds terminal sans ecrire python3 devant
# on veut pouvoir faire : ./script_executable.py 8D28.pdb

import sys      # contient une liste
import RNA.utils as utils
              
if len(sys.argv) != 2:
    print('Error')
    print('Usage:')
    print('>' + sys.argv[0] + ' file.pdb')
    exit()

pdb_name = sys.argv[1]


def extraire_donnees(pdb_name):
    resultat = [] # Liste vide pour stocker les résultats 

    with open(pdb_name, 'r') as file:
        line = file.readline()  
        while line[0:6].strip() != 'TER': 
            if line[0:7].strip() == 'ATOM': # Vérifie si la ligne correspond à un atome
                name = line[12:16].strip()  # Nom de l'atome
                
                if (name.startswith('N') or name.startswith('O')) and not name.startswith('OP') and "'" not in name: 
                    base = line[17:20].strip() # Identification de la base (A,C,G,U)
                    chaine = line[21]            # Identification de la chaine (A, B)
                    position = int(line[22:26].strip()) # Position du nucléotide

                    x = line[30:38].strip()     # Coordonnée X
                    y = line[38:46].strip()
                    z = line[46:55].strip()

                    atome_infos = {
                        'base': base,
                        'position': position,
                        'chaine': chaine,
                        'name': name,       # On rajoute ça pour l'étape 3 d'après !
                        'coord': (x, y, z)  # On garde les coordonnées au cas où
                    }
                    resultat.append(atome_infos) # Correction : on utilise 'resultat'

                else:    
                    line = file.readline()   # On avance d'une ligne
                    continue                 # On enleve tout le reste (C, P, H, etc.)
            
            line = file.readline()

    return resultat    




# 1.Visualisation
mes_atomes = extraire_donnees(pdb_name) # On appelle la fonction et on stocke ce qu'elle renvoie dans 'mes_atomes'
for atome in mes_atomes[:5]: # On affiche seulement les 5 premiers 
    print(atome)



# 2.Reconstruction de la sequence
sequence = {}
for atome in mes_atomes: # on parcourt tous les atomes

    position = atome['position']
    base = atome['base']
    sequence[position] = base # On ne garde qu'une seule base par position

chaine_finale = ''.join(sequence[i] for i in sorted(sequence)) # reconstruction dans l'ordre des positions

print("\nSequence reconstruite :")
print(chaine_finale)



# 3.Classification des Donneurs et Accepteurs
donneurs = {
    'A': ['N6'], 'C': ['N4'], 'G': ['N1', 'N2'], 'U': ['N3'], 'T': ['N3']
}

accepteurs = {
    'A': ['N1', 'N3', 'N7'], 'C': ['O2', 'N3'], 'G': ['O6', 'N3', 'N7'], 'U': ['O2', 'O4'], 'T': ['O2', 'O4']
}

liste_donneurs = []
liste_accepteurs = []

for atome in mes_atomes:  # On parcourt tous les atomes
    base = atome['base']  # On récupère le nom de la base (ex: 'A')
    name = atome['name']  # On récupère le nom de l'atome (ex: 'N6')


# On vérifie si notre atome actuel ('name') est présent dans la liste 'Donneur' 'Accepteur'
    if name in donneurs[base]:
        liste_donneurs.append(atome)
    if name in accepteurs[base]:
        liste_accepteurs.append(atome)

print(f"Tri terminé : {len(liste_donneurs)} donneurs et {len(liste_accepteurs)} accepteurs trouvés.")     
for d in liste_donneurs[:5]:
    print(d)   