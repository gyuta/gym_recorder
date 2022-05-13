# gym_recorder

A recorder for open ai gym.

you can easily add a text on the frame like this.

![result](https://github.com/gyuta/gym_recorder/blob/main/media/example.gif?raw=true)


## install
```
pip install gym_record
```
## usage

```python
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
    
```

## tips
this library depends on opencv-python. so you may need some library to use opencv. this is .Dockerfile example to resolve it.
```
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
```

if you use docker, you have to set "SDL_VIDEODRIVER" to "dummy".

add this to your .Dockerfile
```
ENV SDL_VIDEODRIVER=dummy
```
or simply add this to your script.
```
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
```