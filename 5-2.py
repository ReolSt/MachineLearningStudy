import math
import functools
indexes = [0, 1, 2, 3]
output = [0.001, 0.9, 0.001, 0.098]
label = [0, 0, 0, 1]

# mean square error
mse_result = 0.5 * functools.reduce(lambda x, y: x + (label[y] - output[y]) ** 2, indexes, 0)
print(mse_result)

# cross-entropy
cross_entropy_result = -functools.reduce(lambda x, y: x + label[y] * math.log2(output[y]) + (1 - label[y]) * math.log2(1 - output[y]), indexes, 0)
print(cross_entropy_result)

# log likelihood
log_likelihood_result = -math.log2(output[label.index(1)])
print(log_likelihood_result)
