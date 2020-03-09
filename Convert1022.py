def osBits (n:str, maxbits : int ):
    l=''
    x=1
    n=str(n)
    if maxbits==16 or maxbits==8:
        if len(n)<maxbits:
            while len(n)<maxbits:
                n='0'+n
        elif len(n)>maxbits:
            while len(l)<maxbits:
                l=n[-x]+l
                x=x+1
            n=l
        return n

def addBin(a:int ,b:int ) -> int:   #Ligne 1 : Annonce le nom de la fonction et annonce les variables qu’il faut renter et le type de sortie.
    prec=8                          #Ligne 2 : Donne le nombre de bits maximum.
    a = str(osBits(a,prec))         #Ligne 3 : Passe le premier nombre sur 8 bits et le convertie en string.
    b = str(osBits(b,prec))         #Ligne 4 : Passe le deuxième nombre sur 8 bits et le convertie en string.
    c = ''                          #Ligne 5 : Crée un string vide ou on va ajouter les chiffres 1 à 1.
    rem = 0                         #Ligne 6 : On met rem a 0 qui sera en quelque sorte le compteur a retenue.
    for i in range(7, -1, -1):      #Ligne 7 : Crée une boucle pour parcourir chaque chiffre des nombres.
        S = int(a[i])+int(b[i])+rem #Ligne 8 : Additionne le bit de chaque nombre plus la retenue s’il y en a une.
        if S < 2 :                  #Ligne 9 : Booléen pour se demander si est le résultat de l’addition des 2 bits plus la retenue est plus petit que 2.
            c = str(S) + c          #Ligne 10 : Si le résultat est plus petit que 2 alors on rajoute ce chiffre dans le string c.
            rem = 0                 #Ligne 11 : on met la retenue a 0
        elif S == 2 :               #Ligne 12 : Booléen pour se demander si est le résultat de l’addition des 2 bits plus la retenue est égale à 2.
            c = '0'+ c              #Ligne 13 : Si le résultat est égal à 2 alors on rajoute 0 dans le string c.
            rem = 1                 #Ligne 14 : On met la retenue à 1.
        elif S == 3 :               #Ligne 15 : Booléen pour se demander si est le résultat de l’addition des 2 bits plus la retenue est égale à 3.
            c = '1'+ c              #Ligne 16 : Si le résultat est égal à 3 alors on rajoute 1 dans le string c.
            rem = 1                 #Ligne 17 : On met la retenue à 1.
    return osBits(int(c),prec)      #Ligne 18 : On renvoie le string final c en type string sur 8 bits.

def dec2bin( n: int ) -> str :
    #a = b x q+r
    reste = ''
    a = n
    while a != 0:
        reste = str(a%2) + reste
        a = a // 2
    return reste

def complementa1 (n:int):
    n=str(n)
    j=''
    for g in range (len(n)):
        if n[g]=='1':
            j=j+'0'
        else :
            j=j+'1'
    return j



def dec2signedbin(n:int,bit:int):
    if n>=0:
        n=dec2bin(n)
        n=addBin(n,bit)
        return(n)
    else:
        nabsolu=n-n*2
        nabsolu=osBits(dec2bin(nabsolu),bit)
        nabsolu=complementa1(nabsolu)
        n=addBin(nabsolu,10000000000000001)
        return n


PO=int(input('met ton nombre'))
BIT=int(input('met ton nombre de bit'))
print(dec2signedbin(PO,BIT))

