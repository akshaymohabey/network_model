"""
Akshay Kumar Mohabey
Python 3.12.4 
Mac OSX
19 July 2024

Network Game
Batch Run File
"""
# Importing Dependencies
from mesa.batchrunner import batch_run
import pandas as pd
# from multiprocessing import freeze_support
import parameters as p
from main import NetworkModel
import seaborn as sns

# Creating Parameters Dictionary
# params = {"N": p.num_of_agents, "P": p.prob}
params = {"N": p.num_of_agents, "P": p.prob}

results_4s = batch_run(
    NetworkModel,
    parameters = params,
    iterations = 1,
    max_steps= 5,
    number_processes=1,
    data_collection_period=1,
    display_progress=True
)

results_4s_df = pd.DataFrame(results_4s)
# print(results_5s_df)

results_4s_df.to_csv('export/data.csv', index=False)
