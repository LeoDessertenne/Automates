
def sous_profondeur(graphe, pere, table_pere, table_profondeur, profondeur):
    for voisin in graphe[pere]: # pour chaque voisin du pere
        if table_pere[voisin] == None: # si le sommet n'a pas encore été atteint
            table_pere[voisin] = pere
            table_profondeur[voisin] = table_profondeur[voisin] + 1
            sous_profondeur(graphe, voisin, table_pere, table_profondeur, profondeur + 1) # refaire l'opération pour tout ses voisins
    # composante connexe de sommet est traité
def profondeur(graphe):
    # initialisation
    table_pere = {sommet: None for sommet in graphe}
    table_profondeur = {sommet: -1 for sommet in graphe}
    # traitement
    for sommet in graphe: # Pour tout sommet dans le graph (pour etre sur de faire toutes les composantes connexes)
        if table_pere[sommet] == None: # Si le sommet n'a pas encore été atteint
            table_pere[sommet] = sommet
            table_profondeur[sommet] = 0
            sous_profondeur(graphe, sommet, table_pere, table_profondeur, 0) # regarder les voisins du sommet
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
    table_pere, table_profondeur = profondeur(graphe)
    print("d: ", table_profondeur)
    print("p: ",  table_pere)