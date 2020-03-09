def definit ():
    L1=['','','']
    L2=['','','']
    L3=['','','']
    Ltot=[L1,L2,L3]
    return Ltot
def affichage(t):
    for i in range (len(t)):
        print(t[i])
def demande (player):
    case=input('Sur quel case veut tu jouer ?( ligne et colonne separe par des virgule)')
    case=case.split(',',2)
    return case
def addSymbol (joueur,tot,case):
    if joueur==1:
        tot[int(case[0])-1][int(case[1])-1]='X'
    elif joueur==2:
        tot[int(case[0])-1][int(case[1])-1]='O'
    return tot
def lejeu ():
    t=definit()
    joueur=1
    a=True
    while a==True:
        c=demande(joueur)
        t=addSymbol(joueur,t,c)
        affichage (t)
        a=gagne(t)
        if joueur==1:
            joueur=2
        else:
            joueur=1
def gagne (t):
    def colonne (t,nbcolonne):
        l=[]
        l.append(t[0][int(nbcolonne)])
        l.append(t[1][int(nbcolonne)])
        l.append(t[2][int(nbcolonne)])
        return l
    def diagonale (t):
        diag1=[]
        diag2=[]
        for i in range (3):
            diag1.append(t[i][i])
            diag2.append(t[i][2-i])
        return (diag1,diag2)
    for i in range (len(t)):
        if t[i].count("X")==3:
            print('Joueur 1 a gagne')
            return False
        if t[i].count("O")==3:
            print('Joueur 2 a gagne')
            return False
     #colonne
    for i in range (3):
        if colonne(t,i).count('X')==3:
            print('Joueur 1 a gagne')
            return False
        if colonne(t,i).count("O")==3:
            print('Joueur 2 a gagne')
            return False
    diag1,diag2=diagonale(t)
    if diag1.count("X")==3:
        print('Joueur 1 a gagne')
        return False
    if diag1.count("O")==3:
        print('Joueur 2 a gagne')
        return False
    if diag2.count("X")==3:
        print('Joueur 1 a gagne')
        return False
    if diag2.count("O")==3:
        print('Joueur 2 a gagne')
        return False
    return True
lejeu()



