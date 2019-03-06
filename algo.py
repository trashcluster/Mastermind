solution=[1,2,3,4]
teste=[1,4,2,4]

def mm (solution, teste):
    #print(solution,teste)
    resultat=[0,0,0,0]
    for i in range(len(solution)):
        for j in range(len(teste)):
            #print(resultat)
            if solution[i] == teste[j]:
                resultat[i]='b'
            if solution[i] == teste[i]:
                resultat[i]='r'

    return resultat
print(mm(solution,teste))
