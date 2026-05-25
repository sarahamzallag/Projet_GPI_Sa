class Atome: # Classe pour pour regrouper toutes les informations d'un atome au même endroit
    def __init__(self, base, position, chaine, name, coord): # Constructeur d'objet
        self.base = base # Stocke la base (A, C, G, U)
        self.position = position # Stocke la position numérique
        self.chaine = chaine # Stocke l'identifiant de la chaîne
        self.name = name # Stocke le nom de l'atome (N6, O2, etc.)
        self.coord = coord # Stocke le tuple de coordonnées (x, y, z)


# 1.Extraction des données
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

                    x = float(line[30:38].strip())     # Coordonnée X en decimal
                    y = float(line[38:46].strip())
                    z = float(line[46:55].strip())

                    atome_infos = Atome(base, position, chaine, name, (x, y, z)) # Création de l'objet 
                    resultat.append(atome_infos) # Ajoute l'objet directement dans la liste de résultats

                else:    
                    line = file.readline()   # On avance d'une ligne
                    continue                 # On enleve tout le reste (C, P, H, etc.)
            
            line = file.readline()

    return resultat    


# Fonction principale qui va s'exécuter quand projet_1.py l'appellera
def lancer_analyse(pdb_name):

    # 2.Visualisation
    mes_atomes = extraire_donnees(pdb_name) # On appelle la fonction et on stocke ce qu'elle renvoie dans 'mes_atomes'
    # for atome in mes_atomes[:5]: # On affiche seulement les 5 premiers 
    #     print(f"{{'base': '{atome.base}', 'position': {atome.position}, 'chaine': '{atome.chaine}', 'name': '{atome.name}', 'coord': {atome.coord}}}") # Affiche les variables de l'objet de façon lisible


    # 3.Reconstruction de la sequence
    sequence = {}
    for atome in mes_atomes: # on parcourt tous les atomes

        position = atome.position 
        base = atome.base 
        sequence[position] = base # On ne garde qu'une seule base par position

    chaine_finale = ''.join(sequence[i] for i in sorted(sequence)) # reconstruction dans l'ordre des positions

    # print("\nSequence reconstruite :")
    # print(chaine_finale)


    # 4.Classification des Donneurs et Accepteurs
    donneurs = {
        'A': ['N6'], 'C': ['N4'], 'G': ['N1', 'N2'], 'U': ['N3'], 'T': ['N3']
    }

    accepteurs = {
        'A': ['N1', 'N3', 'N7'], 'C': ['O2', 'N3'], 'G': ['O6', 'N3', 'N7'], 'U': ['O2', 'O4'], 'T': ['O2', 'O4']
    }

    liste_donneurs = []
    liste_accepteurs = []

    for atome in mes_atomes:  # On parcourt tous les atomes
        base = atome.base  
        name = atome.name 

        # On vérifie si notre atome actuel ('name') est présent dans la liste 'Donneur' 'Accepteur'
        if name in donneurs[base]:
            liste_donneurs.append(atome)
        if name in accepteurs[base]:
            liste_accepteurs.append(atome)

    # print(f"Tri terminé : {len(liste_donneurs)} donneurs et {len(liste_accepteurs)} accepteurs trouvés.")     
    # for d in liste_donneurs[:5]:
    #     print(f"{{'base': '{d.base}', 'position': {d.position}, 'name': '{d.name}', 'coord': {d.coord}}}") # Affiche le donneur au format dictionnaire pour le visuel


    # 5.Calcul des distances < 3 Angströms
    liaisons_trouvees = 0

    paires = set() # enlève automatiquement les doublons

    for d in liste_donneurs:
        for a in liste_accepteurs:
            x1, y1, z1 = d.coord 
            x2, y2, z2 = a.coord 
            
            # Formule de la distance 3D
            distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
            
            # Condition : distance max de 3 Å + ne pas faire de liaison avec la MEME base
            if distance <= 3.0  and d.position != a.position : 
                liaisons_trouvees += 1

                i = int(d.position) # Positions des nucléotides 
                j = int(a.position) 
                paires.add((min(i, j), max(i, j))) # On stocke la paire sans doublons

                # print(
                #     f"Liaison {liaisons_trouvees} : "
                #     f"{d.base}{d.position}({d.name}) " 
                #     f"<-> "
                #     f"{a.base}{a.position}({a.name}) " 
                #     f"| Dist: {distance:.2f} Å"
                # )


    # 6. Construction du dot-bracket

    position_depart = min(paires)[0] if paires else 1  # première position de la séquence

    taille = len(chaine_finale)  # longueur totale de l'ARN
    structure = ['.'] * taille   # au départ tous les nucléotides sont non appariés

    deja_apparies = set()  # évite qu'une base ait plusieurs partenaires

    # On parcourt les paires trouvées à l'étape 4
    for i, j in sorted(paires):

        idx_i = i - position_depart  # conversion position biologique -> index Python
        idx_j = j - position_depart

        lettre1 = chaine_finale[idx_i]  # base du nucléotide i
        lettre2 = chaine_finale[idx_j]  # base du nucléotide j

        combine = lettre1 + lettre2  # ex : AU, GC, GU

        # On garde seulement les paires autorisées
        if combine in ['AU', 'CG', 'GC', 'UG', 'GU']:

            # Vérifie que les nucléotides ne sont pas déjà appariés
            if i not in deja_apparies and j not in deja_apparies:

                structure[idx_i] = '('  # parenthèse ouvrante
                structure[idx_j] = ')'  # parenthèse fermante

                deja_apparies.add(i)  # marque i comme apparié
                deja_apparies.add(j)  

    dot_bracket = ''.join(structure)  # transforme la liste en chaîne finale

    #print("\n--- COMPARAISON ---")
    #print("Prof : ((((...((.(((....)))....))...))))")
    #print(f"Moi  : {dot_bracket}")

    # Affichage de la structure en dot-bracket.
    print(dot_bracket)