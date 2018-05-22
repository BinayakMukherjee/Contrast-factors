# Contrast-factors
Calculation of contrast factors of dislocations in crystals using Python. Ref. Ungar et al [J. Appl. Cryst. (1999). 32,
992-1002], Dragomir and Ungar [Powder Diffraction 17 (2), June 2002], and Dragomir and Ungar [J. Appl. Cryst. (2002).
35, 556-564]

This can be implemented as a widget in WONDER, to be plugged in before the Krivoglaz-Wilkens strain model. It takes as
input the elastic constants c11, c12 and c44, as well as the crystal symmetry (slip system) and proportion of screw or
edge dislocations, and outputs possible initial values for A_screw, B_screw, A_edge, B_edge and a final C_avg. It works
by taking the data provided in the papers by Ungar, and is limited by them. In cases where the values of c12/c44 or the
Zener ratio are outside of the range given by Ungar, the relevant A's, B's or C's are set to 0, and a message informing
the user that the data is out of range is displayed.