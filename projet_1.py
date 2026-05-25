#!/usr/bin/env python3

import sys      # contient une liste pour les arguments de la ligne de commande
import RNA.utils as utils # On importe notre package maison RNA (qui contient utils.py)
              
if len(sys.argv) != 2: # Vérifie qu'on a bien passé un seul argument (le fichier PDB)
    print('Error')
    print('Usage:')
    print('>' + sys.argv[0] + ' file.pdb')
    exit() # Arrête le script si l'argument est manquant

pdb_name = sys.argv[1] # Récupère le nom du fichier PDB (ex: 8D28.pdb)

# On appelle la fonction de utils.py en lui passant le nom du fichier
utils.lancer_analyse(pdb_name) # Déclenche toute l'analyse stockée dans le package