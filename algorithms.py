import networkx as nx  #for optimal modularity algorithms (greedy, louvain)
import networkx.algorithms.community as nx_comm
import igraph as ig    #other algorithms for community detection (walktrap)

import pandas as pd
from matplotlib import pyplot as plt


def louvain(G):
    cluste_list = nx_comm.louvain_communities(G, seed=123)
    #print(cluste_list)
    #print(len(cluste_list))

def greedy(G):
    clust_list=nx_comm.greedy_modularity_communities(G, weight='weight')
    print(clust_list)
    print(len(clust_list))
    return 0

def walktrap(G):
    
    g = ig.Graph.TupleList(G.edges(), directed=False)

    wtrap = g.community_walktrap(steps = 4)

    clust = wtrap.as_clustering()
    #print(len(clust))
    #print(clust[0])
    ig.plot(clust, mark_groups = True, bbox=(1600,900), vertex_label=g.vs['name'])
   
    
    