import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix
import generation

data_iris = load_iris()

iris = pd.DataFrame(
    data=np.c_[data_iris['data'], data_iris['target']],
    columns=data_iris['feature_names'] + ['target']
)
# print(iris.head(1000))
#
# print(data_iris.get("target_names"))

train, test = train_test_split(iris, random_state=1)

X_train = train[train.columns[1:4]]
y_train = train["target"]
X_test = test[test.columns[1:4]]
y_test = test["target"]

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform((X_train))
X_test = scaler.transform((X_test))

test = generation.Solution()
MLP = MLPClassifier(hidden_layer_sizes=(test.genetic_pool.get('hidden_layer_sizes')), max_iter=test.genetic_pool.get('max_iterations'))

MLP.fit(X_train, y_train.values.ravel())

predictions = MLP.predict(X_test)


def score(parameters):
    MLP = MLPClassifier(parameters)
    MLP.fit(X_train, y_train.values.ravel())
    return classification_report(y_test, MLP.predict(X_test))


print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
print(['identity', 'logistic', 'tanh', 'relu'][0])
