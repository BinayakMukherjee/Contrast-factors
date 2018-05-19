import numpy
import scipy.interpolate
import matplotlib as plt

#===================================================#

def zener(c11,c12,c44): # definition of the Zener ratio
    return 2*c44/(c11-c12)
def c_(c11,c12): # definition of the ratio c_12/c_44
    return c12/c44
def param_eqn(a,b,c,d,zener): # parametrization equation
    return a*(1-numpy.exp(-zener/b)) + c*zener + d
def A_lowZen_screw_BCC(zener): #calculation of parameter A for Zener ratio <=0.5 for screw dislocation in BCC <110>{111} slip system
    a = 0.0454
    b = 0.1704
    c = 0.0901
    d = 0.0275
    value = param_eqn(a,b,c,d,zener)
    return value
def A_lowZen_edge_BCC(zener,c_): #calculation of parameter A for Zener ratio <=0.5 for edge dislocation in BCC <110>{111} slip system
    a05 = 0.0737 #parameters for c_12/c_44 = 0.5
    b05 = 0.1712
    c05 = 0.0901
    d05 = 0.0275
    a1 = 0.0659 #parameters for c_12/c_44 = 1
    b1 = 0.1551
    c1 = 0.0930
    d1 = 0.0274
    a2 = 0.0552 #parameters for c_12/c_44 = 2
    b2 = 0.1411
    c2 = 0.1057
    d2 = 0.0279
    a3 = 0.0493 #parameters for c_12/c_44 = 3
    b3 = 0.1399
    c3 = 0.1179
    d3 = 0.0286
    x = numpy.array([0.5,1,2,3])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),param_eqn(a3,b3,c3,d3,zener)])
    print(y)
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)
def A_lowZen_screw_FCC(zener,c_): #calculation of parameter A for Zener ratio <=0.5 for screw dislocation in FCC <111>{110} slip system
    a =
    b =
    c =
    d =
    x = numpy.array([0.5,1,2,3])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),param_eqn(a3,b3,c3,d3,zener)])
    print(y)
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)
#===================================================#

def main():
#--- User inputs ----------------------#
    c11 = 1
    c12 = 2
    c44 = 3
    screw_fraction = 0.5
    edge_fraction = 1 - screw_fraction
#--------------------------------------#
    zener_ratio = zener(c11,c12,c44)
    #if (zener_ratio <= 0.5):
    print(A_lowZen_screw_BCC(0.4,2.35))
    return

main()
