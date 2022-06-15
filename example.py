import gym
from gym_recorder import Recorder, Item
import gym_recorder

src_env = gym.make("CartPole-v1")
src_env = gym.make("LunarLander-v2")
env = Recorder(src_env, episode_num=10)

for ep in range(10):
    obs = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        n_obs, reward, done, info = env.step(action)

        env.itemqueue.append(Item(f"episode:{ep}", color = gym_recorder.WHITE))
        env.itemqueue.append(Item(f"obs:{obs}", color = gym_recorder.WHITE))
        env.itemqueue.append(Item(f"action:{action}", color = gym_recorder.WHITE))
        env.itemqueue.append(Item(f"reward:{reward}", color = gym_recorder.WHITE))
        env.itemqueue.append(Item(f"next obs:{n_obs}", color = gym_recorder.WHITE))
    