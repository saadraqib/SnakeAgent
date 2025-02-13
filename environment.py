import gymnasium as gym
from gymnasium import Env
from gymnasium.spaces import Box, Discrete, Dict, Tuple, MultiBinary, MultiDiscrete
import numpy as np



import config
from snake import *
import copy



class SnakeEnv(Env):
    def __init__(self):
        super().__init__()

        # action space left right top bottom
        self.action_space = Discrete(4)

        self.grid_size = 15
        
        # observation space
        self.observation_space = Box(low=1,
                                    high= self.grid_size,#np.array([self.grid_size, self.grid_size, self.grid_size, self.grid_size]),
                                    shape=(4,),
                                    dtype=np.int32)

        self.reset()

    def reset(self, seed = None, options=None):
        super().reset(seed=seed)

        self.board = board(self.grid_size, self.grid_size)

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
            reward = 5 # Reached goal
            done = False
        elif game_over(self.board, destination[0], destination[1]):
            reward = -10 # Fell into pit
            done = True
            self.reset()
        else:
            
            if(compute_distance(self.agent[0], self.target)< compute_distance(destination, self.target)):
                # print("current < target: agent, target, destination ",self.agent[0], self.target, destination)
                reward = -1
            else:
                # print("current >= target: agent, target, destination ",self.agent[0], self.target, destination)
                reward = 1  # Small penalty for each move
            done = False
        self.board, self.agent, self.target= move(self.board, self.agent, destination, self.target)
        self.state = np.concatenate((self.agent[0], self.target))

        return self.state, reward, done, False, {}
       
    def render(self):
        show(self.board, self.agent)
        
    
    def __agent_destination(self, direction):
        # computing next position of the agent on the map and calculating destination row and col
        agent_pos = self.agent[0]

        agent_pos[0] = compute_destination(agent_pos[0], 
                                            config.direction[direction][0])
        agent_pos[1] = compute_destination(agent_pos[1], 
                                            config.direction[direction][1])

        self.direct = direction

        return agent_pos






