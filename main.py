import os
import time
import gymnasium as gym
from gymnasium import Env
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from environment import SnakeEnv

# Register the snake Environment
gym.envs.registration.register(id='Snake-v0', entry_point=SnakeEnv)



#### Training


# log_path = r".\logs\saved_models\snakeRL_6_200K_DQN.zip"

# make a snake Environment game
# environment_name = "Snake-v0"
# env = gym.make(environment_name, render_mode="None")


# model = PPO("MlpPolicy", env, verbose=1,  # Reduce random actions
#            learning_rate=0.001) #, tensorboard_log= log_path)

# # train the agent
# model.learn(total_timesteps=10_000)

# # save the trained model
# model.save(r".\logs\saved_models\snakeRL_2_100K_PPO.zip")

# Testing and Evaluation


# make a snake Environment game
environment_name = "Snake-v0"
env = gym.make(environment_name, render_mode="human")

model = PPO.load(r".\logs\saved_models\snakeRL_1_100K_PPO.zip")
episods = 5

for i in range(1, episods+1):
  obs,_= env.reset()
  done = False
  score = 0
  time.sleep(0.6)
  os.system("cls")

  while not done:
    env.render()
    time.sleep(0.1)

    action, _= model.predict(obs)  # were are now using model
    obs, reward, done, info,_= env.step(action)
    score+=reward
  print("Episods: {}, Score: {}".format(episods, score))
env.close()

# mean_reward, std_reward =evaluate_policy(model, env, n_eval_episodes=10)
# print("mean_reward, std_reward: ", mean_reward, std_reward)





