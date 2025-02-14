import gymnasium as gym
from gymnasium import Env
from gymnasium.spaces import Box, Discrete, Dict, Tuple, MultiBinary, MultiDiscrete
import numpy as np
import pygame


import config
from snake import *
import copy



class SnakeEnv(Env):
    metadata = {"render_modes": ["human"], "render_fps": 10}

    def __init__(self, render_mode = None, show_game_over=False):
        super().__init__()

        # action space left right top bottom
        self.action_space = Discrete(4)

        self.grid_size = 20
        
        # observation space
        self.observation_space = Box(low=0,
                                    high= self.grid_size-1,#np.array([self.grid_size, self.grid_size, self.grid_size, self.grid_size]),
                                    shape=(4,),
                                    dtype=np.int32)

        self.reset()
        self.render_mode = render_mode
        if render_mode == "human":
            pygame.init()
            self.window_size = 450  # Window size
            self.block_size = self.window_size // self.grid_size
            self.screen = pygame.display.set_mode((self.window_size, self.window_size))

    def reset(self, seed = None, options=None):
        super().reset(seed=seed)

       

        self.agent = copy.deepcopy(config.snake)
        self.target = copy.deepcopy(config.target)
        self.direct = copy.deepcopy(config.direct_key)

        self.state = np.concatenate((self.agent[0], self.target))

        return self.state, {}

    def step(self, action):
        
        list_of_directions = list(config.direction.keys())
        if(config.wrong_directions[self.direct] != list_of_directions[action]):
            destination = self.__agent_destination(list_of_directions[action])
        else:
            destination =self.__agent_destination(self.direct)
        
        # Reward Computing
        if destination == self.target:
            reward = 1 # Reached goal
            done = False
        elif game_over(self.grid_size, destination[0], destination[1], self.agent):
            reward = -1 # Fell into pit
            done = True
            self.reset()
        else:
            
            if(compute_distance(self.agent[0], self.target) < compute_distance(destination, self.target)):
                # print("current < target: agent, target, destination ",self.agent[0], self.target, destination)
                reward = -0.01
            else:
                # print("current >= target: agent, target, destination ",self.agent[0], self.target, destination)
                reward = -0.01  # Small penalty for each move
            done = False
        self.agent, self.target= move(self.grid_size, self.agent, destination, self.target)
        self.state = np.concatenate((self.agent[0], self.target))

        return self.state, reward, done, False, {}
       
    def render(self):
        display(self.agent, self.target, self.block_size, self.screen)
        
    
    def __agent_destination(self, direction):
        # computing next position of the agent on the map and calculating destination row and col
        agent_pos = copy.deepcopy(self.agent[0])

        agent_pos[0] = compute_destination(agent_pos[0], 
                                            config.direction[direction][0])
        agent_pos[1] = compute_destination(agent_pos[1], 
                                            config.direction[direction][1])

        self.direct = direction

        return agent_pos






