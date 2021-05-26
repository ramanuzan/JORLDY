### Rainbow IQN CratPole Config ###

env = {
    "name":"cartpole",
    "mode":"discrete",
    "render":False,
}

agent = {
    "name": "rainbow_iqn",
    "network": "rainbow_iqn",
    "optimizer": "adam",
    "learning_rate": 0.0000625,
    "gamma": 0.99,
    "explore_step": 20000,
    "buffer_size": 50000,
    "batch_size": 64,
    "start_train_step": 2000,
    "target_update_period": 1000,
    
    # MultiStep
    "n_step": 3,
    # PER
    "alpha": 0.6,
    "beta": 0.4,
    "learn_period": 4,
    "uniform_sample_prob": 1e-3,
    # IQN
    "num_sample": 64,
    "embedding_dim": 64,
    "sample_min": 0.0,
    "sample_max": 1.0,
}

train = {
    "training" : True,
    "load_path" : None,
    "train_step" : 80000,
    "test_step" : 30000,
    "print_period" : 20,
    "save_period" : 1000,
    "test_iteration": 10,
}
