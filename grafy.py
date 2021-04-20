import numpy

def graf(A,B,C):
    
    if B.shape==C.shape and B.shape[0]==len(A) and B.shape[1]==len(A) :

        graf=tuple([A,B,C])

        print("Udało się stworzyć graf!")

        return graf
    else:
        print("Błąd")
        return 0

def skierowany(arg):
    T= numpy.transpose(arg[2]) == arg[2]

    if T.sum() == T.shape[0] * T.shape[0]:
        return 0

    else:
        return 1

def sortujgalezie(graf):
    listakrawedzi = list([])
    for i in range(0,len(graf[0])):
        if skierowany(graf)==1:
            alfa=0
        else:
            alfa=i
        for j in range(alfa,len(graf[0])):
            if graf[1][i][j] == 1:
                h = tuple([graf[2][i][j],graf[0][i],graf[0][j]])
                listakrawedzi.append(h)
            
    return listakrawedzi



if __name__=="__main__":
    A=['A','B','C']
    B=numpy.array([(1,1,1),(1,1,1),(1,1,1)])
    C=numpy.array([(4,7,3),(7,2,9),(3,9,5)])
    

    grafek=graf(A,B,C)

    skierowany(grafek)
    print(sortujgalezie(grafek))

    
    