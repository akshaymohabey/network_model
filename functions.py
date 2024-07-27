"""
Akshay Mohabey
Python 3.12.4 
Mac OSX
19 July 2024

Network Game -- Marketing, Supply Chain
Functions File
"""
# Import Dependencies
import matplotlib.pyplot as plt
import networkx as nx
import parameters as p
import agents

from collections import Counter
from itertools import combinations, groupby
import random 

# Generating a random graph
"""
G = nx.generators.random_graphs.erdos_renyi_graph(p.num_of_agents,p.prob)
nx.draw(G)
plt.show()
"""

def most_common_list(states_list):
    if not states_list:
        return []
    
    count = Counter(states_list)
    max_count = max(count.values())
    most_common = [num for num, freq in count.items() if freq == max_count]
    return most_common

"""
Generates a random undirected graph, similarly to an Erdős-Rényi 
graph, but enforcing that the resulting graph is conneted
"""
def gnp_random_connected_graph(n, p):
   
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G