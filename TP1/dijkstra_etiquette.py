def dijkstra_etiquette(graphe, s0=1):
    # Initialisation
    table_profondeur = {}
    table_peres = {}
    E = {s0}  # Ensemble des sommets dont on connait la distance relative
    for sommet in graphe:
        table_profondeur[sommet] = float("inf") # valeur infini pour tous les sommets inconnus
        table_peres[sommet] = None
        E.add(sommet)

    table_profondeur[s0] = 0
    table_peres[s0] = s0
    while E != set():
        sommet = min(E, key=table_profondeur.get)  # Prendre le sommet de E avec la plus petite valeur de table_profondeur
        E.remove(sommet)
        # définir d pour des voinsins de "sommet"
        for voisin in graphe[sommet]:
            sommet_voisin = voisin[0]
            poids_voisin = voisin[1]
            if sommet_voisin in E: # si le voisin est un sommet dont on  connait  la distance relative
                valeur = table_profondeur[sommet] + poids_voisin # Calcule la nouvelle profondeur
                if valeur < table_profondeur[sommet_voisin]: # Si le chemin est plus court, met à jour la profondeur
                    table_profondeur[sommet_voisin] = valeur
                    table_peres[sommet_voisin] = sommet
    return table_profondeur, table_peres


if __name__ == "__main__":
    graphe = {
        1: [(2, 7), (5, 6), (6, 2)],
        2: [(3, 4), (5, 5), (1, 7)],
        3: [(4, 1), (5, 2), (2, 4)],
        4: [(3, 1), (5, 3)],
        5: [(1, 6), (2, 5), (3, 2), (4, 3), (6, 1)],
        6: [(1, 2), (5, 1)]
    }

    graphe2 = {
        1: [(2, 10), (3, 2), (5, 6), (6, 2)],
        2:[(3, 4), (5, 0), (1, 10)],
        3:[(2, 4), (1, 2), (5, 2), (4, 1)],
        4:[(3, 1), (5, 0)],
        5: [(4, 0), (3, 2), (2, 0), (1, 6), (6, 1)],
        6: [(1, 2), (5, 1)]
    }
    # Affichage des résultats
    table_pere, table_profondeur = dijkstra_etiquette(graphe2)
    print("d: ", table_profondeur)
    print("p: ", table_pere)