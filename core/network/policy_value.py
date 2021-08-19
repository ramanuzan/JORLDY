import torch
import torch.nn.functional as F

from .base import BaseNetwork

class ContinuousPolicyValue(BaseNetwork):
    def __init__(self, D_in, D_out, D_hidden=512, header=None):
        D_in, D_hidden = super(ContinuousPolicyValue, self).__init__(D_in, D_hidden, header)
        
        self.l1 = torch.nn.Linear(D_in, D_hidden)
        self.l2 = torch.nn.Linear(D_hidden, D_hidden)
        self.mu = torch.nn.Linear(D_hidden, D_out)
        self.log_std = torch.nn.Linear(D_hidden, D_out)
        self.v = torch.nn.Linear(D_hidden, 1)
        self.v_i = torch.nn.Linear(D_hidden, 1)

    def forward(self, x):
        x = super(ContinuousPolicyValue, self).forward(x)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        
        mu = torch.clamp(self.mu(x), min=-5., max=5.)
        log_std = torch.tanh(self.log_std(x))
        return mu, log_std.exp(), self.v(x)
    
    def get_vi(self, x):
        x = super(DiscretePolicyValue, self).forward(x)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        return self.v_i(x)
    
    
class DiscretePolicyValue(BaseNetwork):
    def __init__(self, D_in, D_out, D_hidden=512, header=None):
        D_in, D_hidden = super(DiscretePolicyValue, self).__init__(D_in, D_hidden, header)
        
        self.l1 = torch.nn.Linear(D_in, D_hidden)
        self.l2 = torch.nn.Linear(D_hidden, D_hidden)
        self.pi = torch.nn.Linear(D_hidden, D_out)
        self.v = torch.nn.Linear(D_hidden, 1)
        self.v_i = torch.nn.Linear(D_hidden, 1)
        
    def forward(self, x):
        x = super(DiscretePolicyValue, self).forward(x)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        return F.softmax(self.pi(x), dim=-1), self.v(x)

    def get_vi(self, x):
        x = super(DiscretePolicyValue, self).forward(x)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        return self.v_i(x)
    
    