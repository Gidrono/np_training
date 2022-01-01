import numpy as np
arr1 = np.arange(9).reshape(3,3)
arr2 = np.arange(1,101).reshape(10,10)
arr2/100
np.random.seed(100)
a = np.random.randint(0, 5, 10)
a
np.unique(a, return_index=True)[1]
arr1 = np.arange(6)
arr2 = arr1+10
arr3=arr2+10
arr4=arr3+10
arr5=arr4+10
arr6=arr5+10
mat1 = np.concatenate((arr1, arr2, arr3, arr4, arr5, arr6))
mat2=mat1.reshape(6,6)
mat2
mat1[1::7]
c=mat2[4]
c
c[(c%5==0) | (c%42==0)]
d=mat2[:,2]
d[(d<3)|(d%22==0)|(d%52==0)]
np.random.seed(100)
np.set_printoptions(precision=2)
a = np.random.uniform(1,50, 20)
a
condlist = [a<10, a>30]
choicelist = [10,30]
np.select([a < 10, a > 30],[10,30], a)