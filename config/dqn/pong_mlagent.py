# ### DDQN Pong_ML-Agents Config ###

# env = {
#     "name": "pong_mlagent",
#     "train_mode": True
# }

# agent = {
#     "name": "dqn",
#     "network": "dueling",
#     "optimizer": "adam",
#     "learning_rate": 0.00025,
#     "gamma": 0.99,
#     "epsilon_init": 1.0,
#     "epsilon_min": 0.1,
#     "explore_step": 450000,
#     "buffer_size": 50000,
#     "batch_size": 64,
#     "start_train_step": 25000,
#     "target_update_term": 1000,
# }

# train = {
#     "training" : True,
#     "load_path" : None,
#     "train_step" : 500000,
#     "test_step" : 50000,
#     "print_term" : 10,
#     "save_term" : 500,
#     "id": "ddqn"
#     "test_iteration": 10,
# }

### DQN Pong_ML-Agents Config ###

env = {
    "name": "pong_mlagent",
    "train_mode": True
}

agent = {
    "name": "dqn",
    "network": "dqn",
    "optimizer": "adam",
    "learning_rate": 0.00025,
    "gamma": 0.99,
    "epsilon_init": 1.0,
    "epsilon_min": 0.1,
    "explore_step": 450000,
    "buffer_size": 50000,
    "batch_size": 32,
    "start_train_step": 25000,
    "target_update_term": 1000,
}

train = {
    "training" : True,
    "load_path" : None,
    "run_step" : 500000,
    "print_term" : 1000,
    "save_term" : 10000,
    "test_iteration": 5,
    "update_term" : 1,
    "num_worker" : 16,
}