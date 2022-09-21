# Importation des modules nécessaires
from random import *


def create_graph_non_oriente(n_sommet, n_arrete):
    dic = {}
    cmpt = 0
    for i in range (0, n_sommet):
        dic [i] = []

    while cmpt < n_arrete:
        sommet_source = randint(0, n_sommet-1)
        sommet_cible = randint(0, n_sommet-1)
        if (sommet_cible not in dic[sommet_source]) and sommet_source not in dic[sommet_cible]:
            dic[sommet_source].append(sommet_cible)
            dic[sommet_cible].append(sommet_source)
            cmpt += 1
        print(cmpt*100/n_arrete)
    return dic




def dominating_set(graph):
    res = []
    visited = []
    while len(graph) != len(visited):
        sommet = randint(0, len(graph)-1)
        if (sommet not in visited) and (sommet not in res):
            print("On choisi un sommet au hasard qui est : ", sommet," et qui n'est pas dans la liste des points visiter ni dans la liste des points du domninating set")
            res.append(sommet)
            print("On ajoute le sommet à la liste du dominating set")
            visited.append(sommet)
            print("On ajoute le sommet à la liste des valeurs deja vérifier")
            for valeur in graph[sommet]:
                if valeur not in visited:
                    print("On ajoute le point ",valeur," lier au sommet ",sommet)
                    visited.append(valeur)
    return res




def is_dominating_set(graph, set):
    for node in graph:

        if node not in set:
            flag = False 
            for neighbor in graph[node]: 
                if neighbor in set:
                    flag = True

                    break
            if not flag:

                return False

    return True



graphe = create_graph_non_oriente(1000, 15000)
#print(graphe)

#dicto = {0:[1], 1:[2,3], 2:[1,3,6,7],3:[1,2,4], 4:[3,5], 5:[4], 6:[2], 7:[2]}

res = dominating_set(graphe)
print("LA solution final du dominating set pour le graphe est : ",res)
print("IL Y A ",100*len(res)/len(graphe), "% DES POINTS DU GRAPHE QUI SONT DANS LA SOLUTION")
print("VERIFICATION DU DOMINATING SET = ",is_dominating_set(graphe, res), "[!] Renvoie 'True' si c'est bien un dominating set SINON renvoie 'False'")

