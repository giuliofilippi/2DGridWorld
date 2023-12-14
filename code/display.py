# imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Define a custom colormap for pheromones (gradient of greens)
pheromone_cmap = LinearSegmentedColormap.from_list('pheromone_cmap', ['white', 'green'])

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
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Plot the pheromone concentrations using the custom colormap
    pheromone_im = ax.imshow(pheromone_data, cmap=pheromone_cmap, interpolation='none', alpha=0.8, vmin=0, vmax=1)

    # Overlay agents on top of pheromones (agents are lighter blue)
    x, y = np.where(grid_data == -2)  # Assuming -2 represents agent positions
    ax.plot(y, x, 's', color='blue', markersize=5) 

    # Create a colorbar for pheromones
    cbar = plt.colorbar(pheromone_im)
    cbar.set_label('Pheromone Concentration', color='white')  # Set colorbar label color to white
    cbar.ax.yaxis.label.set_color('white')  # Set colorbar axis label color to white
    cbar.outline.set_edgecolor('white')  # Set colorbar outline color to white
    cbar.dividers.set_color('white')  # Set colorbar dividers color to white
    cbar.dividers.set_linewidth(1)  # Set colorbar dividers linewidth

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Remove axis spines (borders will stay)
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    if show:
        plt.show()

    if save:
        plt.savefig(name, facecolor=fig.get_facecolor(), edgecolor='none')  # Save with black background
