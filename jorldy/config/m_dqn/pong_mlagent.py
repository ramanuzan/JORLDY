### Munchausen DQN Pong_ML-Agents Config ###

env = {"name": "pong_mlagent", "time_scale": 12.0}

agent = {
    "name": "m_dqn",
    "network": "discrete_q_network",
    "gamma": 0.99,
    "epsilon_init": 1.0,
    "epsilon_min": 0.1,
    "explore_ratio": 0.1,
    "buffer_size": 50000,
    "batch_size": 32,
    "start_train_step": 25000,
    "target_update_period": 1000,
    # M-DQN Parameters
    "alpha": 0.9,
    "tau": 0.03,
    "l_0": -1,
}

optim = {
    "name": "adam",
    "lr": 2.5e-4,
}

train = {
    "training": True,
    "load_path": None,
    "run_step": 200000,
    "print_period": 5000,
    "save_period": 50000,
    "eval_iteration": 10,
    # distributed setting
    "update_period": 8,
    "num_workers": 16,
}
