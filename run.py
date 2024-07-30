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
from mpl_toolkits.mplot3d import Axes3D

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

""" 2D Graph """
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
plt.title('Most Common State/Total States vs Step for Multiple Runs')
plt.legend(title='N', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(False)

# Show the plot
plt.tight_layout()
# Showing Graph
# plt.show()
# Exporting graphs to file
plt.savefig("graphs/ER_2D_Plot_No_1.png")


""" 3D Plot """

# Creating a 3D Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting data
sc = ax.scatter(results_4s_df['Step'],
                results_4s_df['N'], 
                results_4s_df['Most Common State'], 
                c=results_4s_df['N'],
                cmap='viridis',
                # marker='o'
            )

# Add labels and title
ax.set_xlabel('Step')
ax.set_ylabel('Number of Agents (N)')
ax.set_zlabel('Most Common State/Total States')
ax.set_title('3D Plot:Most Common State/Total States vs Step and Number of Agents')

# Add color bar
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Number of Agents (N)')

# Show plot
# plt.show()

# Save Plot
plt.savefig("graphs/ER_3D_Plot_No_1.png")


""" 
Creating a 3D line plot 
"""
# Line Plot

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Get unique values of N
unique_n_values = results_4s_df['N'].unique()

# Plot data
for n in unique_n_values:
    subset = results_4s_df[results_4s_df['N'] == n]
    ax.plot(subset['Step'], 
            subset['N'], 
            subset['Most Common State'], 
            # marker='o', 
            label=f'N={n}')

# Add labels and title
ax.set_xlabel('Step')
ax.set_ylabel('Number of Agents (N)')
ax.set_zlabel('Most Common State/Total')
ax.set_title('3D Line Plot: Most Common State/Total States vs Step and Number of Agents')

# Add legend
ax.legend(title='Number of Agents')

# Show plot
# plt.show()
plt.savefig("graphs/ER_3D_Plot_No_2.png")