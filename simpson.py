# Tutorial2 Question2a: Integration of cos(x) for 0 to pi/2 for range # of points using the simple mothod, include 10,30,100,300,1000 points between 0 and pi/2
import numpy as np 
xi = 0
xf = np.pi/2 
delta = [(xf-xi)/10,(xf-xi)/30,(xf-xi)/100,(xf-xi)/300,(xf-xi)/1000]
for dx in delta:
     x = np.arange(xi,xf,dx)
     y = np.cos(x)
     total = y.sum()*dx  
     print 'integral is ' + repr(total) + ' with dx=' + repr(dx)
