# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:20:06 2024

@author: Luis Lucas García
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
"""
For the first part we will calculate the remaining concentration of two
uranium isotopes. Their decay curves are caracterized by their constant
lambda, which depends on each isotope.
"""

def N(t, N0, l): #The decay of an isotope depends on its constants

    return N0*np.exp(-l*t)

l1 = np.log(2)/4.468e9
l2 = np.log(2)/704.8e6
N0 = 1e6
t = np.linspace(0, 1e10, 10000)

#Then, we can plot activity and remaining nuclei

fig, ax = plt.subplots(1, 2)
fig.set_size_inches((12, 6))
ax[0].grid()
ax[0].set_title("Remaining nuclei")
ax[0].set_xlabel("t (years)")
ax[0].set_ylabel("N (nuclei)")
ax[0].plot(t, N(t, N0, l1), label="U-238")
ax[0].plot(t, N(t, N0, l2), label="U-235")
ax[0].legend()
ax[1].tick_params(bottom=True, top=False, left=False, right=True)
ax[1].tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=True)
ax[1].grid()
ax[1].set_title("Activity")
ax[1].set_xlabel("t (years)")
ax[1].set_ylabel("$Activity \\left( years^{-1} \\right)$")
ax[1].plot(t, l1*N(t, N0, l1), label="U-238")
ax[1].plot(t, l2*N(t, N0, l2), label="U-235")
ax[1].legend()
plt.savefig("Images\\Nuclei and activity.png", dpi=200)

"""
We want to do the second step of the decay chain of uranium, this means we have
to know the semi-life of the two isotopes of Thorium, a quick search gives us
that t(Th-234) = 24.1d and t(Th-231) = 25.52h. We can use the expression from
theor for the decay in chain of uranium. Let N2 be the concentration of the second
element from the chain.
"""

def N2(t, N0, l1, l2): #Decay of the second element
    
    return (N0*l1/(l2-l1))*(np.exp(-l1*t) - np.exp(-l2*t))

l3 = np.log(2)/(24.1/365)
l4 = np.log(2)/(25.52/(24*365))
t2 = np.linspace(0, 1e10, 10000)

#We plot activity and remaining nuclei, adding the second elements

fig, ax = plt.subplots(1, 2)
fig.set_size_inches((12, 6))
ax[0].grid()
ax[0].set_title("Remaining nuclei")
ax[0].set_xlabel("t (years)")
ax[0].set_ylabel("N (nuclei)")
ax[0].plot(t2, N(t2, N0, l1), label="U-238")
ax[0].plot(t2, N(t2, N0, l2), label="U-235")
ax[0].plot(t2, N2(t2, N0, l1, l3), "--", label="Th-234")
ax[0].plot(t2, N2(t2, N0, l2, l4), "--", label="Th-231")
ax[0].legend()
ax[1].tick_params(bottom=True, top=False, left=False, right=True)
ax[1].tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=True)
ax[1].grid()
ax[1].set_title("Activity")
ax[1].set_xlabel("t (years)")
ax[1].set_ylabel("$Activity \\left( years^{-1} \\right)$")
ax[1].plot(t2, l1*N(t2, N0, l1), label="U-238")
ax[1].plot(t2, l2*N(t2, N0, l2), label="U-235")
ax[1].plot(t2, l3*N2(t2, N0, l1, l3), "--", label="Th-234")
ax[1].plot(t2, l4*N2(t2, N0, l2, l4), "--", label="Th-231")
ax[1].legend()
fig.savefig("Images\\Nuclei and activity in chains.png", dpi=200)

"""
For this next section we will calculate when a given percentage, a, of the initial
quantity of uranium is present, we can solve for t in the analytical expression of
N(t) so it's easy to implement.
"""

def T(a, l):
    
    return -np.log(a)/l

U1, U2, U3 = T(0.9, l1), T(0.5, l1), T(0.1, l1)
U4, U5, U6 = T(0.9, l2), T(0.5, l2), T(0.1, l2)

print("We have 90% of the initial quantity of U-238 at", U1, "years, 50% at,", U2,
      "years and 10% at", U3, "years.")
print("We have 90% of the initial quantity of U-235 at", U4, "years, 50% at,", U5,
      "years and 10% at", U6, "years.")