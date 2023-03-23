import random
import neural_network

ACTIVATION_FUNCTIONS = ['identity', 'logistic', 'tanh', 'relu']
SOLVER = ['lbfgs', 'sgd', 'adam']
LEARNING_RATE = ['constant', 'invscaling', 'adaptive']


class Solution:
    def __init__(self, genetic_pool=None):
        if genetic_pool is None:
            self.genetic_pool = {
                'learning_rate_init': random.random(),
                'activation': ACTIVATION_FUNCTIONS[random.randint(0, len(ACTIVATION_FUNCTIONS) - 1)],
                'solver': SOLVER[random.randint(0, len(SOLVER) - 1)],
                'max_iterations': random.randint(650, 1250),
                'random_state': random.randint(0, 100),
                'hidden_layer_sizes': [random.randint(3, 100) for x in range(1, random.randint(2, 15))],
                'alpha': random.random(),
                'batch_size': random.randint(200, 1000),
                'learning_rate': LEARNING_RATE[random.randint(0, len(LEARNING_RATE) - 1)],
                'power_t': random.random(),
                'shuffle': bool(random.randint(0, 1)),
                'momentum': random.random(),
                'nesterovs_momentum': bool(random.randint(0, 1)),
                'beta_1': random.random(),
                'beta_2': random.random(),
                'n_iter_no_change': random.randint(5, 20),
            }
        fitness_score = neural_network.score(** self.genetic_pool)
