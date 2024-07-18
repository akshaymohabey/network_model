"""
Akshay Kumar Mohabey
Python 3.12.4 
Mac OSX
19 July 2024

Network Game -- Marketing, Supply Chain
Agents File
"""
# Import Dependencies
import matplotlib.pyplot as plt
import networkx as nx
import parameters as p


G = nx.generators.random_graphs.erdos_renyi_graph(p.num_of_agents,p.prob)

nx.draw(G)
plt.show()