import numpy as np
import networkx as nx  #for optimal modularity algorithms (greedy, louvain)
import networkx.algorithms.community as nx_comm
import igraph as ig    #other algorithms for community detection (walktrap)

import pandas as pd
from matplotlib import pyplot as plt

import save_partition as sp
import ploting as p

def return_list_cluster(list, G):
    nodes = dict(G.nodes())
    list_nodes = [key for key in nodes]
    size = len(G.nodes())
    list_of_cluster = np.zeros((size,), dtype=int)
    
    for i in range(len(list)):
        for j in list[i]:
            index = list_nodes.index(j)
            list_of_cluster[index]=i+1
            
    return list_of_cluster


def louvain(G, path):
    cluste_list = nx_comm.louvain_communities(G, seed=123)
    id_cluster_list = return_list_cluster(cluste_list, G)
    #print(cluste_list)
    sp.save_file(id_cluster_list, 'louvain\\'+path)
    p.plot(cluste_list, G, path, "louvain")
    return id_cluster_list

def greedy(G, path):
    clust_list=nx_comm.greedy_modularity_communities(G, weight='weight')
    id_cluster_list = return_list_cluster(clust_list, G)
    sp.save_file(id_cluster_list, 'greedy\\'+path)
    p.plot(clust_list, G, path, "greedy")
    return id_cluster_list

def walktrap(G, path):
    
    g = ig.Graph.TupleList(G.edges(), directed=False)

    wtrap = g.community_walktrap(steps = 4)

    clust = wtrap.as_clustering()
    
    id_cluster_list = clust.membership
    id_cluster_list = list(np.asarray(id_cluster_list) + 1)
    
    sp.save_file(id_cluster_list, 'walktrap\\'+path)
    out = ig.plot(clust, mark_groups = True, bbox=(1600,900))#, vertex_label=g.vs['name'])
    out.save("./plots/"+path+'/walktrap_plot.png')
    return id_cluster_list
    
    
   
    
    