# imports
import numpy as np

# World class
class World:
    def __init__(self, width, length):
        """
        Initializes a new instance of the World class.

        Parameters:
        - width: Width of the space.
        - length: Length of the space.
        """
        self.width = width
        self.length = length
        self.grid = np.zeros((width, length))  # Assuming the grid represents some state information.
        self.pheromones = np.zeros((width, length))  # Initialize pheromones with zeros.

    def diffuse_tensor(self, tensor, diffusion_rate=0.2):
        """
        Diffuses a given tensor in the world.

        Parameters:
        - tensor: The tensor to be diffused.
        - diffusion_rate: Rate at which the tensor diffuses.

        Note: This method assumes periodic boundary conditions.
        """
        for i in range(self.width):
            for j in range(self.length):
                # Implement diffusion with periodic boundary conditions
                left = tensor[(i - 1) % self.width, j]
                right = tensor[(i + 1) % self.width, j]
                up = tensor[i, (j - 1) % self.length]
                down = tensor[i, (j + 1) % self.length]

                self.pheromones[i, j] = (
                    (1 - diffusion_rate) * tensor[i, j]
                    + (diffusion_rate / 4) * (left + right + up + down)
                )

# Agent class
class Agent:
    def __init__(self, world, initial_pos=None, initial_state=None):
        """
        Initializes a new instance of the Agent class.

        Parameters:
        - world: The world in which the agent exists.
        - initial_pos: Initial position of the agent in the world (x, y).
        - initial_state: Initial state of the agent.

        If initial_pos or initial_state is None, they will be randomly selected from available entries.
        """

        if initial_pos is None:
            initial_pos = self.random_empty_position()

        if initial_state is None:
            initial_state = np.random.choice([0, 1])  # Assuming states are 0 or 1

        self.pos = initial_pos
        self.state = initial_state

        # Place the agent in the world
        self.place(world)

    def random_empty_position(self, world):
        """
        Returns a random empty position from the available entries in the world's grid.
        """
        empty_positions = np.argwhere(world.grid == 0)
        if len(empty_positions) == 0:
            raise ValueError("No empty positions available in the world's grid.")
        return tuple(empty_positions[np.random.choice(len(empty_positions))])

    def place(self, world):
        """
        Places the agent in the world, updating the grid accordingly.
        """
        x, y = self.pos
        world.grid[x, y] = -2  # Encode agent position with -2

    def move(self, world, new_pos):
        """
        Moves the agent from the current position to the new position in the grid.

        Parameters:
        - new_pos: New position of the agent in the world (x, y).
        """
        # current pos
        x, y = self.pos
        # Update the grid to remove the agent from the current position
        world.grid[x, y] = 0
        # Update the agent's position
        self.pos = new_pos
        # Place the agent in the new position
        self.place()

    def change_state(self, new_state):
        """
        Changes the state of the agent.

        Parameters:
        - new_state: New state of the agent.
        """
        self.state = new_state