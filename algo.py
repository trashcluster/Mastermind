from random import *

#fonction de création de la solution, crée une liste de 'colonnes' longueur avec des chiffres allant de 1 à 'couleurs'
def fsolution (colonnes, couleurs):
    solution=[]
    for i in range(colonnes):
        solution.append(int(couleurs*random()))
    return solution

#fonction d'entrée des valeurs à tester dans le tableau test
def ftest (colonnes):
    #initialise un tableau de test vide
    test=[]
    #demande une valeur à l'utilisateur. Répète l'action 'colonnes' fois.
    i=int(0)
    while i < colonnes:
        x = int(input("couleurs : 1à9, effacer : 0 : "))
        #colorange définit l'étendue des couleurs possibles
        colorange=range(1,colonnes+1)
        #si la valeur entrée par l'utilisateur est une couleur contenu dans la liste de couleurs disponible elle sera prise en compte et ajouté au tableau...
        if x in colorange:
            test.append(x)
            i+=1
        # ...sinon elle retourne une erreur indiquant que la couleur choisis n'est pas possible...
        elif x !=0 :
            print("Couleur choisi : ", x, "Couleurs possibles : ", colorange)
            # ...sinon si x = 0 et le tableau contient au moins une couleur la dernière valeur ajouté au tableau est supprimé
        elif x == 0 and len(test)>0:
            test.pop()
            i-=1
        print(test)
    return test

#prend en entrée la solution et la liste à tester et retourne 'r','b','0' dans une liste de même longueur
def mm (solution, test):
    #DEBUG print(solution,test)
    #initialisation d'un tableau vide
    resultat=[]

    #ajoute les pions rouges au tebleau resultat
    for i in range(len(solution)):
        if solution[i]==test[i]:
            resultat.append('r')
    #ajoute les pions blanc au tableau 'résultat', les tests sons là pour empêcher le tableau 'resultat' de dépasser la taille désiré (un bug faisait que si une couleur se trouvait à plusieurs reprises dans la solution mais que cette couleur n'etait pas en première position et que si le test contenait 2 fois ou plus cette couleur le tableau 'solution' dépassait la taille demandé)
    for i in range(len(solution)-len(resultat)-1):
        for j in range(len(test)):
            if solution[i] == test[j]:
                if solution[i] != test[i]:
                    if len(resultat)<len(solution):
                        resultat.append('b')

#si le tableau de resultat ne fait pas la longueur désiré, complète le tableau avec '0'
    while len(resultat)<len(solution):
        resultat.append('0')
    return resultat

#colonnes : tailles de la solution
colonnes = 0
while colonnes not in range(1,10):
    colonnes = int(input("entre le nombre de colonnes (9 max) : "))
#lignes : nombre maximum d'essais
lignes =int(input("Entre le nombre maximum d'essais : "))
#couleurs : nombre de couleures différentes pouvant être utilisé
couleurs = int(input("entre le nombre de couleurs : "))

#crée une liste remplie avec 'r' de lal longueur de la solution pour comparer avec la liste en sortie de la fonction de test
mx = ['r' for f in range(colonnes)]

#initie la solution à l'aide de la fonction 'fsolution'
sol=fsolution(colonnes,couleurs)

#DEBUG print(sol)

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
