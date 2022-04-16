import os
import glob
import sklearn as sk
import pandas as pd
from matplotlib import pyplot as plt

import networkx as nx  # for optimal modularity algorithms (greedy, louvain)
import networkx.algorithms.community as nx_comm
import igraph as ig    # other algorithms for community detection (edge_betweeness)

import algorithms as al


if __name__ == '__main__':
    folders = ["./A3-networks/model/", "./A3-networks/real/", "./A3-networks/toy/"]

    for folder in folders:
        net_files = glob.glob(os.path.join(folder, "*.net"))
        for net_file in net_files:
            net_file_sep = net_file.split("\\")
            net_file_sep = net_file_sep[1].split(".net")

            if net_file_sep[0] != "rb125":
                clu_file = folder + net_file_sep[0] + ".clu"
            else:
                clu_file = [folder + "rb125-1.clu", folder + "rb125-2.clu", folder + "rb125-3.clu"]

            graph = nx.read_pajek(net_file)
            graph = nx.Graph(graph)

            #print(net_file_sep[0])
            
            community_list_louvain=al.louvain(graph, net_file_sep[0])
            community_list_greedy=al.greedy(graph, net_file_sep[0])
            #community_list_walktrap=al.walktrap(graph, net_file_sep[0])

    
    '''network_airport = './A3-networks/real/airports_UW.net'
    graph = nx.read_pajek(network_airport)
    graph = nx.Graph(graph)
    
    al.louvain(graph, "airports_UW")
    #al.greedy(graph, "airports_UW")
    # al.walktrap(graph)'''
 