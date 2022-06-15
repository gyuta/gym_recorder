from dataclasses import dataclass
from typing import Tuple

import gym
from .const import BLACK
import cv2

class Recorder(gym.Wrapper):
    """ 
    save simulation as mp4
    write text on a frame
    """

    def __init__(self, env, path = "", videoname = "out", episode_num = 1, codec="vp09", **kwargs):
        """
        episode_num: the number of episode a file contains
        """
        super().__init__(env, **kwargs)
        self.videonumber = 0
        self.env = env
        self.path = path
        self.videoname = videoname
        self.codec = codec

        self.itemqueue =  []
        self.episode_num = episode_num
        self.count_episode = 0
    
    def reset(self, **kwargs):
        obs = super().reset(**kwargs)
        if self.count_episode == 0:
            self.start_recording()
        return obs
    
    def step(self, action):
        self.record_step()
        obs, reward, done, info = self.env.step(action)
        if done:
            self.count_episode += 1
            if self.count_episode == self.episode_num:
                self.stop_recording()
                self.count_episode = 0
        
        return obs, reward, done, info
    
    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc(*self.codec)
        
        video_name =  f"{self.videoname}_{self.videonumber}.mp4"
        if self.path == "":
            path = video_name
        else:
            path = f"{self.path}/{video_name}"
        self.video = cv2.VideoWriter(path, fourcc, 50.0, (600, 400))
    
    def stop_recording(self):
        self.video.release()
        self.videonumber += 1

    def record_step(self):
        frame = self.env.render(mode="rgb_array")
        im = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        txt_pos = 10
        for item in self.itemqueue:
            cv2.putText(im, item.txt, (5, txt_pos), cv2.FONT_HERSHEY_PLAIN, 1, item.color, 1, cv2.LINE_AA)
            txt_pos += 20
        self.itemqueue = []
        self.video.write(im)
    
    def close(self):
        """ if there is a remaining episode, save it
        """

        if self.count_episode != 0:
            self.stop_recording()

Color = Tuple[int, int, int]

@dataclass
class Item:
    txt: str
    color: Color = BLACK
