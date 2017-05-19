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
        nom, nombre d'adhérents (nbadh), montant de l'adhésion (adh), trésorerie (tres),
        nombre de salariés (sal), occupation de locaux (loc), subventions extérieures (sub),
        montant de la demande (dem)
        """
        self.nom = nom
        self.nbadh = nbadh
        self.adh = adh
        self.tres = tres
        self.sal = sal
        self.loc = loc
        self.sub =sub
        self.dem = dem



        
def coef():
    """ 
    Calcul du pourcentage affecté à chaque association
    """
    try:
        fichAssos = open("assos", 'rb')
        listAssos = pickle.load(fichAssos)
        fichAssos.close()
        dic = {}
        total = 0
        for asso in listAssos:
            dic[asso.nom] = asso.nbadh +asso.adh +asso.tres +asso.sal -asso.loc -asso.sub +asso.dem
            total += dic[asso.nom]
        for k in dic:
            print(k, dic[k]/(total/100),"%")
    except:
        print("Aucune associations dans le fichier")
    

