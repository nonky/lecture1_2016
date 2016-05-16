import numpy as np
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __pow__(self,r): # using polar form (r&teatha) and Euler's Equation
        self.r = np.sqrt(self.real**2 + self.imag**2)
        if self.real==0.0: # condition is set for the benefit of integer powers 
            tet = np.pi/2
        else:
            tet = np.arctan(self.imag/self.real)
        return Complex(self.r**pr*np.cos(pr*tet),
                       self.r**pr*np.sin(pr*tet))

    def __str__(self):
        return '(%g,%g)'%(self.real,self.imag)

z = Complex(3.0,4.0)
pr = 2 # for integer
mypow = z**pr
print 'the complex number is z', z
print 'complex number z the power of ', repr(pr)
print 'is ', (mypow)
pr = 1/2.0 # for abitraray real number 
mypow1 = z**pr
print 'complex number z the power of ', repr(pr)
print 'is ', (mypow1
