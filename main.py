import os
import time
import gymnasium as gym
from gymnasium import Env
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from environment import SnakeEnv

# Register the snake Environment
gym.envs.registration.register(id='Snake-v0', entry_point=SnakeEnv)

# make a snake Environment game
environment_name = "Snake-v0"
env = gym.make(environment_name)


#### Training


log_path = r".\reinforcement-learning\logs"



model = DQN("MlpPolicy", env, verbose=1,exploration_fraction=0.1,  # Reduce random actions
            exploration_final_eps=0.05, learning_rate=0.001, tensorboard_log= log_path)

# train the agent
model.learn(total_timesteps=20_000)

# save the trained model
model.save(r".\logs\saved_models\snakeRL_0_20K_DQN.zip")

# Testing and Evaluation

# model = DQN.load(r".\logs\saved_models\snakeRL_6_200K_DQN.zip")
# episods = 5

# for i in range(1, episods+1):
#   obs,_= env.reset()
#   done = False
#   score = 0

#   while not done:
#     env.render()
#     time.sleep(0.3)
#     os.system("cls")

#     action, _= model.predict(obs)  # were are now using model
#     obs, reward, done, info,_= env.step(action)
#     score+=reward
#   print("Episods: {}, Score: {}".format(episods, score))
# env.close()

# mean_reward, std_reward =evaluate_policy(model, env, n_eval_episodes=10)
# print("mean_reward, std_reward: ", mean_reward, std_reward)







