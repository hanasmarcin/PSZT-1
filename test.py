import numpy as np
from cec17_functions import cec17_test_func


# x: Solution vector
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# nx: Number of dimensions
nx = 10
# mx: Number of objective functions
mx = 1
# func_num: Function number
func_num = 1
# Pointer for the calculated fitness
f = [0]

print(cec17_test_func)
dir(cec17_test_func)

cec17_test_func(x, f, nx, mx, func_num)

print(f[0])

