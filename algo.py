from random import *

#fonction de création de la solution
def fsolution (colonnes, couleurs):
    solution=[]
    for i in range(colonnes):
        solution.append(int(couleurs-1*random()+1))
    return solution

#fonction d'entrée des valeurs à tester dans le tableau test
def ftest (colonnes):
    test=[]
    for i in range(colonnes):
        test.append(int(input("Entre la valeur",i)))
    return test


def mm (solution, test):
    #print(solution,test)
#initialisation d'un tableau vide
    resultat=[]
#ajoute les pions rouges au tebleau resultat
    for i in range(len(solution)):
        if solution[i]==test[i]:
            resultat.append('r')
#ajouyte les pions blanc au tableau résultat
    for i in range(len(solution)):
        for j in range(len(test)):
            if solution[i] == test[j] and solution[i] != test[i]:
                resultat.append('b')
#si le tableau de resultat ne fait pas la longueur désiré, complète le tableau avec 'v'
    while len(resultat)<len(solution):
        resultat.append('v')
    return resultat

colonnes = int(input("entre le nombre de colonnes : "))
lignes =int(input("Entre le nombre maximum d'essais : "))
couleurs = int(input("entre le nombre de couleurs : "))
print(mm(fsolution(colonnes,couleurs),ftest(colonnes)))
