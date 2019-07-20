from math import exp
from functools import reduce
output = [0.4, 2.0, 0.001, 0.32]

# method 1
el = list(map(exp, output))
result = list(map(lambda x: x / sum(el), el))
print("Method 1")
print(result)

# method 2
denominator = reduce(lambda x, y: x + exp(y), output, 0)
result = [exp(x) / denominator for x in output]
print("Method 2")
print(result)
