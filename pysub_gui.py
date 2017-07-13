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
    nom = (entrees[0][1].get()).lower()
    nbadh = int(entrees[1][1].get())
    adh = float(entrees[2][1].get())
    tres = float(entrees[3][1].get())
    sal = int(entrees[4][1].get())
    loc = int(entrees[5][1].get())
    sub = float(entrees[6][1].get())
    dem = float(entrees[7][1].get())
    
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
        
        fen = Toplevel(root)
        fen.title("Liste")
        colonne = ["Assos", "Adhérents", "Adhésion", "Trésorerie",
                   "Salarié(es)", "Salles", "Sub ext", "Demande"]
        num_col = 0
        while num_col < len(colonne):
            Label(fen, text=colonne[num_col], width=10).grid(row=0,
                                                             column=num_col)
            num_col += 1
        num_row = 1
        for asso in listAssos:
            num_col = 0
            Label(fen, text=asso).grid(row=num_row, column=num_col, sticky=W)
            for e in listAssos[asso]:
                num_col += 1
                Label(fen, text=str(e)).grid(row=num_row, column=num_col,
                                             sticky=W)
            num_row += 1
        
    except:
        confirm.set("Fichier vide")
    
    
def vidage():
    """
    Vide les champs du formulaire.
    """
    for ent in entrees:
        ent[1].delete(0, END)
        
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
            sub = float(entrees[8][1].get())            
            fen = Toplevel(root)
            fen.title("Répartition")
            colonne = ["Assos", "Pourcentage", "Montant"]
            num_col = 0
            while num_col < len(colonne):
                Label(fen, text=colonne[num_col], width=12).grid(row=0,
                                                                 column=num_col)
                num_col += 1
                
            for asso, val in listAssos.items():                
                dic[asso] = (val[0]*adherent.get()
                + val[1]*adhesion.get()
                + val[2]*tresorerie.get()
                + val[3]*salarie.get()
                - val[4]*salle.get()
                -val[5]*subvention.get()
                + val[6])                
                total += dic[asso]
            num_row = 1
            num_col = 0
            for k in dic:                
                pourcent = dic[k]/(total/100)                
                assob = sub/100*pourcent
                num_col = 0
                Label(fen, text=k).grid(row=num_row, column=num_col, sticky=W)
                Label(fen, text=str(round(pourcent,2))+"%  ").grid(row=num_row,
                                                             column=num_col+1,
                                                             sticky=E)
                Label(fen, text=str(round(assob,2))+"€  ").grid(row=num_row,
                                                          column=num_col+2,
                                                          sticky=E)
                num_row += 1
                #cont += (k+" "+str(round(pourcent, 2))+"% = "
                #+str(round(assob, 2))+"€\n")                
            #liste.set(cont)            
            #confirm.set("Résultat: ")            
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
root.resizable(0,0)


fen = Frame(root, padding=10)
fen.grid(column=0, row=0, sticky=(E,W))
message = Frame(root, padding=10, borderwidth=2, relief="sunken", height=400)
message.grid(column=0, row=12, sticky=(E,W))
scale = Labelframe(root, text="Réglage cœfficients", padding=10)
scale.grid(column=0, row=20, rowspan=3)


confirm = StringVar()
liste = StringVar()
nom_label = ["Association: ", "Nombre d'adhérents: ", "montant de l'adhésion: ",
             "Trésorerie: ", "Salarié(es): ", "Occupation des salles: ",
             "Subvention extérieures: ", "Montant de la demande: ",
             "Montant total à répartir: "]
num_row = 0
entrees = []
for nom in nom_label:
    if num_row == 8:
        num_row = 9
    Label(fen, text=nom).grid(row=num_row, sticky=W)
    ent = Entry(fen, width=30)
    ent.grid(row=num_row, column=1)
    entrees.append((nom, ent))
    num_row += 1

Button(fen, text="Enregistrer", command=nouvelle_asso).grid(row=8, sticky=W)
Button(fen, text="Nouveau", command=vidage, width=25).grid(row=8, column=1)
Button(fen, text="Listing", command=listing).grid(row=8, column=2, sticky=E)
Button(fen, text="Calcul", command=coef).grid(row=10, sticky=W)
Label(message, textvariable=confirm).grid(column=0, row=11, sticky=W)
Label(message, textvariable=liste).grid(column=3, row=11, sticky=E)

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

fen.columnconfigure(0, weight=1)
fen.columnconfigure(1, weight=1)
fen.columnconfigure(2, weight=1)

entrees[0][1].focus()

root.mainloop()

