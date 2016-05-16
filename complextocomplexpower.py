import numpy as np
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __pow__(self,other): # make the use of, or z=x+yi, ln(z) = ln(r) + i(tetha)
        r = np.sqrt(self.real**2 + self.imag**2) # Modulus of complex #1
        if (self.real==0 and self.imag==0):
            print ('Error: z1 can not be zero, ZeroDivisionError')
            return 'nan'
        if self.real==0.0: 
            tet = np.pi/2
        else:
            tet = np.arctan(self.imag/self.real) # Argument of the complex #1
        return Complex(np.exp(other.real*np.log(r)-other.imag*tet)*np.cos(other.real*tet + other.imag*np.log(r)),
                       np.exp(other.real*np.log(r)-other.imag*tet)*np.sin(other.real*tet + other.imag*np.log(r)))
    
    def __str__(self):
        return '(%g,%g)'%(self.real,self.imag)
    
#if __name__=='__main__':
    
z1 = Complex(3.0,4.0)
z2 = Complex(2.0,-1.0)
mypow = z1**z2
print 'complex number z1 is ', z1
print 'complex number z2 is ', z2
print 'complex z1 the power of z2 is ', mypow
