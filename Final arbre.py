from Arbre import *


def arbre_insertion(T,y):
    x=T
    while T!= None :
        x=T
        if y<x.valeur:
            T=x.get_gauche()
        else:
            T=x.get_droit()
    if y<x.valeur:
        x.insert_gauche(y)
    else :
        x.insert_droit(y)

arbre= None
with open('noms.txt','r') as file:
    for line in file:
        contenu= line.strip()
        if arbre is None:
            arbre = ArbreBinaire(contenu)
        else:
            arbre_insertion(arbre,contenu)

def prefixe(arb,file):
    if arb!= None :
        file.write(arb.valeur + "\n")
        prefixe(arb.get_gauche(),file)
        prefixe(arb.get_droit(),file)
def infixe(arb,file):
    if arb!= None :
        infixe(arb.get_gauche(),file)
        file.write(arb.valeur + "\n")
        infixe(arb.get_droit(),file)
def postfixe(arb,file):
    if arb!= None :
        postfixe(arb.get_droit(),file)
        postfixe(arb.get_gauche(),file)
        file.write(arb.valeur+ "\n")


with open("prefixe.txt","r+") as liste_prefixe:
    prefixe(arbre,liste_prefixe)
    print(liste_prefixe.readlines())
with open("infixe.txt","r+") as liste_infixe :
    infixe(arbre,liste_infixe)
    print(liste_infixe.readlines())
with open("postfixe.txt","r+") as liste_postfixe:
    postfixe(arbre,liste_postfixe)
    print(liste_postfixe.readlines())

