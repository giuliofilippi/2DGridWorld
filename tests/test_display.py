# sys
import sys
sys.path.append('code')

# base imports
import numpy as np
import pandas as pd
import time

# classes and functions
from classes import World, Agent
from display import render

# Assuming you have a World instance with grid and pheromones attributes
world = World(width=10, length=10)
agent = Agent(world)
world.grid[5, 5] = 1  # Set an example state in the grid
world.pheromones[3, 3] = 10  # Set an example pheromone concentration

# test diffusion
world.diffuse_pheromones(0.5, 10)

# Visualize the world state
render(world.grid, world.pheromones, show=True, save=False, name="example_image.png")