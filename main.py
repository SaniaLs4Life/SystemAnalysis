from numpy import *
from matplotlib.pyplot import *
from scipy.stats import *



x = array([0,1,2,3,4,5])
y = array([0,0.8,0.9,1,-0.8,-1])

p1 = polyfit(x,y,1)
p2 = polyfit(x,y,2)
p3 = polyfit(x,y,3)

plot(x,y,'o')

xp = linspace(-2, 6, 100)

plot(xp, polyval(p1, xp), 'r-')
plot(xp, polyval(p2, xp), 'b--')
plot(xp, polyval(p3, xp), 'm:')

yfit = p1[0] * x + p1[1]

yresid = y - yfit
SSresid = sum(pow(yresid,2))
SStotal = len(y) * var(y)
rsq = 1 - SSresid/SStotal


slope, intercept, r_value, p_value, std_err = linregress(x,y)



print('Y Fit : ',yfit)
print('Y : ', y)
print('P1 : ',p1)
print('P2 : ',p2)
print('P3 : ',p3)
print('RSQ : ',rsq)
print('R Value : ',pow(r_value, 2))
print('P Value : ', p_value)
show()

