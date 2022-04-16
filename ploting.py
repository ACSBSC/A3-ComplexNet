import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import networkx as nx

# installation easiest via pip:
# pip install netgraph
#from netgraph import Graph

def plot(cluster_nodes, G, path, algorithm):  
    G = nx.Graph(G)
    
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    colors = list(colors)
   
    pos = nx.spring_layout(G) #calculate position for each node
    # pos is needed because we are going to draw a few nodes at a time,
    # pos fixes their positions.

    # Notice that the pos dict is passed to each call to draw below

    # Draw the graph, but don't color the nodes
    plt.figure(3,figsize=(12,10)) 
    nx.draw(G, pos, edge_color='k',  #with_labels=True,
            font_weight='light', node_size= 280, width= 0.9)
    
    for i in range(len(cluster_nodes)):
         nx.draw_networkx_nodes(G, pos, nodelist=cluster_nodes[i], node_color=colors[i*5])


    plt.savefig("./plots/"+path+'/'+algorithm+'_plot.png')
    plt.show()
    
