
def largeur(graphe):
    # initialisation
    table_pere = {sommet: None for sommet in graphe}
    table_profondeur = {sommet: -1 for sommet in graphe}
    file = [0] * len(graphe)
    debut = 0
    fin = 0
    # traitement
    for sommet in graphe: # Pour tout sommet dans le graph (pour etre sur de faire toutes les composantes connexes)
        if table_pere[sommet] == None: # si le sommet n'a pas encore été atteint
            table_pere[sommet] = sommet
            table_profondeur[sommet] = 0
            file[fin] = sommet # Ajoute le sommet à la file
            fin += 1
            while debut < fin:  # Tant que la file n'est pas vide donc qu'il y a encore des voisins a traiter
                sommet_pere = file[debut] # Sélectionne le premier sommet dans la file
                for voisin in graphe[sommet_pere]: # Pour chaque voisin du sommet sélectionné
                    if table_pere[voisin] == None: # Si le voisin n'a pas encore été atteint
                        table_pere[voisin] = sommet_pere
                        table_profondeur[voisin] = table_profondeur[sommet_pere] + 1
                        file[fin] = voisin  # Ajoute le voisin à la file de sommet a traiter
                        fin += 1
                    debut += 1 # Passe au sommet suivant dans la file
    return table_pere, table_profondeur

if __name__ == '__main__':
    # definition du graphe
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
    table_pere, table_profondeur = largeur(graphe2)
    print("d: ", table_profondeur)
    print("p: ",  table_pere)