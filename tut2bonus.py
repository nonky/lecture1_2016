## The difference of the two Area can be seen integrating the function in to two parts, 
## like in this case the integration from -5 to 5 is 1st part from -5 to 3 and 2nd part 
## 3 to 5, Therefore, 1st integral is the sum of the two parts and the 2nd interation is
## just the 1st only 
import numpy
import scipy.integrate as quad
def mygauss(x,cent=0,sig=0.1):
    return numpy.exp(-0.5*(x-cent)**2/sig**2)

I,err=quad.quad(mygauss,-5,5) 
print I
I1,err=quad.quad(mygauss,-5,3)
print I1
I2,err=quad.quad(mygauss, 3,5)
print I2
