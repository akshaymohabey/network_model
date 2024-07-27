"""
Akshay Kumar Mohabey
Python 3.12.4 
Mac OSX
19 July 2024

Network Game
Run File
"""
# Importing Dependencies
from mesa.batchrunner import batch_run

# from multiprocessing import freeze_support
import parameters as p
from main import NetworkModel


# Delete this line


# Creating Parameters Dictionary
params = {"N": p.num_of_agents, "P": p.prob}


results = batch_run(
    NetworkModel,
    parameters = params,
    iterations = 10,
    max_steps= 100
)