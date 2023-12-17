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
world = World(width=100, length=100)
agents = [Agent(world) for _ in range(50)]
world.pheromones[[50,20,2], [50,20,2]] = 100  # Set an example pheromone concentration
world.diffuse_pheromones(0.5, 10) # diffuse
world.evaporate_pheromones(0.1, 10) # evaporate

# Visualize the world state
render(world.grid, world.pheromones, show=True, save=True, name="example_image.png")