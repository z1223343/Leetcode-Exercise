import math
maxint = 2**32/2-1
maxpower = int(math.floor(math.log(maxint,3)))
maxpowerof3 = 3**maxpower
print(maxint,maxpower,maxpowerof3)