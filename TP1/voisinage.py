def voisinage(graphe):
    # initialisation
    table_pere = {sommet: None for sommet in graphe}
    table_profondeur = {sommet: -1 for sommet in graphe}
    deja_visite = set()
    # traitement
    for sommet in graphe: # Pour tout sommet dans le graph (pour etre sur de faire toutes les composantes connexes)
        if table_pere[sommet] == None: # si le sommet n'a pas encore été atteint
            table_pere[sommet] = sommet
            table_profondeur[sommet] = 0
            deja_visite.add(sommet)
            while deja_visite != set(): # tant que il n'a pas fini de visiter tout ses voisins
                sommet = deja_visite.pop() # attribuer le premier element de deja_visite puis le supprimer directement
                for voisin in graphe[sommet]: # pour tout les voisins des voisins
                    if table_pere[voisin] == None: # si le sommet n'a pas encore été atteint
                        table_pere[voisin] = table_pere[sommet]
                        table_profondeur[voisin] = table_profondeur[sommet] + 1
                        deja_visite.add(voisin) # ajouter le voisins dans la liste visite (donc a traiter)
    return table_pere, table_profondeur


if __name__ == '__main__':
    # definition du graphee
    graphe = {
        0: [1, 4],
        1: [0, 2, 3, 4],
        2: [1, 3, 8],
        3: [1, 2],
        4: [0, 1],
        5: [6, 7],
        6: [5, 7],
        7: [5, 6],
        8: [2]
    }
    graphe2 = {
        1: [2, 3],
        2: [1],
        3: [1, 4],
        4: [3]
    }
    # Affichage des résultats
    table_pere, table_profondeur = voisinage(graphe2)
    print("d: ", table_profondeur)
    print("p: ", table_pere)
