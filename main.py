import networkx as nx  #for optimal modularity algorithms (greedy, louvain)
import networkx.algorithms.community as nx_comm
import igraph as ig    #other algorithms for community detection (edge_betweeness)
import sklearn as sk
import pandas as pd
from matplotlib import pyplot as plt 

import algorithms as al

network_airport = './A3-networks/model/rb125.net'
graph = nx.read_pajek(network_airport)
graph = nx.Graph(graph)
al.walktrap(graph)
