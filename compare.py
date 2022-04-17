import numpy as np
import sklearn.metrics.cluster as skmc
import os
import glob


def read_clu(path):
    file1 = open(path, 'r')
    Lines = file1.readlines()
    lines=[]
    
    for i in range(len(Lines)-1):
        lines.append(int(Lines[i+1].strip()))
    #print(lines)
    
    return lines

def compare_contingency_matrix(list1, list2): 
    return skmc.contingency_matrix(list1, list2)

def compare_partitions():
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
         

            #read .clu files existing
            result1 = read_clu(clu_file) 
            result2_louvain = read_clu("./partitions/louvain/"+clu_file_sep[0]+".clu") #created louvain
            result2_greedy = read_clu("./partitions/greedy/"+clu_file_sep[0]+".clu") #created louvain
            result2_walktrap= read_clu("./partitions/walktrap/"+clu_file_sep[0]+".clu") #created louvain
            
            
            #compare louvain created partitions with existing partitions
            print("Model: Louvain\nCOMPARE "+clu_file_sep[0]+" .CLU FILES EXISTING/CREATED ("+clu_file_sep0[1]+"/"+clu_file_sep[0]+".clu)\nContingency_Matrix")
            print()
            matrixL = compare_contingency_matrix(result1, result2_louvain)
            print(matrixL)
            print()
            #compare greedy created partitions with existing partitions
            print("Model: Greedy\nCOMPARE "+clu_file_sep[0]+" .CLU FILES EXISTING/CREATED ("+clu_file_sep0[1]+"/"+clu_file_sep[0]+".clu)\nContingency_Matrix")
            print()
            matrixG = compare_contingency_matrix(result1, result2_greedy)
            print(matrixG)
            print()
            #compare walktrap created partitions with existing partitions
            print("Model: Walktrap\nCOMPARE "+clu_file_sep[0]+" .CLU FILES EXISTING/CREATED ("+clu_file_sep0[1]+"/"+clu_file_sep[0]+".clu)\nContingency_Matrix")
            print()
            matrixW = compare_contingency_matrix(result1, result2_walktrap)
            print(matrixW)
            
            #save matrix files into csv files
            np.savetxt("./contigency_matrix/"+clu_file_sep[0]+'/louvain_contigency_matrix_'+clu_file_sep0[1]+'.csv', matrixL, delimiter=",")
            np.savetxt("./contigency_matrix/"+clu_file_sep[0]+'/greedy_contigency_matrix_'+clu_file_sep0[1]+'.csv', matrixG, delimiter=",")
            np.savetxt("./contigency_matrix/"+clu_file_sep[0]+'/walktrap_contigency_matrix_'+clu_file_sep0[1]+'.csv', matrixW, delimiter=",")
            
            


