def count_common_elements(main_list, list2):
    print(main_list, "salut", list2)
    code = main_list.copy()
    """
    out : dico avec 1 si element sont les mêmes et 0 si différents pour emplacement respectifs
    """
    same_place_dico = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
    }

    #FINIR FONCTION POUR PION NOIR = BIEN PLACE / PION BLANC = MAL PLACE / RIEN = MAUVAISE COULEUR
    #bug si 2 couleurs présentent dans la liste principale

    for i in range(len(code)):
        for j in range(len(list2)):
            if code[i] == list2[j] and i == j:
                same_place_dico[i] = 1
                code[i] = "*"
                list2[j] = "*" 
                break
    print(code, list2)

    for i in range(len(code)):
        for j in range(len(list2)):
            if code[i] == list2[j] and i != j:
                if code[i] != "*" and list2[j] != "*":
                    same_place_dico[j] = 2
                    break
    print(same_place_dico)
    return same_place_dico


if(__name__ == '__main__'):
    main_list = ["vert", "bleu", "rouge", "jaune"]
    list2 = ["bleu", "bleu", "rouge", 'jaune']
    result = count_common_elements(main_list, list2)
    for key, item in result.items():
        print(key, item)

