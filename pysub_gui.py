"""
Aide au calcul de la répartition des subventions de la mairie
 pour les associations.

@auteur: Rod <rod.cat@free.fr>  License libre
"""

from tkinter import *
from tkinter.ttk import *
import pickle


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
        if nom in listAssos:
            confirm.set("L'association " + nom + " est déjà enregistrée")       
        else:
            listAssos[nom] = [nbadh, adh, tres, sal, loc, sub, dem]
            fichAssos = open("assos", 'wb')
            pickle.dump(listAssos, fichAssos)
            fichAssos.close()
            confirm.set("L'association " + nom + " est bien enregistrée")       
    except:
        listAssos = {}
        fichAssos = open("assos", 'wb')
        listAssos[nom] = [nbadh, adh, tres, sal, loc, sub, dem]
        pickle.dump(listAssos, fichAssos)
        fichAssos.close()
        confirm.set("L'association " + nom + " est bien enregistrée")
        
def listing():
    """
    liste les associations déjà enregistrées.
    """
    try:
        fichAssos = open("assos", 'rb')        
        listAssos = pickle.load(fichAssos)        
        fichAssos.close()
        cont = ""
        for asso in listAssos:            
            cont += asso + ", " + str(listAssos[asso][0]) + " adhérents" + "\n" 
        liste.set(cont)                
    except:
        liste.set("Fichier vide")
    
    
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
        cont = ""        
        try:
            sub = float(entr9.get())            
            for asso, val in listAssos.items():                
                dic[asso] = (val[0]*adherent.get()
                + val[1]*adhesion.get()
                + val[2]*tresorerie.get()
                + val[3]*salarie.get()
                - val[4]*salle.get()
                -val[5]*subvention.get()
                + val[6])                
                total += dic[asso]                
            for k in dic:                
                pourcent = dic[k]/(total/100)                
                assob = sub/100*pourcent                
                cont += (k+" "+str(round(pourcent, 2))+"% = "
                +str(round(assob, 2))+"€\n")                
            liste.set(cont)            
            confirm.set("Résultat: ")            
        except:
            confirm.set("Entrez une somme à répartir")
    except:
        confirm.set("Aucune associations dans le fichier")

def scale_val():
    val_adherents.set("Adhérents:     " + str(round(adherent.get(),2)))
    val_adhesion.set("Adhésion:      " + str(round(adhesion.get(),2)))
    val_tresorerie.set("Trésorerie:         " + str(round(tresorerie.get(),2)))
    val_salarie.set("Salarié(es):     " + str(round(salarie.get(),2)))
    val_salle.set("Usage salle:    " + str(round(salle.get(),2)))
    val_subvention.set("Subvention ext:   " + str(round(subvention.get(),2)))

def scale_update(event):
    scale_val()


root = Tk()
root.title("Aide à la répartition des subventions")


fen = Frame(root, padding=10)
fen.grid(column=0, row=0, sticky=(E,W))
message = Frame(root, padding=10, borderwidth=2, relief="sunken", height=400)
message.grid(column=0, row=12, sticky=(E,W))
scale = Frame(root, padding=10)
scale.grid(column=0, row=20, rowspan=3)


confirm = StringVar()
liste = StringVar()


Label(fen, text="Association: ").grid(row=0, sticky=W)
Label(fen, text="Nombre d'adhérents: ").grid(row=1, sticky=W)
Label(fen, text="Montant de l'adhésion: ").grid(row=2, sticky=W)
Label(fen, text="Trésorerie: ").grid(row=3, sticky=W)
Label(fen, text="Salarié(es): ").grid(row=4, sticky=W)
Label(fen, text="Occupation des salles: ").grid(row=5, sticky=W)
Label(fen, text="Subventions extérieures: ").grid(row=6, sticky=W)
Label(fen, text="Montant de la demande: ").grid(row=7, sticky=W)
Label(fen, text="Montant total à répartir").grid(row=9, sticky=W)
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
Button(fen, text="Enregistrer", command=nouvelle_asso).grid(row=8, sticky=W)
Button(fen, text="Nouveau", command=vidage, width=25).grid(row=8, column=1, padx=5)
Button(fen, text="Listing", command=listing).grid(row=8, column=2, sticky=E)
Button(fen, text="Calcul", command=coef).grid(row=10, sticky=W)
Label(message, textvariable=confirm).grid(column=0, row=11, sticky=W)
Label(message, textvariable=liste).grid(column=1, row=11, sticky=W)

adherent = Scale(scale, length=250, orient=HORIZONTAL, from_=-10, to=10)
adhesion = Scale(scale, length=250, orient=HORIZONTAL, from_=-10, to=10)
tresorerie = Scale(scale, length=250, orient=HORIZONTAL, from_=-10, to=10)
salarie = Scale(scale, length=250, orient=HORIZONTAL, from_=-10, to=10)
salle = Scale(scale, length=250, orient=HORIZONTAL, from_=-10, to=10)
subvention = Scale(scale, length=250, orient=HORIZONTAL, from_=-10, to=10)
adherent.grid(row=16)
adhesion.grid(row=16, column=1)
tresorerie.grid(row=16, column=2)
salarie.grid(row=18)
salle.grid(row=18, column=1)
subvention.grid(row=18, column=2)

val_adherents = DoubleVar()
val_adhesion = DoubleVar()
val_tresorerie = DoubleVar()
val_salarie = DoubleVar()
val_salle = DoubleVar()
val_subvention = DoubleVar()

Label(scale, textvariable=val_adherents).grid(row=15, sticky=W)
Label(scale, textvariable=val_adhesion).grid(row=15, column=1, sticky=W)
Label(scale, textvariable=val_tresorerie).grid(row=15, column=2, sticky=W)
Label(scale, textvariable=val_salarie).grid(row=17, sticky=W)
Label(scale, textvariable=val_salle).grid(row=17, column=1, sticky=W)
Label(scale, textvariable=val_subvention).grid(row=17, column=2, sticky=W)

root.bind('<B1-Motion>', scale_update)
scale_val()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
fen.columnconfigure(0, weight=1)
fen.columnconfigure(1, weight=1)
fen.columnconfigure(2, weight=1)
fen.rowconfigure(0, weight=1)
# message.columnconfigure(0, weight=1)
# message.rowconfigure(0, weight=1)
# scale.columnconfigure(0, weight=1)
# scale.rowconfigure(0, weight=1)

entr1.focus()

root.mainloop()

