"""
Akshay Mohabey
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
import functions as f


# Initialize Model Class
class NetworkModel(mesa.Model):
    def __init__(self,N,P):

        # Initializing Parent Class
        super().__init__()
        self.steppy = 1

        # self.G = nx.generators.random_graphs.erdos_renyi_graph(N,P)

        # Generating Randoom Network
        self.G = nx.erdos_renyi_graph(N,P)

        # Initializing Network Grid
        self.grid = mesa.space.NetworkGrid(self.G)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        # print(nx.number_of_nodes(self.G))
        agent_no = 0

        # Adding agents to the model
        # Change this defination to include enumerate function
        for node in nx.nodes(self.G):
            a = agents.People(agent_no,self)
            self.schedule.add(a)
            self.grid.place_agent(a,node)
            agent_no += 1

        # Adding Connections to the agents
        for node in nx.nodes(self.G):
            a = []
            a.append(node)
            node_agents = self.grid.get_cell_list_contents(a)
            # print(node_agents)
            agent = node_agents[0]
            neighborhood_list = self.grid.get_neighborhood(node)
            neighbors = self.grid.get_cell_list_contents(neighborhood_list)
            agent.set_connections(neighbors)
            # print(agent.return_connections())
            

        # Initiating Data Collector
        self.datacollector = mesa.DataCollector(
            agent_reporters={"State": "state"}
            )
        
        # Drawing the Network Graph
        nx.draw(self.G,
                with_labels = True,
                node_color = "green",
                node_size = 400,
                font_color = "white",
                font_family = "Times New Roman")
        plt.margins(0.2)
        plt.show()

    # Step Function
    def step(self):
        print(self.steppy)
        self.steppy += 1
        self.datacollector.collect(self)
        self.schedule.step()


main_instance = NetworkModel(p.num_of_agents,p.prob)


for i in range(10):
    main_instance.step()