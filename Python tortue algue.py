from turtle import*
def transfo(listcarac:str)->str:
    gr=''
    for j in range (len(listcarac)):
        t=listcarac[j]
        if t=='A':
            gr=gr+'AB'
        elif t=='B':
            gr=gr+'A'
    return gr#transformation chaine
f="A"
pos=[]
angr=[]
posbase=[]
angrb=[]
pro=0
g=0
max2=[]
ang2=[]
anginf=[]
n=int(input('entre le nombre de generation'))
for z in range (n):
    f=transfo(f)
for tz in range(len(f)):
    print(f[tz])
for tri in range (len(f)):#premiere generation
    zre=f[tri]
    if zre=='A':
        fd(25)
        if pro<2:
         posbase.append(position())
         angrb.append(heading())
         pro=pro+1
    elif zre=='B':
        pos.append(position())
        angr.append(heading())
        rt(30)
        fd(25)
        max2.append(position())
        ang2.append(heading())
        up()
        goto(pos.pop(-1))
        lt(360-angr.pop(-1))
        pos.append(position())
        angr.append(heading())
        lt(60)
        down()
        fd(25)
        max2.append(position())
        ang2.append(heading())
        goto(pos.pop(-1))
        rt(60)
trwq=len(max2)
for fre in range(trwq-1):
    up()
    goto(max2.pop(-1))
    lt(ang2.pop(-1))
    down()
    for tri in range (len(f)):
        zre=f[tri]
        if zre=='A':
            fd(5)
        elif zre=='B':
            pos.append(position())
            angr.append(heading())
            rt(25)
            fd(5)
            up()
            goto(pos.pop(-1))
            lt(360-angr.pop(-1))
            pos.append(position())
            angr.append(heading())
            lt(60)
            down()
            fd(5)
            goto(pos.pop(-1))
            rt(60)
    anginf.append(heading())
up()
goto(posbase.pop(-1))
for tri in range (len(f)):
    zre=f[tri]
    if zre=='A':
        fd(5)
    elif zre=='B':
        pos.append(position())
        angr.append(heading())
        rt(30)
        fd(5)
        max2.append(position())
        ang2.append(heading())
        up()
        goto(pos.pop(-1))
        lt(360-angr.pop(-1))
        pos.append(position())
        angr.append(heading())
        lt(60)
        down()
        fd(5)
        max2.append(position())
        ang2.append(heading())
        goto(pos.pop(-1))
        rt(60)



