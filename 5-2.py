from functools import reduce
from math import log2
indexes = [0, 1, 2, 3]
o = [0.001, 0.9, 0.001, 0.098]
label = [0, 0, 0, 1]

# mean square error
mse_result = 0.5 * reduce(lambda x, y: x + (label[y] - o[y]) ** 2, indexes, 0)
print("MSE result")
print(mse_result)

# cross-entropy
cross_entropy = lambda x, y: x + label[y] * log2(o[y]) + (1 - label[y]) * log2(1 - o[y])
cross_entropy_result = -reduce(cross_entropy, indexes, 0)
print("Cross Entropy result")
print(cross_entropy_result)

# log likelihood
log_likelihood_result = -log2(o[label.index(1)])
print("Log Likelihood result")
print(log_likelihood_result)
