# 1
import numpy as np
print(np.__version__) 
print(np.show_config())
###
# 2
print(np.info(np.add))
###
# 3
tab1 = np.zeros((1,4))
tab2 = np.ones((1,4))
print(np.all(tab1))
print(np.all(tab2))
###
# 4
tab3 = np.array([1,0,0,0])
print(np.any(tab3))
print(np.any(tab1))
###
# 5
tab_nan_inf = np.array([1,0,np.nan,np.inf])
print(np.isfinite(tab_nan_inf))
###
# 6
print(np.isinf(tab_nan_inf))
###
# 7
print(np.isnan(tab_nan_inf))
###
# 8
tab_crs = np.array([1+1j,1+0j,4.5,3,2,2j])
print(np.iscomplex(tab_crs))
print(np.isreal(tab_crs))
print(np.isscalar(3.1))
print(np.isscalar([3.1]))
###
# 9
print(np.allclose([1e10,1e-7],[1.00001e10,1e-8]))
print(np.allclose([1e10,1e-8],[1.00001e10,1e-9]))
print(np.allclose([1e10,1e-8],[1.0001e10,1e-9]))
print(np.allclose([1e10,1e-7],[1.00001e10,1e-8]))
print(np.allclose([1.0,np.nan],[1.0,np.nan]))
print(np.allclose([1.0,np.nan],[1.0,np.nan],equal_nan= True))
###
# 10
x = np.array([3,5])
y = np.array([2,5])
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))
####
# 11
# x = .............
# y = .............
print(np.equal(x,y))
print(np.allclose(x,y))
####
# 12
print("%d bytes" % (tab3.size*tab3.itemsize))
####
# 13
print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5) 
print(np.full(10,5))
####
# 14
print(np.arange(start=30,stop=71))
####
# 15
print(np.arange(start=30,stop=71,step=2))
####
# 16
print(np.identity(3))
print(np.identity(3, dtype=int))
####
# 17
print(np.random.random())
####
# 18
print(np.array(list(np.random.random() for i in range(15))))
####
# 19
print(np.array(list(np.random.randint(15,55) for i in range(15)))[1:-1])
####
# 20
array = np.zeros(12,dtype=int).reshape((3,4))
for x in np.nditer(array):
    print(x)
####
# 21
print(np.linspace(5,50,10))
####
# 22
print(np.array(list(-i if 9<=i<=15 else i for i in range(20))))
####
# 23
array = np.arange(10)
np.random.shuffle(array)
print(array[0:5])
####
# 24
x = np.array([2,4])
y = np.array([1,2])
print(x*y)
####
# 25
print(np.array(list(-1 if i%2 else i for i in range(10))))
####
# 26
print(np.arange(9).reshape((3,-1)))
####
# 27
array = np.arange(4).reshape(2,-1)
print(array + np.full((2,2),202))
####
# 28
print(np.random.randint(30,41,size=10))
####
# 29
x = np.random.randint(30,41,size=10)
y = np.random.randint(30,41,size=10)
print(x)
print(y)
print(np.where(x > y))
print(np.where(x == y))
####
# 30
print(np.arange(100).reshape(5,-1)[:,:4])
####