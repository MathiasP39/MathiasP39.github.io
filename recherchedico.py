def rechdicho(L,x):
    tr=False
    deb=0
    fin=len(L)-1
    while tr==False and deb<=fin:
        mil=(deb+fin)%2
        if L[mil]==x:
            tr=True
        else:
            if x>L[mil]:
                deb=mil+1
            else:
                fin=mil-1
    return tr