x = [0,1]
for i in xrange(7):    
    x.append(x[-1] + x[-2]) 
print ', '.join(str(y) for y in x)
