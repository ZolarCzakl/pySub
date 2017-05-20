"""
Aide au calcul de la répartition des subventions de la mairie pour les associations.

@auteur: Rod <rod.cat@free.fr>  License libre
"""




from tkinter import *
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

def verif(liste, nom):
    """
    Vérifie la présence d'une association dans le fichier.
    """
    for asso in liste:
        if asso.nom == nom:
            vrai = 1
            break
        else:
            vrai = 0
    return vrai

def nouvelle_asso():
    """
    Ajoute une nouvelle association au fichier.
    """
    nom = (entr1.get()).lower()
    nbadh = int(entr2.get())
    adh = float(entr3.get())
    tres = float(entr4.get())
    sal = int(entr5.get())
    loc = int(entr6.get())
    sub = float(entr7.get())
    dem = float(entr8.get())
    asso = Assos(nom, nbadh, adh, tres, sal, loc, sub, dem)
    try:
        fichAssos = open("assos", 'rb')
        listAssos = pickle.load(fichAssos)
        fichAssos.close()
        if verif(listAssos, nom):
            confirm.configure(text = "L'association " + nom + " est déjà enregistrée")
        else:
            listAssos.append(asso)
            fichAssos = open("assos", 'wb')
            pickle.dump(listAssos, fichAssos)
            fichAssos.close()
            confirm.configure(text = "L'association " + asso.nom + " est bien enregistrée")
        
    except:
        fichAssos = open("assos", 'wb')
        listAssos = [asso]
        pickle.dump(listAssos, fichAssos)
        fichAssos.close()
        confirm.configure(text = "L'association " + asso.nom + " est bien enregistrée")
    
def listing():
    """
    Liste les associations déjà enregistrées.
    """
    try:
        fichAssos = open("assos", 'rb')        
        listAssos = pickle.load(fichAssos)        
        fichAssos.close()
        contenu = ""
        for asso in listAssos:
            contenu += asso.nom + ", " + str(asso.nbadh) + " adhérents" + "\n"
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
            for asso in listAssos:
                dic[asso.nom] = asso.nbadh +asso.adh +asso.tres +asso.sal -asso.loc -asso.sub +asso.dem
                total += dic[asso.nom]
            for k in dic:
                pourcent = dic[k]/(total/100)
                assob = sub/100*pourcent
                contenu += k + " " + str(round(pourcent, 2)) + "% = " + str(round(assob, 2)) + "€\n"
            liste.configure(text = contenu)
            confirm.configure(text = "Résultat: ")
        except:
            confirm.configure(text = "Entrez une somme à répartir")
    except:
        confirm.configure(text = "Aucune associations dans le fichier")

fen = Tk()
fen.title("Aide à la répartition des subventions")

Label(fen, text = "Association: ").grid(row = 0, sticky = W)
Label(fen, text = "Nombre d'adhérents: ").grid(row = 1, sticky = W)
Label(fen, text = "Montant de l'adhésion: ").grid(row = 2, sticky = W)
Label(fen, text = "Trésorerie: ").grid(row = 3, sticky = W)
Label(fen, text = "Salarié(es): ").grid(row = 4, sticky = W)
Label(fen, text = "Occupation des salles: ").grid(row = 5, sticky = W)
Label(fen, text = "Subventions extérieures: ").grid(row = 6, sticky = W)
Label(fen, text = "Montant de la demande: ").grid(row = 7, sticky = W)
Label(fen, text = "Montant total à répartir").grid(row = 9, sticky = W)
entr1 = Entry(fen, width=30)
entr2 = Entry(fen, width=30)
entr3 = Entry(fen, width=30)
entr4 = Entry(fen, width=30)
entr5 = Entry(fen, width=30)
entr6 = Entry(fen, width=30)
entr7 = Entry(fen, width=30)
entr8 = Entry(fen, width=30)
entr9 = Entry(fen, width=30)
entr1.grid(row = 0, column = 1)
entr2.grid(row = 1, column = 1)
entr3.grid(row = 2, column = 1)
entr4.grid(row = 3, column = 1)
entr5.grid(row = 4, column = 1)
entr6.grid(row = 5, column = 1)
entr7.grid(row = 6, column = 1)
entr8.grid(row = 7, column = 1)
entr9.grid(row = 9, column = 1)
Button(fen, text = "Enregistrer", command = nouvelle_asso).grid(row = 8, sticky = W)
Button(fen, text = "Nouveau", command = vidage).grid(row = 8, column = 1, sticky = W)
Button(fen, text = "Listing", command = listing).grid(row = 8, column = 2, sticky = W)
Button(fen, text = "Calcul de la répartition", command = coef).grid(row = 10, sticky = W)
confirm = Label(fen)
confirm.grid(row = 11)
liste = Label(fen)
liste.grid(row = 11, column = 1)
Scale(fen, length=250, orient=HORIZONTAL, label="Adhérents", sliderlength=20, showvalue=0,
      from_=-10, to=10, tickinterval=1).grid(row = 12)
Scale(fen, length=250, orient=HORIZONTAL, label="Adhésion", sliderlength=20, showvalue=0,
      from_=-10, to=10, tickinterval=1).grid(row = 12, column = 1)
Scale(fen, length=250, orient=HORIZONTAL, label="Trésorerie", sliderlength=20, showvalue=0,
      from_=-10, to=10, tickinterval=1).grid(row = 12, column = 2)
Scale(fen, length=250, orient=HORIZONTAL, label="Salarié(es)", sliderlength=20, showvalue=0,
      from_=-10, to=10, tickinterval=1).grid(row = 13)
Scale(fen, length=250, orient=HORIZONTAL, label="Occupation de salle", sliderlength=20, showvalue=0, from_=-10, to=10, tickinterval=1).grid(row = 13, column = 1)
Scale(fen, length=250, orient=HORIZONTAL, label="Subventions ext", sliderlength=20, showvalue=0, from_=-10, to=10, tickinterval=1).grid(row = 13, column = 2)

fen.mainloop()

