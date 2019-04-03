from random import *

#fonction de création de la solution
def fsolution (colonnes, couleurs):
    solution=[]
    for i in range(colonnes):
        solution.append(int(couleurs*random()))
    return solution

#fonction d'entrée des valeurs à tester dans le tableau test
def ftest (colonnes):
    test=[]
    #demande une valeur à l'utilisateur.
    for i in range(colonnes):
        test.append(int(input("Entre la valeur : ")))
    return test

#prend en entrée la solution et la liste à tester et retourne 'r','b','0' dans une liste de même longueur
def mm (solution, test):
    #print(solution,test)
    #initialisation d'un tableau vide
    resultat=[]

    #ajoute les pions rouges au tebleau resultat
    for i in range(len(solution)):
        if solution[i]==test[i]:
            resultat.append('r')
    #ajouyte les pions blanc au tableau résultat
    for i in range(len(solution)-len(resultat)-1):
        for j in range(len(test)):
            if solution[i] == test[j]:
                if solution[i] != test[i]:
                    if len(resultat)<len(solution):
                        resultat.append('b')

#si le tableau de resultat ne fait pas la longueur désiré, complète le tableau avec 'v'
    while len(resultat)<len(solution):
        resultat.append('0')
    return resultat

colonnes = int(input("entre le nombre de colonnes : "))
lignes =int(input("Entre le nombre maximum d'essais : "))
couleurs = int(input("entre le nombre de couleurs : "))

#crée une liste remplie avec 'r' de lal longueur de la solution pour comparer avec la liste en sortie de la fonction de test
mx = ['r' for f in range(colonnes)]

#initie la solution à l'aide de la fonction 'fsolution'
sol=fsolution(colonnes,couleurs)

#debug
#print(sol)

#main
for i in range(lignes):
    #appelle la fonction mm pour tester les entrées de l'utilisateur
    res=(mm(sol,ftest(colonnes)))
    print(res)
    #si res == mx (eg ['r','r','r','r']==['r','r','r','r'])
    if res==mx :
        print("gagné")
    else :
        print("recommence")
