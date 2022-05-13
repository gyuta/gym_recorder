import gym
from gym_recorder import Recorder

src_env = gym.make("CartPole-v1")
env = Recorder(src_env, episode_num=10)

for ep in range(10):
    obs = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        n_obs, reward, done, info = env.step(action)

        env.txtqueue.append(f"episode:{ep}")
        env.txtqueue.append(f"obs:{obs}")
        env.txtqueue.append(f"action:{action}")
        env.txtqueue.append(f"reward:{reward}")
        env.txtqueue.append(f"next obs:{n_obs}")
    