#!/usr/bin/env python3
"""

'''
class Protein: #classe
   def __init__(self,name): #init et self convention qui doivent tjrs etre presente 
        self.nom = name


protein1 = Protein('hemoglobin') #prot1 est une instance de la classe Protein
protein2 = Protein('cytochrom c')

print(protein1.nom)
print(protein2.nom)

'''


class Protein :
 def __init__(self,name):
    self.folded = True # on part du principe que toutes les proteines sont d'abord repliées
    self.name = name
    
 
 def unfold(self):
    self.folded = False

 def fold(self):
    self.folded = True

class FoldableProtein(Protein):
 def fold(self) :
    print(self.name + 'is not foldable')

prot1 = Protein('hgb')
prot2 = Protein('cytochrome C')
prot3 = FoldableProtein('ovalbumin')

proteome = [prot1,prot2,prot3]


print('before')
'''
for prot in proteome :
 print (prot.name + ' is folded:' , prot.folded)

for prot in proteome :
 prot.unfold()

print('after')
for prot in proteome:
 print (prot.name + ' is folded: ',prot.folded)

for prot in proteome :
 prot.fold()
 '''

for prot in proteome:
  print('Protein '+prot.name + ' is a Protein:',isinstance(prot,Protein))
  print('Protein '+prot.name + ' is a FoldableProtein:',isinstance(prot,Protein))

"""




#Lecture d'un fichier pdb

lines =[]
with open('8D28.pdb','r') as file:
    for i in range(1000):
        lines.append(file.readline())

for line in lines:
    if line[:4] == 'ATOM' :
     print(line)




