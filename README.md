# Projet_GPI_Sa

## Description du projet

Ce projet de bioinformatique utilise les informations 3D d’un fichier PDB afin de reconstruire les appariements entre bases d’une séquence ARN et générer sa structure secondaire en notation 'dot-bracket'.  

Le script extrait les données atomiques, reconstruit la séquence nucléotidique, identifie les interactions donneurs/accepteurs puis détecte les paires de bases grâce à des calculs de distances dans l’espace 3D.  

Le projet a été développé en Python avec une approche orientée objet simple basée sur une classe 'Atom' permettant d’encapsuler les données atomiques et de faciliter les manipulations.

---

# Structure du projet

Le code est organisé sous forme de package afin d’améliorer la lisibilité et la modularité du projet .

### Fichiers principaux

- projet_1.py  
  Script principal servant de point d’entrée pour l’analyse.

- RNA/utils.py 
   Module contenant les outils et fonctions nécessaires au traitement des structures ARN.

---

# Architecture et choix techniques

## Classe Atome

Le projet utilise une classe Atome afin d’encapsuler les informations atomiques :

- base nucléotidique,
- position,
- chaîne,
- nom de l’atome,
- coordonnées 3D.

Cette approche permet une manipulation plus claire et plus structurée des données.

---

## Reconstruction de la séquence

La séquence ARN est reconstruite à partir des positions nucléotidiques extraites du fichier PDB.

Un dictionnaire est utilisé afin de :
- conserver une seule base par position,
- supprimer les doublons liés aux différents atomes d’un même nucléotide.

---

## Détection des interactions

Les interactions sont identifiées à partir :
- des atomes donneurs,
- des atomes accepteurs,
- d’un seuil de distance fixé à 3 Å.

Les distances sont calculées dans l’espace 3D à partir des coordonnées atomiques.


---

## Génération du dot-bracket

Les paires de bases valides sont converties en notation **dot-bracket** :

- `(` : nucléotide apparié ouvrant,
- `)` : nucléotide apparié fermant,
- `.` : nucléotide non apparié.

Exemple :

```txt
(((....)))
```

---

# Stratégie de développement

Le script inclut plusieurs étapes de vérification intermédiaires afin de valider progressivement chaque partie de l’algorithme :

- extraction des données,
- reconstruction de la séquence,
- classification des atomes,
- calcul des distances,
- génération de la structure secondaire.

Cette approche facilite le débogage, les tests et la maintenance du projet.

---

# Utilisation

## Prérequis

- Python 3
- aucune bibliothèque externe nécessaire

---

## Exécution

Rendre le script exécutable :

```bash
chmod +x projet_1.py
```

Lancer l’analyse :

```bash
./projet_1.py 8D28.pdb
```

---

# Exemple de sortie

```txt
Séquence : GGCGAUACCAGCCGAAAGGCCCUUGGCAGCGCC

Dot-bracket :
((((...((.(((....)))....))...))))
```

---

# Objectifs pédagogiques

Ce projet a permis de travailler sur :

- le parsing de fichiers biologiques (PDB),
- les calculs géométriques en 3D,
- l’analyse des interactions moléculaires,
- la reconstruction de structures secondaires ARN,
- ainsi qu’une première approche de la programmation orientée objet en Python.