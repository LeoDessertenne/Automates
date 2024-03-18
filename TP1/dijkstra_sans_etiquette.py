def dijkstra_sans_etiquette(graphe, s0=1):
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
            if voisin in E: # si le voisin est un sommet dont on  connait  la distance relative
                valeur = table_profondeur[sommet] + 1 # Calcule la nouvelle profondeur
                if valeur < table_profondeur[voisin]: # Si le chemin est plus court, met à jour la profondeur
                    table_profondeur[voisin] = valeur
                    table_peres[voisin] = sommet
    return table_profondeur, table_peres


if __name__ == "__main__":
    graphe = {
        1: [2, 5],
        2: [3],
        3: [4, 6],
        4: [3, 7],
        5: [1, 6],
        6: [3, 5, 7],
        7: [4, 6],
        8: [9],
        9: [8]}
    graphe2 = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 5],
        4: [1, 5],
        5: [3, 4]
    }
    # Affichage des résultats
    table_pere, table_profondeur = dijkstra_sans_etiquette(graphe2)
    print("d: ", table_profondeur)
    print("p: ", table_pere)