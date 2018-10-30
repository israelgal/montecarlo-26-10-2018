import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math as mt

def E_0(n_e):
    E=[] 
    for i in range(n_e):
        E.append([rd.choice([-1,1])for i in range(n_e)])

    return E

def U_interacction(x,y,E):
    J=1.0
    DimX =  len(E)
    DimY = len(E[0])
    if (x<(DimX-1)):
       S_r = E[x+1][y]
    else:
       S_r = E[0][y]
    S_l = E[x-1][y]
    if (y<(DimY-1)):
       S_u = E[x][y+1]
    else:
       S_u = E[x][0]
    S_d = E[x][y-1]
    u = -J*(S_r + S_l + S_u + S_d)*E[x][y]
    return u



def Magnetization(E):
    s = np.array(E).sum()
    return s


def MCStep(E,n_e,T):
    x = rd.randint(0,n_e-1)
    y = rd.randint(0,n_e-1)
    DU = -2.*U_interacction(x,y,E)
    if DU>0:
       r = rd.random()
       if r<=mt.exp(-DU/T):
          E[x][y]=-E[x][y]
    else:
       E[x][y] = -E[x][y]
    return E

def MC(T,E):
    for i in range(10000000):
        E = MCStep(E,n_e,T)
    return E

def MCmagnetization(T,E):
    N=10000000  
    M=0
    n=0
    for i in range(N):
        E = MCStep(E,n_e,T)
        if (i >= N-50):
           M = M + Magnetization(E)
           n = n+1
    return M/n

n_e = 100
E0 = E_0(n_e)

a="2"


if a=="1":
   print("Magnetizacion")
   l = np.linspace(.5,4,10)
   v = [ abs(MCmagnetization(T,E0)) for T in l]
   plt.plot(l,v)
   plt.savefig("MC.png")
   plt.show()
else:
   T=0.1
   plt.imshow(MC(T,E0))
   plt.savefig("MC2.png")
   plt.show()































 






























 
