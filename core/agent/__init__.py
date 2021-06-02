from .dqn import DQNAgent
from .sac import SACAgent
from .double import DoubleDQNAgent
from .per import PERAgent
from .noisy import NoisyAgent
from .c51 import C51Agent
from .rainbow import RainbowAgent
from .rainbow_iqn import RainbowIQNAgent
from .qrdqn import QRDQNAgent
from .iqn import IQNAgent 
from .icm_dqn import ICMDQNAgent
from .icm_ppo import ICMPPOAgent
from .reinforce import REINFORCEAgent
from .ppo import PPOAgent
from .multistep import MultistepDQNAgent

import sys, os

sys.path.append(os.path.abspath('../../'))


class Agent:
    dictionary = {
    "dqn": DQNAgent,
    "sac": SACAgent,
    "double": DoubleDQNAgent,
    "dueling": DQNAgent,
    "multistep": MultistepDQNAgent,
    "per": PERAgent,
    "noisy": NoisyAgent,
    "c51": C51Agent,
    "rainbow": RainbowAgent,
    "rainbow_iqn": RainbowIQNAgent,
    "qrdqn": QRDQNAgent,
    "iqn": IQNAgent,
    "icm_dqn": ICMDQNAgent,
    "icm_ppo": ICMPPOAgent,
    "reinforce": REINFORCEAgent,
    "ppo": PPOAgent,
    }
    
    def __new__(self, name, *args, **kwargs):
        expected_type = str
        if type(name) != expected_type:
            print("### name variable must be string! ###")
            raise Exception
        name = name.lower()
        if not name in self.dictionary.keys():
            print(f"### can use only follows {[opt for opt in self.dictionary.keys()]}")
            raise Exception
        return self.dictionary[name](*args, **kwargs)


'''
class BaseAgent:
    def __init__(self):
        pass

    def act(self, state):
        return action

    def learn(self):
        return result
    
    def process(self, transitions):
        result = None
        # Process per step
        
        # Process per epi
        if done :
            pass
        return result

    def save(self, path):
        pass

    def load(self, path):
        pass
'''