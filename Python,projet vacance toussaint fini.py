from turtle import*
def transfo (base:str)->str:
    g=''
    suite='f+f-f-f+f'
    for a in range (len(base)):
        if base[a]=='f':
            g=g+suite
        else:
            g=g+base[a]
    return g
laliste=['f']
speed(5)
up()
backward(300)
down()
n=int(input('rentre le nombre de génération que tu veux'))
for t in range (n):
    laliste=[transfo(laliste[0])]
for lecture in range (len(laliste)):
    t=laliste[lecture]
    for i in range (len(t)):
        if t[i]=="f":
            fd(25)
        elif t[i]=='+':
            lt(90)
        elif t[i]=='-':
            rt(90)

