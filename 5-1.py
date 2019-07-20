import math
import functools
output = [0.4, 2.0, 0.001, 0.32]

# method 1
el = list(map(math.exp, output))
result = list(map(lambda x: x / sum(el), el))
print(result)

# method 2
denominator = functools.reduce(lambda x, y: x + math.exp(y), output, 0)
result = [math.exp(x) / denominator for x in output]
print(result)
