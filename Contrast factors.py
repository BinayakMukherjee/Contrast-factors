import numpy
import scipy.interpolate
import matplotlib as plt

#========================================================#

def zener(c11,c12,c44): # definition of the Zener ratio
    return 2*c44/(c11-c12)

def c_(c11,c12): # definition of the ratio c_12/c_44
    return c12/c44

def param_eqn(a,b,c,d,zener): # parametrization equation
    return a*(1-numpy.exp(-zener/b)) + c*zener + d

#--- A parameters, low Zener ratio ----------------------#

def A_lowZen_screw_FCC(zener): # calculation of parameter A for Zener ratio <=0.5 for screw dislocation
                               # in FCC <110>{111} slip system
    a = 0.0454
    b = 0.1704
    c = 0.0901
    d = 0.0275
    return param_eqn(a,b,c,d,zener)

def A_lowZen_edge_FCC(zener,c_): # calculation of parameter A for Zener ratio <=0.5 for edge dislocation
                                 # in FCC <110>{111} slip system
    a05 = 0.0737 # parameters for c_12/c_44 = 0.5
    b05 = 0.1712
    c05 = 0.0901
    d05 = 0.0275
    a1 = 0.0659 # parameters for c_12/c_44 = 1
    b1 = 0.1551
    c1 = 0.0930
    d1 = 0.0274
    a2 = 0.0552 # parameters for c_12/c_44 = 2
    b2 = 0.1411
    c2 = 0.1057
    d2 = 0.0279
    a3 = 0.0493 # parameters for c_12/c_44 = 3
    b3 = 0.1399
    c3 = 0.1179
    d3 = 0.0286
    x = numpy.array([0.5,1,2,3])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)

def A_lowZen_screw_BCC(zener,c_): # calculation of parameter A for Zener ratio <=0.5 for screw dislocation in
                                  # BCC <111>{110} slip system
    a05 = 0.0736 # parameters for c_12/c_44 = 0.5
    b05 = 0.2822
    c05 = 0.1342
    d05 = 0.0264
    a1 = 0.0624 # parameters for c_12/c_44 = 1
    b1 = 0.2236
    c1 = 0.1532
    d1 = 0.024
    a2 = 0.1264 # parameters for c_12/c_44 = 2
    b2 = 0.385
    c2 = 0.0845
    d2 = 0.0249
    a3 = 0.1271 # parameters for c_12/c_44 = 3
    b3 = 0.3591
    c3 = 0.0842
    d3 = 0.0233
    a5 = 0.1321 # parameters for c_12/c_44 = 5
    b5 = 0.3334
    c5 = 0.0783
    d5 = 0.0216
    x = numpy.array([0.5,1,2,3,5])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener),param_eqn(a5,b5,c5,d5,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)

def A_lowZen_edge_BCC(zener,c_): # calculation of parameter A for Zener ratio <=0.5 for edge dislocation in
                                 # BCC <111>{110} slip system
    a05 = 0.0565 # parameters for c_12/c_44 = 0.5
    b05 = 0.1548
    c05 = 0.0821
    d05 = 0.02432
    a1 = 0.04901 # parameters for c_12/c_44 = 1
    b1 = 0.1327
    c1 = 0.08528
    d1 = 0.02382
    a2 = 0.03768 # parameters for c_12/c_44 = 2
    b2 = 0.10732
    c2 = 0.10115
    d2 = 0.02373
    a3 = 0.03181 # parameters for c_12/c_44 = 3
    b3 = 0.09116
    c3 = 0.11696
    d3 = 0.02269
    a5 = 0.02702 # parameters for c_12/c_44 = 5
    b5 = 0.07624
    c5 = 0.14048
    d5 = 0.02075
    x = numpy.array([0.5,1,2,3,5])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener),param_eqn(a5,b5,c5,d5,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)

#--- B parameters, low Zener ratio ----------------------#

def B_lowZen_screw_FCC(zener): # calculation of parameter B for Zener ratio <=0.5 for screw dislocation
                               # in FCC <110>{111} slip system
    a = 48.5946
    b = 0.0713
    c = 9.7907
    d = -58.552
    return - param_eqn(a,b,c,d,zener) * A_lowZen_screw_BCC(zener,c_)

def B_lowZen_edge_FCC(zener,c_): # calculation of parameter B for Zener ratio <=0.5 for edge dislocation
                                 # in FCC <110>{111} slip system
    a05 = 43.4223 # parameters for c_12/c_44 = 0.5
    b05 = 0.0739
    c05 = 6.9926
    d05 = -48.3544
    a1 = 43.4100 # parameters for c_12/c_44 = 1
    b1 = 0.0744
    c1 = 7.6463
    d1 = -48.9061
    a2 = 43.3221 # parameters for c_12/c_44 = 2
    b2 = 0.07568
    c2 = 8.6402
    d2 = -49.6478
    a3 = 43.3401 # parameters for c_12/c_44 = 3
    b3 = 0.0771
    c3 = 9.2576
    d3 = -50.1819
    x = numpy.array([0.5,1,2,3])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return -y_interp(c_) * A_lowZen_edge_BCC(zener,c_)

def B_lowZen_screw_BCC(zener,c_): # calculation of parameter B for Zener ratio <=0.5 for screw dislocation
                                  # in BCC <111>{110} slip system
    a = 54.1422
    b = 0.0731
    c = 9.7907
    d = -58.552
    return - param_eqn(a, b, c, d, zener) * A_lowZen_screw_FCC(zener,c_)

def B_lowZen_edge_BCC(zener,c_): # calculation of parameter B for Zener ratio <=0.5 for edge dislocation
                                 # in BCC <111>{110} slip system
    a05 = 45.89136 # parameters for c_12/c_44 = 0.5
    b05 = 0.0691
    c05 = 9.09972
    d05 = -53.08442
    a1 = 45.86721 # parameters for c_12/c_44 = 1
    b1 = 0.06885
    c1 = 10.20281
    d1 = -53.96221
    a2 = 44.80338 # parameters for c_12/c_44 = 2
    b2 = 0.07067
    c2 = 11.87255
    d2 = -54.17248
    a3 = 45.14885 # parameters for c_12/c_44 = 3
    b3 = 0.07123
    c3 = 13.46823
    d3 = -55.52068
    a5 = 46.18657 # parameters for c_12/c_44 = 5
    b5 = 0.0732
    c5 = 15.16578
    d5 = -57.58587
    x = numpy.array([0.5,1,2,3,5])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener),param_eqn(a5,b5,c5,d5,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return -y_interp(c_) * A_lowZen_edge_FCC(zener,c_)

#--- A parameters, high Zener ratio ----------------------#

def A_highZen_screw_FCC(zener): # calculation of parameter A for Zener ratio > 0.5 for screw dislocation
                                # in FCC <110>{111} slip system
    a = 0.1740
    b = 1.9522
    c = 0.0293
    d = 0.0662
    return param_eqn(a,b,c,d,zener)

def A_highZen_edge_FCC(zener,c_): # calculation of parameter A for Zener ratio > 0.5 for edge dislocation
                                  # in FCC <110>{111} slip system
    a05 = 0.1312 # parameters for c_12/c_44 = 0.5
    b05 = 1.4284
    c05 = 0.0201
    d05 = 0.0954
    a1 = 0.1687 # parameters for c_12/c_44 = 1
    b1 = 2.0400
    c1 = 0.0194
    d1 = 0.0926
    a2 = 0.2438 # parameters for c_12/c_44 = 2
    b2 = 2.4243
    c2 = 0.0172
    d2 = 0.0816
    a3 = 0.2635 # parameters for c_12/c_44 = 3
    b3 = 2.1880
    c3 = 0.0186
    d3 = 0.0731
    x = numpy.array([0.5,1,2,3])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)

def A_highZen_screw_BCC(zener,c_): # calculation of parameter A for Zener ratio > 0.5 for screw dislocation
                                   # in BCC <111>{110} slip system
    a = 0.1740
    b = 1.9522
    c = 0.0293
    d = 0.0662
    return param_eqn(a, b, c, d, zener)

def A_highZen_edge_BCC(zener,c_): # calculation of parameter A for Zener ratio > 0.5 for edge dislocation
                                  # in BCC <111>{110} slip system
    a05 = 1.4948 # parameters for c_12/c_44 = 0.5
    b05 = 25.671
    c05 = 0.0
    d05 = 0.0966
    a1 = 1.6690 # parameters for c_12/c_44 = 1
    b1 = 21.124
    c1 = 0.0
    d1 = 0.0757
    a2 = 1.4023 # parameters for c_12/c_44 = 2
    b2 = 12.739
    c2 = 0.0
    d2 = 0.0563
    x = numpy.array([0.5,1,2])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return y_interp(c_)

#--- B parameters, high Zener ratio ----------------------#

def B_highZen_screw_FCC(zener): # calculation of parameter B for Zener ratio > 0.5 for screw dislocation
                                # in FCC <110>{111} slip system
    a = 0.0454
    b = 0.1704
    c = 0.0901
    d = 0.0275
    return - param_eqn(a,b,c,d,zener) * A_lowZen_screw_FCC(zener)

def B_highZen_edge_FCC(zener,c_): # calculation of parameter B for Zener ratio > 0.5 for edge dislocation
                                  # in FCC <110>{111} slip system
    a05 = 4.0327 # parameters for c_12/c_44 = 0.5
    b05 = 0.8846
    c05 = 0.0986
    d05 = -2.8225
    a1 = 4.8608 # parameters for c_12/c_44 = 1
    b1 = 0.8687
    c1 = 0.0896
    d1 = -3.4280
    a2 = 5.8282 # parameters for c_12/c_44 = 2
    b2 = 0.8098
    c2 = 0.0828
    d2 = -4.297
    a3 = 6.3398 # parameters for c_12/c_44 = 3
    b3 = 0.7751
    c3 = 0.0813
    d3 = -4.8129
    x = numpy.array([0.5,1,2,3])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener),
                     param_eqn(a3,b3,c3,d3,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return -y_interp(c_) * A_highZen_edge_FCC(zener,c_)

def B_highZen_screw_BCC(zener,c_): # calculation of parameter B for Zener ratio > 0.5 for screw dislocation
                                   # in BCC <111>{110} slip system
    a05 = 7.5149 # parameters for c_12/c_44 = 0.5
    b05 = 0.3818
    c05 = 0.0478
    d05 = -4.9826
    a1 = 8.6590 # parameters for c_12/c_44 = 1
    b1 = 0.3730
    c1 = 0.0424
    d1 = -6.074
    a2 = 6.0725 # parameters for c_12/c_44 = 2
    b2 = 0.4338
    c2 = 0.0415
    d2 = -3.5021
    x = numpy.array([0.5,1,2])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return -y_interp(c_) * A_highZen_screw_BCC(zener,c_)

def B_highZen_edge_BCC(zener,c_): # calculation of parameter B for Zener ratio > 0.5 for edge dislocation
                                  # in BCC <111>{110} slip system
    a05 = 5.3020 # parameters for c_12/c_44 = 0.5
    b05 = 1.0945
    c05 = 0.1540
    d05 = -4.1841
    a1 = 7.2361 # parameters for c_12/c_44 = 1
    b1 = 0.9285
    c1 = 0.1359
    d1 = -5.7484
    a2 = 8.8331 # parameters for c_12/c_44 = 2
    b2 = 0.8241
    c2 =  0.1078
    d2 = -7.0570
    x = numpy.array([0.5,1,2])
    y = numpy.array([param_eqn(a05,b05,c05,d05,zener),param_eqn(a1,b1,c1,d1,zener),param_eqn(a2,b2,c2,d2,zener)])
    y_interp = scipy.interpolate.interp1d(x, y)
    return -y_interp(c_) * A_highZen_edge_BCC(zener,c_)

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
