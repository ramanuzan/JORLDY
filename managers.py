import os
for proxy in ['https_proxy', 'http_proxy']:
    if os.environ.get(proxy): 
        del os.environ[proxy]
import ray
import torch
import numpy as np 
import datetime
import time
import copy
from collections import defaultdict
from functools import reduce

from torch.utils.tensorboard import SummaryWriter

class MetricManager:
    def __init__(self):
        self.metrics = defaultdict(list)
        
    def append(self, result):
        for key, value in result.items():
            self.metrics[key].append(value)
    
    def get_statistics(self, mode='mean'):
        ret = dict()
        if mode == 'mean':
            for key, value in self.metrics.items():
                ret[key] = 0 if len(value) == 0 else round(sum(value)/len(value), 4)
                self.metrics[key].clear()
        return ret
    
class LogManager:
    def __init__(self, env, id):
        self.id=id
        self.now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.path = f"./logs/{env}/{id}/{self.now}/"
        self.writer = SummaryWriter(self.path)
        self.stamp = time.time()
        
    def write_scalar(self, scalar_dict, step):
        for key, value in scalar_dict.items():
            self.writer.add_scalar(f"{self.id}/"+key, value, step)
            self.writer.add_scalar("all/"+key, value, step)
            if "score" in key:
                time_delta = int(time.time() - self.stamp)
                self.writer.add_scalar(f"{self.id}/{key}_per_time", value, time_delta)
                self.writer.add_scalar(f"all/{key}_per_time", value, time_delta)
            
class TestManager:
    def __init__(self):
        pass
    
    def test(self, agent, env, iteration=10):
        if not iteration > 0:
            print("Error!!! test iteration is not > 0")
            return 0
        
        scores = []
        for i in range(iteration):
            done = False
            state = env.reset()
            while not done:
                action = agent.act(state, training=False)
                state, reward, done = env.step(action)
            scores.append(env.score)
            
        return np.mean(scores)

class DistributedManager:
    def __init__(self, Env, env_config, agent, num_worker):
        ray.init()
        agent = copy.deepcopy(agent).cpu()
        Env, env_config, agent = map(ray.put, [Env, env_config, agent])
        self.actors = [Actor.remote(Env, env_config, agent, i) for i in range(num_worker)]

    def run(self, step=1):
        transitions = reduce(lambda x,y: x+y, 
                             ray.get([actor.run.remote(step) for actor in self.actors]))
        return transitions

    def sync(self, agent):
        sync_item = agent.sync_out()
        sync_item = ray.put(sync_item)
        ray.get([actor.sync.remote(sync_item) for actor in self.actors])
    
@ray.remote
class Actor:
    def __init__(self, Env, env_config, agent, id):
        self.env = Env(id=id+1, **env_config)
        self.agent = agent.set_distributed(id)
        self.state = self.env.reset()
    
    def run(self, step):
        transitions = []
        for t in range(step):
            action = self.agent.act(self.state)
            next_state, reward, done = self.env.step(action)
            transitions.append((self.state, action, reward, next_state, done))
            self.state = next_state if not done else self.env.reset()
        return transitions
    
    def sync(self, sync_item):
        self.agent.sync_in(**sync_item)

