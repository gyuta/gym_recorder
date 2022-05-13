import gym
from gym_recorder import Record

env = Record(gym.make("CartPole-v0"))

env.reset()
done = False
while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    