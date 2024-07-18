"""
Akshay Kumar Mohabey
Python 3.12.4 
Mac OSX
19 July 2024

Network Game
Agents File
"""

# Importing Dependencies

import mesa
import parameters as p
import random


class People(mesa.Agent):
    def __init__(self,unique_ID, model):
        super().__init__(unique_ID,model)
        self.ID = unique_ID
        self.state = random.choice(range(p.num_states))
        print(f'Agent{self.ID} | State {self.state}')

    # @property
    def return_ID(self):
        return self.ID
    
    # @property
    def return_state(self):
        return self.state
    
    def modify_state(self,incoming_state_list):
        pass
    
    def return_incoming_links(self):
        pass

    def step(self):
        pass


    
