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

            '''if net_file_sep[0] == "rb125":
                #clu_file = folder + net_file_sep[0] + ".clu"
                clu_file = [folder + "rb125-1.clu", folder + "rb125-2.clu", folder + "rb125-3.clu"]
            elif net_file_sep[0] == "dolphins":
                clu_file = folder + net_file_sep[0] + "-real.clu"
            elif net_file_sep[0] == "football":
                clu_file = folder + net_file_sep[0] + "-conferences.clu"
            elif net_file_sep[0] == "zachary_unwh":
                clu_file = folder + net_file_sep[0] + "-real.clu"
            else:
                clu_file = folder + net_file_sep[0] + ".clu"
                #clu_file = [folder + "rb125-1.clu", folder + "rb125-2.clu", folder + "rb125-3.clu"]'''

            graph = nx.read_pajek(net_file)
            graph = nx.Graph(graph)
            
            al.louvain(graph, net_file_sep[0])
            al.greedy(graph, net_file_sep[0])
            al.walktrap(graph, net_file_sep[0])
                   
    c.compare_partitions()   
    
    
    
    

 