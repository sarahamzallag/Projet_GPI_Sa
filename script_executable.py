#!/usr/bin/env python3

# script executable 
#le rendre excutable : chmod +x script_excutable.py ds terminal sans ecrir python3 devant
#on veut pouvoir faire ' script_excutable.py 8D28.pdb




import sys      #contient un list
import RNA.utils as utils
              
if len(sys.argv) != 2:
    print('Error')
    print('Usage:')
    print ('>' +sys.argv[0] + 'file.pdb')
    exit ()

pdb_name = sys.argv[1]


with open (pdb_name, 'r') as file :
    line = file.readline()  
    while line [0:6].strip() != 'TER' : 
        if line[0:7].strip() == 'ATOM': # Vérifie si la ligne correspond à un atome

            name = line[12:16].strip()  # Nom de l'atome
            
            
            if (name.startswith('N') or name.startswith('O'))and not name.startswith('OP') and "'" not in name: # On ne garde slmt les Azotes et  Oxygenes ET on eleve les ribose 
             
                base = line[17:20].strip() # Identification de la base (A,C,G,T)
                chaine = line[21]            # Identification de la chaine (A, B)
                position = int(line[22:26].strip()) # Position du nucléotide dans la chaîne

                x = line[30:38].strip()     # Coordonnée X
                y = line[38:46].strip()
                z = line[46:55].strip()
                print(base, position, chaine,name, x, y, z)
            else:    
                line = file.readline()   # On avance d'une ligne
                continue                 # On enleve tout le reste (C, P, H, etc.)
        
        line = file.readline()