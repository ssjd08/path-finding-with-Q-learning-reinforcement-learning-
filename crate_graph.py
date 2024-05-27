import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def ShowGraph(G):
    """plots graph with labals

    Args:
        G (Graph): the graph to be shown
    """
    #plot the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    
def crate_graph(file_path):
    """recreate graph from excel file
    
    Args:
        file_path (string): the path of the exel file
    """
    # file_path = "graph_data_with_weights.xlsx"
    edges_df = pd.read_excel(file_path)
    print(edges_df.head())
    #create graph
    G = nx.Graph()

    #add edges to graph acording to dataframe
    for _, row in edges_df.iterrows():
        G.add_edge(row["Source"], row["Destination"], weight=row["weight"])
    
    ShowGraph(G)
    return G
    
