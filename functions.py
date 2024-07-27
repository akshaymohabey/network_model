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

# Generating a random graph
"""
G = nx.generators.random_graphs.erdos_renyi_graph(p.num_of_agents,p.prob)
nx.draw(G)
plt.show()
"""

from collections import Counter

def most_common_list(states_list):
    if not states_list:
        return []
    
    count = Counter(states_list)
    max_count = max(count.values())
    most_common = [num for num, freq in count.items() if freq == max_count]
    
    return most_common