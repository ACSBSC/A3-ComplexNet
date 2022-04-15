
def save_file(list, filename):
    
    f= open('.\\partitions\\'+filename+'.clu',"w+")
    f.write("*Vertices "+str(len(list))+ '\n')
    for cluster_id in list:
        f.write(str(cluster_id) + '\n')
    f.close()
