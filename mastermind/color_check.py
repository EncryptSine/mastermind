def test(main_list, list2):
    '''
    Compare 2 listes pour en déduire le nombre d'éléments au même endroit / mal placé

    PARAMETRES:
    ------------------
    main_list : list
                    liste principale
    list2 : list
                liste secondaire dont les éléments seront comparés avec l'emplacement de ceux ci dans main_list

    SORTIE:
    --------
    same_place_dico : dictionnaire de 4 keys (0, 1, 2, 3) avec pour valeur 0 / 1 / 2
        0 = élément non présent dans la liste principale
        1 = élément bien placé dans la liste principale
        2 = élément présent mais mal placé dans la liste principale    

    PRECONDITION:
    ------------------
    Les listes main_liste et liste2 doivent contenir 4 éléments ni plus ni moins
    
    POSTCONDITION:
    ------------------
    Si 2 mêmes éléments sont présent dans list2 et qu'un seul d'eux est présent dans main_list,
    le second élément sera considéré comme non présent et l'autre comme mal placé et ou au mauvaise endroit
    '''

    #copie de la liste fourni pour ne pas modifier directement celle ci
    code = main_list.copy()

    #initialisation du dictionnaire
    same_place_dico = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
    }

    #boucle for comparant en premier les éléments au même endroit et en les remplaçants par "*" pour la suite
    for i in range(len(code)):
        for j in range(len(list2)):
            if code[i] == list2[j] and i == j:
                same_place_dico[i] = 1
                code[i] = "*"
                list2[j] = "*" 
                break

    #deuxième boucle for comparant les éléments mal placé grâce aux "*" cela permet d'évité des problèmes du à la présence de 2 même couleurs dans liste2
    for i in range(len(code)):
        for j in range(len(list2)):
            if code[i] == list2[j] and i != j:
                if code[i] != "*" and list2[j] != "*":
                    same_place_dico[j] = 2
                    break
    return same_place_dico


#test unitaire vérifiant le bon fonctionnement de la fonction avec des listes fictives
if(__name__ == '__main__'):
    main_list = ["vert", "bleu", "rouge", "jaune"]
    list2 = ["bleu", "bleu", "rouge", 'vert']
    result = test(main_list, list2)
    for key, item in result.items():
        print(key, item)
