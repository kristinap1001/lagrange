import sys
from matplotlib import pyplot as plt
import numpy as np
from decimal import Decimal

# Kristina Pettersson
# Lagrange Points Calculator
# January 31, 2023

def mag(v):
    # Helper function for vector magnitudes
    return np.sqrt(v[0]**2 + v[1]**2)

def potential(r):
    # Gravitational potential at point r
    return -m1/mag( [r[0]-x1,r[1]] ) - m2/mag( [r[0]-x2,r[1]] ) - 1/2 * omegaSq*mag(r)**2


def gx(r):
    # x component of grav accel
    return -m1*(r[0] - x1) / mag( [r[0]-x1,r[1]] )**3 - m2*(r[0] - x2) / mag( [r[0]-x2,r[1]] )**3 + omegaSq*r[0]
def gx_y0(x):
    # Calculates x component only on x axis, for finding L1-L3
    return gx([x,0])


def gy(r):
    # y compponent of grav accel
    return -m1*r[1] / mag( [r[0]-x1,r[1]] )**3 - m2*r[1] / mag( [r[0]-x2,r[1]] )**3 + omegaSq*r[1]
def gy_xmidpoint(y):
    # Calculates y component only on y=(x1+x2)/2 axis, for finding L4 and L5
    return gy([(x1+x2)/2, y])


def bisection(l,u,f,tol):
    # Finds root of f between x=l and x=u within tolerance tol
    mid = (l+u)/2
    while (u-l)/2 > tol:
        if f(mid) == 0:
            return mid
        elif f(l)*f(mid) < 0:
            u = mid
        else:
            l = mid
        mid = (l+u)/2
    return mid

def main(argv):
    if (len(sys.argv) != 4):
        sys.exit('Usage: lagrange.py m1 m2 d')

    global m1,m2,m,x1,x2,omegaSq
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    d = float(sys.argv[3])

    # Checking input
    if(m1<=0 or m2<=0):
        sys.exit('Masses must be greater than zero')
    if(d<=0):
        sys.exit('Distance must be greater than zero')

    m = m1+m2
    omegaSq = m/(d**3) # Angular velocity squared
    # Distances from m1 and m2 to center of gravity
    x1 = -(m2/m)*d
    x2 = (m1/m)*d

    # Calculating Lagrange points
    # Some lower/upper bounds are adjusted by 0.01 to avoid dividing by 0 or algorithm placing l4/l5 on x axis

    # L1: on x axis between x1 and x2
    l1 = bisection(x1+0.01,x2-0.01,gx_y0,1e-4)

    # L2: on x axis to the right of x2
    l2 = bisection(x2+0.01,2*d,gx_y0,1e-4)

    # L3: on x axis to the left of x1
    l3 = bisection(-2*d,x1-0.01,gx_y0,1e-4)

    # L4: above midpoint between x1 and x2
    l4 = bisection(0.01,2*d,gy_xmidpoint,1e-4)

    # L5: below midpoint between x1 and x2
    l5 = bisection(-2*d,-0.01,gy_xmidpoint,1e-4)

    # Printing output
    print("Locations of Lagrange points for m1 = %3.2E & m2 = %3.2E solar masses, d = %3.2f AU:" % (Decimal(m1),Decimal(m2),d))
    print("L1: (%1.4f,0)" % l1)
    print("L2: (%1.4f,0)" % l2)
    print("L3: (%1.4f,0)" % l3)
    print("L4: (%1.4f,%1.4f)" % ((x1+x2)/2,l4))
    print("L5: (%1.4f,%1.4f)" % ((x1+x2)/2,l5))


    # Creating graph
    x,y = np.meshgrid(np.linspace(-2*d,2*d,60),np.linspace(-2*d,2*d,60))
    r = [x,y]
    fig,ax = plt.subplots(1,1,figsize=(7,7))

    fig.suptitle("Gravitational Potential Contours and Acceleration Vectors")
    ax.set_title("m1 = %3.2E & m2 = %3.2E solar masses, d = %3.2f AU" % (Decimal(m1),Decimal(m2),d))
    ax.set_xlabel("Distance from center of mass (AU)")

    # Axes
    plt.axvline(x=0)
    plt.axhline(y=0)

    # Potential contour lines (log scale)
    cs = plt.contour(x,y, np.log10(-potential(r)), levels=25)
    #plt.clabel(cs)

    # Gravitational force vector field
    gnorm = mag([gx(r),gy(r)]) # Divide by gnorm^0.6 just to make vectors look nice on graph
    q = plt.quiver(x,y, gx(r)/gnorm**0.6, gy(r)/gnorm**0.6)

    # Points for m1 and m2
    plt.plot(x1,0,'bo',markersize=3)
    plt.plot(x2,0,'bo',markersize=3)

    # Lagrange points
    plt.plot(l1,0,'ro',markersize=3)
    plt.plot(l2,0,'ro',markersize=3)
    plt.plot(l3,0,'ro',markersize=3)
    plt.plot((x1+x2)/2,l4,'ro',markersize=3)
    plt.plot((x1+x2)/2,l5,'ro',markersize=3)

    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
