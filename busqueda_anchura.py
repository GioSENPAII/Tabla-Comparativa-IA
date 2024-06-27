import networkx as nx

def BFS(G,v0):
    encontrados={v0}
    procesados=set()
    en_proceso=[v0]
    while en_proceso:
        v=en_proceso[0]
        print(v) #Aquí decidimos que hacer al comenzar a procesar un vértice
        for w in G.neighbors(v):
            if (w not in procesados) and (w not in encontrados):
                encontrados.add(w)
                en_proceso.append(w)
        en_proceso.remove(v)
        procesados.add(v)
      
G = nx.Graph()
G.add_edges_from([(0,1), (0,2), (0,3), (1,4), (7,4), (10,2), (2,3), (2,4), (3,4), (6,7), (5,7), (6,8), (8,9), (6,10)])
nx.draw_kamada_kawai(G,with_labels=True, node_color='#22bbbb',node_size=500)

BFS(G,3)
