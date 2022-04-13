import networkx as nx  #for optimal modularity algorithms (greedy, louvain)
import networkx.algorithms.community as nx_comm
import igraph as ig    #other algorithms for community detection (walktrap)

import pandas as pd
from matplotlib import pyplot as plt


def louvain():
    
    return 0

def greedy():
    
    return 0

def walktrap(path):
    g = ig.read(path,format="pajek")
    communities = g.community_walktrap(steps = 4)
    return 0
    
    