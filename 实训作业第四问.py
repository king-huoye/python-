import numpy as np
import random
a=np.random.random((5,5))
ten_a=10*a
print(ten_a)
mask=(ten_a>5)&(ten_a<8)
print(mask)

"""
a = np.array([[1,2],[3,4],[5,6]])
print("a=")
print(a)
mask = (a > 2)
print("mask=")
print(mask)
"""