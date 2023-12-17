# imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Define a custom colormap for pheromones (gradient of greens)
pheromone_cmap = LinearSegmentedColormap.from_list('pheromone_cmap', ['white', 'green'])
agent_cmap = LinearSegmentedColormap.from_list('pheromone_cmap', ['white', 'blue'])

# render world state with matplotlib
def render(grid_data, pheromone_data, show=True, save=False, name="image.png"):
    """
    Render a world state using matplotlib

    Parameters:
    - grid_data: The world grid
    - pheromone_data: The world pheromone concentrations
    - show: Whether to display the visualization.
    - save: Whether to save the visualization.
    - name: Name of the saved image.
    """
    # Set a black background
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Plot the pheromone concentrations using the custom colormap
    pheromone_im = ax.imshow(pheromone_data, cmap=pheromone_cmap, interpolation='none', alpha=0.5, vmin=0, vmax=1)
    agent_im = ax.imshow(grid_data==-2, cmap=agent_cmap, interpolation='none', alpha=0.5, vmin=0, vmax=1)

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Remove axis spines (borders will stay)
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    if save:
        plt.savefig(name)  # Save

    if show:
        plt.show()
