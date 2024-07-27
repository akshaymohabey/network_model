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

# Graphing Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Creating Parameters Dictionary
# params = {"N": p.num_of_agents, "P": p.prob}
params = {"N": p.num_of_agents, "P": p.prob}

results_4s = batch_run(
    NetworkModel,
    parameters = params,
    iterations = 1,
    max_steps= 50,
    number_processes=1,
    data_collection_period=1,
    display_progress=True
)

results_4s_df = pd.DataFrame(results_4s)
# print(results_4s_df.keys())

results_4s_df.to_csv('export/data.csv', index=False)



# Seaborn Graph
# Create the line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=results_4s_df, 
             x='Step', 
             y='Most Common State', 
             hue='N', 
            #  marker='o',
             errorbar=("ci",78),
             palette="tab10")

# Add labels and title
plt.xlabel('Step')
plt.ylabel('Ratio')
plt.title('Most Common State vs Step for Multiple Runs')
plt.legend(title='N', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(False)

# Show the plot
plt.tight_layout()
plt.show()
