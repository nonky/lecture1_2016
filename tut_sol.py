import numpy as np

x0=0
x1=np.pi/2

mydelts=[x1/10,x1/30,x1/100,x1/300,x1/1000]
for dx in mydelts:
    x = np.arange(x0,x1,dx)
    y = np.cos(x)
    tot = y.sum()*dx
    print 'integral is ' + repr(tot) + ' with dx=' + repr(dx)


#oddx=x[1:n:2]
#for i in oddx:
#	print oddx[i]
#evenx=x[2:n-1:2]
#for k in evenx:
#s	print evenx[k]

x0=0
x1=np.pi/2
n=input("points")
mydelts=[x1/n]
for dx in mydelts:
	x=np.arange(x0,x1,dx)
	evenx=x[2:n-2:2]
	oddx=x[1::2]
	y=np.cos(x)
	tot_end= y[0]+y[n-1]
	tot_odd=[j*4 for j in oddx]
	tot_even= [i*2 for i in evenx]
	total= dx*(tot_end + sum(tot_odd)+sum(tot_even))/3
print 'integral is ' + repr(total) + 'with dx=' + repr(dx)



