import os
import glob

import networkx as nx  

import algorithms as al
import compare as c
import modularity_graph as mod


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
            
            partitionL=al.louvain(graph, net_file_sep[0])
            partitionG=al.greedy(graph, net_file_sep[0])
            partitionW=al.walktrap(graph, net_file_sep[0])
            
            mod.created_partition(graph,partitionL,partitionG,partitionW,net_file_sep[0])
    
    '''network_airport = './A3-networks/real/football.net'
    graph = nx.read_pajek(network_airport)
    graph = nx.Graph(graph)
    partitionL=al.louvain(graph, "football") 
    partitionG=al.greedy(graph, "football")
    partitionW=al.walktrap(graph, "football")
    mod.created_partition(graph,partitionL,partitionG,partitionW,"football")'''
               
    #c.compare_partitions() #this script did not work it only gets the contigency matrix and we run out of time to do this part, intesd we used radatools
    mod.existing_partition()   
    
    
    
    
   
    
    
    
    

 