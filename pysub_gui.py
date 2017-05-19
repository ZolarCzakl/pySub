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
    for asso in liste:
        if asso.nom == nom:
            vrai = 1
            break
        else:
            vrai = 0
    return vrai

def nouvelle_asso():
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
    try:
        fichAssos = open("assos", 'rb')        
        listAssos = pickle.load(fichAssos)        
        fichAssos.close()
        contenu = ""
        for asso in listAssos:
            contenu += asso.nom+", " + str(asso.nbadh) + " adhérents" + "\n"
        liste.configure(text = contenu)
            
        
        
    except:
        liste.configure(text = "Fichier vide")
    
    
def vidage():
    entr1.delete(0, END)
    entr2.delete(0, END)
    entr3.delete(0, END)
    entr4.delete(0, END)
    entr5.delete(0, END)
    entr6.delete(0, END)
    entr7.delete(0, END)
    entr8.delete(0, END)
        

fen = Tk()

Label(fen, text = "Association: ").grid(row = 0, sticky = W)
Label(fen, text = "Nombre d'adhérents: ").grid(row = 1, sticky = W)
Label(fen, text = "Montant de l'adhésion: ").grid(row = 2, sticky = W)
Label(fen, text = "Trésorerie: ").grid(row = 3, sticky = W)
Label(fen, text = "Salarié(es): ").grid(row = 4, sticky = W)
Label(fen, text = "Occupation des salles: ").grid(row = 5, sticky = W)
Label(fen, text = "Subventions extérieures: ").grid(row = 6, sticky = W)
Label(fen, text = "Montant de la demande: ").grid(row = 7, sticky = W)
entr1 = Entry(fen)
entr2 = Entry(fen)
entr3 = Entry(fen)
entr4 = Entry(fen)
entr5 = Entry(fen)
entr6 = Entry(fen)
entr7 = Entry(fen)
entr8 = Entry(fen)
entr1.grid(row = 0, column = 1, columnspan = 2)
entr2.grid(row = 1, column = 1, columnspan = 2)
entr3.grid(row = 2, column = 1, columnspan = 2)
entr4.grid(row = 3, column = 1, columnspan = 2)
entr5.grid(row = 4, column = 1, columnspan = 2)
entr6.grid(row = 5, column = 1, columnspan = 2)
entr7.grid(row = 6, column = 1, columnspan = 2)
entr8.grid(row = 7, column = 1, columnspan = 2)
Button(fen, text = "Enregistrer", command = nouvelle_asso).grid(row = 8, sticky = W)
Button(fen, text = "Nouveau", command = vidage).grid(row = 8, column = 1, sticky = W)
Button(fen, text = "Listing", command = listing).grid(row = 8, column = 2, sticky = W)
confirm = Label(fen)
confirm.grid(row = 9)
liste = Label(fen)
liste.grid(row = 9, column = 1)
fen.mainloop()
