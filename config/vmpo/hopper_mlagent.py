### PPO Hopper Config ###

env = {
    "name": "hopper_mlagent",
    "train_mode": True
}

agent = {
    "name": "vmpo",
    "network": "continuous_pi_v",
    "optimizer": "adam",
    "learning_rate": 5e-4,
    "gamma": 0.99,
    "batch_size":64,
    "n_step": 200,
    "n_epoch": 1,
    "_lambda": 0.95,
    
    "min_eta": 1e-8,
    "min_alpha_mu": 1e-8,
    "min_alpha_sigma": 1e-8,
    
#     "eps_eta": 0.01,
#     "eps_alpha_mu": 0.05,
#     "eps_alpha_sigma": 5*1e-5,
    "eps_eta": 0.01,
    "eps_alpha_mu": 0.01,
    "eps_alpha_sigma": 5*1e-5,
    
    "eta": 1.0,
    "alpha_mu": 1.0,
    "alpha_sigma": 1.0,
}

train = {
    "training" : True,
    "load_path" : None,
    "run_step" : 200000,
    "print_period" : 1000,
    "save_period" : 10000,
    "test_iteration": 10,
    # distributed setting
    "update_period" : agent["n_step"],
    "num_worker" : 8,
}
