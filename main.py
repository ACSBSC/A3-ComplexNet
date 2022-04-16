import os
import glob

import networkx as nx  

import algorithms as al
import compare as c


if __name__ == '__main__':
    folders = ["./A3-networks/model/", "./A3-networks/real/", "./A3-networks/toy/"]

    for folder in folders:
        net_files = glob.glob(os.path.join(folder, "*.net"))
        #clu_files = glob.glob(os.path.join(folder, "*.clu"))
        for net_file in net_files:
            net_file_sep = net_file.split("\\")
            net_file_sep = net_file_sep[1].split(".net")

            graph = nx.read_pajek(net_file)
            graph = nx.Graph(graph)
            
            '''al.louvain(graph, net_file_sep[0])
            al.greedy(graph, net_file_sep[0])
            al.walktrap(graph, net_file_sep[0])'''
    
    network_airport = './A3-networks/real/airports_UW.net'
    graph = nx.read_pajek(network_airport)
    graph = nx.Graph(graph)
    al.louvain(graph, "airports_UW") 
    al.greedy(graph, "airports_UW")
    al.walktrap(graph, "airports_UW")            
    #c.compare_partitions()   
    
    
    
    
   
    
    
    
    

 