"""
Aide au calcul de la répartition des subventions de la mairie
 pour les associations.

@auteur: Rod <rod.cat@free.fr>  License libre
"""

from tkinter import *
from tkinter import ttk
import pickle


def verif(dic, nom):
    """
    Vérifie la présence d'une association dans le fichier.
    """
    if nom in dic:
        vrai = 1
    else:
        vrai = 0
    return vrai

def nouvelle_asso():
    """
    Ajoute une nouvelle association au fichier.
    Initialisation des valeurs liées aux associations:
    nom, nombre d'adhérents (nbadh), montant de l'adhésion (adh),
    trésorerie (tres), nombre de salariés (sal),
    occupation de locaux (loc), subventions extérieures (sub),
    montant de la demande (dem)
    """
    nom = (entr1.get()).lower()
    nbadh = int(entr2.get())
    adh = float(entr3.get())
    tres = float(entr4.get())
    sal = int(entr5.get())
    loc = int(entr6.get())
    sub = float(entr7.get())
    dem = float(entr8.get())
    try:
        fichAssos = open("assos", 'rb')
        listAssos = pickle.load(fichAssos)
        fichAssos.close()
        if verif(listAssos, nom):
            confirm.configure(text = "L'association "
                              + nom + " est déjà enregistrée")
        else:
            listAssos[nom] = [nbadh, adh, tres, sal, loc, sub, dem]
            fichAssos = open("assos", 'wb')
            pickle.dump(listAssos, fichAssos)
            fichAssos.close()
            confirm.configure(text = "L'association "
                              + nom + " est bien enregistrée")
        
    except:
        listAssos = {}
        fichAssos = open("assos", 'wb')
        listAssos[nom] = [nbadh, adh, tres, sal, loc, sub, dem]
        pickle.dump(listAssos, fichAssos)
        fichAssos.close()
        confirm.configure(text = "L'association "
                          + nom + " est bien enregistrée")
    
def listing():
    """
    liste les associations déjà enregistrées.
    """
    try:
        fichAssos = open("assos", 'rb')        
        listAssos = pickle.load(fichAssos)        
        fichAssos.close()
        contenu = ""
        for asso in listAssos:
            contenu += asso + ", " + str(listAssos[asso][0])
            + " adhérents" + "\n"
        liste.configure(text = contenu)
            
        
        
    except:
        liste.configure(text = "Fichier vide")
    
    
def vidage():
    """
    Vide les champs du formulaire.
    """
    entr1.delete(0, END)
    entr2.delete(0, END)
    entr3.delete(0, END)
    entr4.delete(0, END)
    entr5.delete(0, END)
    entr6.delete(0, END)
    entr7.delete(0, END)
    entr8.delete(0, END)
    entr9.delete(0, END)
        
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
        contenu = ""
        try:
            sub = float(entr9.get())
            for asso, val in listAssos.items():
                dic[asso] = val[0]*adherent.get()
                + val[1]*adhesion.get()
                + val[2]*tresorerie.get()
                + val[3]*salarie.get()
                - val[4]*salle.get()
                -val[5]*subvention.get()
                + val[6]
                total += dic[asso]
            for k in dic:
                pourcent = dic[k]/(total/100)
                assob = sub/100*pourcent
                contenu += k + " " + str(round(pourcent, 2))
                + "% = " + str(round(assob, 2)) + "€\n"
            liste.configure(text = contenu)
            confirm.configure(text = "Résultat: ")
        except:
            confirm.configure(text = "Entrez une somme à répartir")
    except:
        confirm.configure(text = "Aucune associations dans le fichier")


fen = Tk()
fen.title("Aide à la répartition des subventions")

ttk.Label(fen, text = "Association: ").grid(row = 0, sticky = W)
ttk.Label(fen, text = "Nombre d'adhérents: ").grid(row = 1, sticky = W)
ttk.Label(fen, text = "Montant de l'adhésion: ").grid(row = 2, sticky = W)
ttk.Label(fen, text = "Trésorerie: ").grid(row = 3, sticky = W)
ttk.Label(fen, text = "Salarié(es): ").grid(row = 4, sticky = W)
ttk.Label(fen, text = "Occupation des salles: ").grid(row = 5, sticky = W)
ttk.Label(fen, text = "Subventions extérieures: ").grid(row = 6, sticky = W)
ttk.Label(fen, text = "Montant de la demande: ").grid(row = 7, sticky = W)
ttk.Label(fen, text = "Montant total à répartir").grid(row = 9, sticky = W)
entr1 = ttk.Entry(fen, width=30)
entr2 = ttk.Entry(fen, width=30)
entr3 = ttk.Entry(fen, width=30)
entr4 = ttk.Entry(fen, width=30)
entr5 = ttk.Entry(fen, width=30)
entr6 = ttk.Entry(fen, width=30)
entr7 = ttk.Entry(fen, width=30)
entr8 = ttk.Entry(fen, width=30)
entr9 = ttk.Entry(fen, width=30)
entr1.grid(row = 0, column = 1)
entr2.grid(row = 1, column = 1)
entr3.grid(row = 2, column = 1)
entr4.grid(row = 3, column = 1)
entr5.grid(row = 4, column = 1)
entr6.grid(row = 5, column = 1)
entr7.grid(row = 6, column = 1)
entr8.grid(row = 7, column = 1)
entr9.grid(row = 9, column = 1)
ttk.Button(fen, text = "Enregistrer", command = nouvelle_asso).grid(row = 8,
                                                                sticky = W)
ttk.Button(fen, text = "Nouveau", command = vidage).grid(row = 8, column = 1,
                                                     sticky = W)
ttk.Button(fen, text = "Listing", command = listing).grid(row = 8, column = 2
                                                      , sticky = W)
ttk.Button(fen, text = "Calcul", command = coef).grid(row = 10, sticky = W)
confirm = ttk.Label(fen)
confirm.grid(row = 11)
liste = ttk.Label(fen)
liste.grid(row = 11, column = 1)



adherent = Scale(fen, length=250, orient=HORIZONTAL, label="Adhérents",
                 sliderlength=20, showvalue=0, from_=-10,
                 to=10, tickinterval=1)
adherent.grid(row = 12)
adhesion = Scale(fen, length=250, orient=HORIZONTAL, label="Adhésion",
                 sliderlength=20, showvalue=0, from_=-10, to=10,
                 tickinterval=1)
adhesion.grid(row = 12, column = 1)
tresorerie = Scale(fen, length=250, orient=HORIZONTAL, label="Trésorerie",
                 sliderlength=20, showvalue=0, from_=-10, to=10,
                 tickinterval=1)
tresorerie.grid(row = 12, column = 2)
salarie = Scale(fen, length=250, orient=HORIZONTAL, label="Salarié(es)",
                 sliderlength=20, showvalue=0, from_=-10, to=10,
                 tickinterval=1)
salarie.grid(row = 13)
salle = Scale(fen, length=250, orient=HORIZONTAL, label="Occupation de salle",
                 sliderlength=20, showvalue=0, from_=-10, to=10,
                 tickinterval=1)
salle.grid(row = 13, column = 1)
subvention = Scale(fen, length=250, orient=HORIZONTAL, label="Subventions ext",
                 sliderlength=20, showvalue=0, from_=-10, to=10,
                 tickinterval=1)
subvention.grid(row = 13, column = 2)

fen.mainloop()

