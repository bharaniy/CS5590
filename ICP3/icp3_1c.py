import numpy as np
a=np.random.randint(20, size=15)
print(a)
b=a.reshape((3,5))
print(b)
matrix=np.array(b)
c=np.where(b==np.max(b,axis=1).reshape(-1,1),0*b,b)
print(c)