import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def ShowGraph(G, title):
    """plots graph with labals

    Args:
        G (Graph): the graph to be shown
        title (str): The title for the plot.
    """
    #plot the graph
    pos = nx.spring_layout(G)
    print(G,title)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
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
    
    ShowGraph(G, "recreated Graph")
    return G
    
    
def create_subgraph(G, nodes_to_keep):
    """
    Creates a subgraph containing only the specified nodes and calculates the sum of the edge weights in the subgraph.

    Args:
        G (networkx.Graph): The original graph from which to create the subgraph.
        nodes_to_keep (list): A list of nodes to include in the subgraph.

    Returns:
        tuple: A tuple containing the subgraph (networkx.Graph) and the sum of the edge weights (int).
    """
    H = G.subgraph(nodes_to_keep).copy()

    sum = 0
    for i in range(len(nodes_to_keep)):
        try:
            first_node = nodes_to_keep[i]
            second_node = nodes_to_keep[i+1]
            sum += G[first_node][second_node]["weight"]
        except :
            break
    
    return H, sum