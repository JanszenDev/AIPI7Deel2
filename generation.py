from warnings import catch_warnings, simplefilter
from numpy.random import uniform, randint, choice
from random import randint
from scipy.stats import norm
from sklearn.datasets import load_iris, load_breast_cancer, fetch_olivetti_faces
from sklearn.neural_network import MLPClassifier


# iris = load_iris()
# X = iris.data
# y = iris.target

# breast_cancer = load_breast_cancer()
# X = breast_cancer.data
# y = breast_cancer.target

faces = fetch_olivetti_faces()
X = faces.data
y = faces.target

class Solution:
    def __init__(self, genetic_pool=None, fitness=True):
        self.genetic_pool = genetic_pool
        if genetic_pool is None:
            self.genetic_pool = {
                'learning_rate_init': uniform(low=0.001, high=0.1),
                'activation': choice(['identity', 'logistic', 'tanh', 'relu']),
                'solver': choice(['lbfgs', 'sgd', 'adam']),
                'learning_rate': choice(['constant', 'invscaling', 'adaptive']),
                'max_iter': randint(200, 650),
                'random_state': randint(0, 100),
                'hidden_layer_sizes': [int(x) for x in norm.rvs(loc=15, scale=10, size=randint(2, 5))],
                'alpha': uniform(low=0.0001, high=0.01),
                'batch_size': randint(200, 1000),
                'power_t': uniform(low=0.1, high=0.9),
                'shuffle': bool(randint(0, 1)),
                'momentum': uniform(low=0.1, high=0.9),
                'nesterovs_momentum': bool(randint(0, 2)),
                'beta_1': uniform(low=0.1, high=0.9),
                'beta_2': uniform(low=0.1, high=0.9),
                'n_iter_no_change': randint(5, 20)
            }
        if fitness:
            self.fitness_score = self.fitness_scoring()

    def fitness_scoring(self):
        with catch_warnings():
            simplefilter("ignore")
            try:
                neural_network = MLPClassifier(**self.genetic_pool)
                neural_network.fit(X, y)
                return neural_network.score(X, y)
            except (Exception, Warning):
                return 0.

    def create_model(self):
        return MLPClassifier(**self.genetic_pool)


