import networkx.algorithms.community as nx_comm
import networkx as nx
import os
import glob

def read_clu(path, node_list):
    file1 = open(path, 'r')
    Lines = file1.readlines()
    lines=[]

    for i in range(len(Lines)-1):
        lines.append(int(Lines[i+1].strip()))

    array_line=[[]]
    for i in range(max(lines)):
        list = set()
        count=0
        for line in lines:
            
            if line == i+1:
                list.add(node_list[count])
            count += 1
        
        array_line.insert(i, list)
    del array_line[len(array_line)-1]

    return array_line

def existing_partition():
    folders = ["./A3-networks/model/", "./A3-networks/real/", "./A3-networks/toy/"]
    for folder in folders:
        clu_files = glob.glob(os.path.join(folder, "*.clu"))
        for clu_file in clu_files:
            clu_file_sep0 = clu_file.split("\\")
            clu_file_sep = clu_file_sep0[1].split(".clu")
            if clu_file_sep[0] == 'dolphins-real' or clu_file_sep[0]=='football-conferences' or clu_file_sep[0]=='zachary_unwh-real':
                clu_file_sep = clu_file_sep[0].split("-")
            if clu_file_sep[0] == 'rb125-1' or clu_file_sep[0]=='rb125-2' or clu_file_sep[0]=='rb125-3':
                clu_file_sep = clu_file_sep[0].split("-")
            
            #print(clu_file_sep[0])
            if clu_file_sep[0]!='football':
                path = folder+clu_file_sep[0]+'.net'
                G = nx.read_pajek(path)
                G = nx.Graph(G)
                node_list=[]
                for node in G.nodes:
                    #print(node)
                    node_list.append(node)
                
                result1 = read_clu(clu_file, node_list)
                '''print(type(next(iter(result1[0]))))
                print(len(result1))
                print(result1)'''
                
                modE = nx_comm.modularity(G, result1)
                print(clu_file_sep[0]+" Net Walktrap Modularity: ", modE)
                print()
            
                f= open('.\\modularity\\'+clu_file_sep[0]+'\\created_partition_modularity_'+clu_file_sep[0]+'.txt',"a")
                f.write('Existing File\n')
                f.write(str(modE)+'\n')
                f.close()
        
def created_partition(G,louvain, greedy, walktrap,path):
    modL = nx_comm.modularity(G, louvain)
    print(path+" Net Louvain Modularity: ", modL)
    
    modG = nx_comm.modularity(G, greedy)
    print(path+" Net Greedy Modularity: ", modG)
    
        
    modW = walktrap.modularity
    print(path+" Net Walktrap Modularity: ", modW)
    
    print()
    
    f= open('.\\modularity\\'+path+'\\created_partition_modularity_'+path+'.txt',"w+")
    f.write('Louvain\t\t\t\tGreedy\t\t\t\tWalktrap\n')
    f.write(str(modL)+'\t'+str(modG)+'\t'+str(modW)+'\n')
    f.close()