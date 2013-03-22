import numpy as N

def lyamake(x0, x1, y0, y1, abstr, xres, yres, depth):
#AB STR given by calling main is a string of 1s and 0s corresponding to As and Bs respectively.

    #downcounter = xres -1 
    output = N.array([])
	rawfile = open('rawdata.txt', 'w')	

    for x in N.arange(x0,x1,(x1-x0)/xres):
        #print(str( N.floor((xres - downcounter)*100/xres)))
        #downcounter -= 1
        for y in N.arange(y0,y1,(y1-y0)/yres):
            #print(str(x)+','+str(y))
            v = N.array([.5])
            r = 0
            if abstr[0]:
                r = x
            else:
                r = y
            for i in N.arange(depth):
                if abstr[ (i+1) % abstr.size]:
                    r = N.append(r, x)
                else:
                    r = N.append(r, y)
                v = N.append(v, r[-1]*v[-1]*(1-v[-1]))
            output = N.append(output, N.sum( N.log( N.abs(r[1:]*(1- 2*v[1:])))))
		rawfile = i
    print(output.size)
    return N.reshape(output,(xres,yres))

if __name__ == "__main__":
    import numpy.random as R
    x0 = 2  #R.randint(400)/100.
    x1 = 4  #R.randint(100*x0,400)/100.
    y0 = 2  #R.randint(400)/100.
    y1 = 4  #R.randint(100*y0,400)/100.

    xwidth = 100
    ywidth = 100
    
    abstr = N.array([1,0])  #R.randint(0,2,10)

    lyafrac = lyamake(x0, x1, y0, y1, abstr, xwidth, ywidth, 100)
    lyafrac = lyafrac.T
    #Replace values in imagemap with blue and yellow.
    import matplotlib.pyplot as plt
    from matplotlib import colors
    
    imgcols = colors.ListedColormap(['yellow','black','blue'])
    imgbounds = [-100, -.01, .01, 100]
    imgnorm = colors.BoundaryNorm(imgbounds,imgcols.N)

    image = plt.imshow(lyafrac, cmap=imgcols, norm=imgnorm)
    plt.savefig('lyapimage[' + str(x0) + ',' + str(x1) + ']x['+ str(y0) + ',' + str(y1) + ', R' + str(xwidth) +'].png')
    plt.show()
    
      
