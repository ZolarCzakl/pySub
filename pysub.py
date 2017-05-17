#!/usr/bin/env python3

"""
Created on Thu May  4 10:03:51 2017

@author: rod  Licence: GPL

Aide au calcul des subventions associatives.
"""
import pickle


class Assos:
    def __init__(self, nom, nbadh, adh, tres, sal, loc, sub, dem):
        """
        Initialisation des valeurs liées aux associations:
        nom, nombre d'adhérents (nbadh), montant de l'adhésion (adh), trésorerie (tres), nombre de salariés (sal), occupation de locaux (loc), subventions extérieures (sub), montant de la demande (dem)
        """
        self.nom = nom
        self.nbadh = nbadh
        self.adh = adh
        self.tres = tres
        self.sal = sal
        self.loc = loc
        self.sub =sub
        self.dem = dem


def nouvelle_asso():
    nom = input("Nom de l'association: ")
    nbadh = int(input("Nombre d'adhérants: "))
    adh = float(input("Montant de l'adhésion: "))
    tres = float(input("Montant de la trésorerie: "))
    sal = int(input("Nombre de salarié: "))
    loc = int(input("Occupation des salles: "))
    sub = float(input("Subventions extérieures: "))
    dem = float(input("Montant de la demande: "))
    asso = Assos(nom, nbadh, adh, tres, sal, loc, sub, dem)
    try:
        fichAssos = open("assos", 'ab')
        listAssos = pickle.load(fichAssos)
        listAssos.append(asso)
        pickle.dump(listAssos, fichAssos)
        fichAssos.close()
    except:
        fichAssos = open("assos", 'wb')
        listAssos = [asso]
        pickle.dump(listAssos, fichAssos)
        fichAssos.close()
        
def coef():
    fichAssos = open("assos", 'rb')
    listAssos = pickle.load(fichAssos)
    fichAssos.close()
    dic = {}
    total = 0
    for asso in listAssos:
        dic[asso.nom] = asso.nbadh +asso.adh +asso.tres +asso.sal +asso.loc +asso.sub +asso.dem
        total += dic[asso.nom]
    for k in dic:
        print(k, dic[k]/(total/100),"%")
    
choix = ""
while choix != "q":
    choix = input("Entrez 'o' pour ajouter une nouvelle association, 'c' pour les coef et 'q' pour quitter.")
    if choix == "o":
        nouvelle_asso()
    elif choix == "c":
        coef()
    
