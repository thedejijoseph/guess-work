# to test my theory of a model learning the algorithm
# behind python's pseudo-random module "random",
# ill use a known formula, train the model to predict
# going forward and to determine the cause of value
# looking backwards.


# algo: y = (2 * x) - 1
# model.predict(3) = 8
# model.determine(8) = 3
func_y = lambda x: (2 * x) - 1

X = range(1200)
y = [func_y(i) for i in X]

import sklearn
import numpy as np

from sklearn import utils

dataset = utils.Bunch()
dataset.data = np.array(X).reshape(-1, 1)
dataset.target = np.array(y).reshape(-1, 1)

from sklearn import linear_model
model = linear_model.LinearRegression()

model.fit(dataset.data, dataset.target)

test_X = np.array([i for i in range(3, 1200)]).reshape(-1, 1)
test_y = np.array([func_y(i) for i in test_X]).reshape(-1, 1)
pred_y = model.predict(test_X)

from sklearn import metrics
scorer = metrics.explained_variance_score
scorer(test_y, pred_y)
# outputs 1.0