"""
Akshay Kumar Mohabey
Python 3.12.4 
Mac OSX
19 July 2024

Network Game
Model File
"""

# Import Dependencies
import mesa
import networkx as nx
import random
import parameters as p
import copy
import matplotlib.pyplot as plt
import agents

# Initialize Model Class
class NetworkModel(mesa.Model):
    def __init__(self,N,P):

        super().__init__()

        # self.G = nx.generators.random_graphs.erdos_renyi_graph(N,P)

        self.G = nx.erdos_renyi_graph(N,P)

        self.grid = mesa.space.NetworkGrid(self.G)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        print(nx.number_of_nodes(self.G))
        agent_no = 0

        # Adding agents to the model
        # Change this defination to include enumerate function
        for node in nx.nodes(self.G):
            a = agents.People(agent_no,self)
            self.schedule.add(a)
            self.grid.place_agent(a,node)
            agent_no = agent_no + 1
        
        self.datacollector = mesa.DataCollector(agent_reporters={"State": "state"})
        
        nx.draw(self.G,
                with_labels = True,
                node_color = "green",
                node_size = 400,
                font_color = "white",
                font_family = "Times New Roman")
        plt.margins(0.2)
        plt.show()

    # def record

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
            

        

main_instance = NetworkModel(p.num_of_agents,p.prob)

