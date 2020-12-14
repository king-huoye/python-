import numpy as np
a=np.random.random((5,5))
ten_a=10*a
mask=(ten_a>5)&(ten_a<8)
new_arr=mask*ten_a
print(new_arr)

