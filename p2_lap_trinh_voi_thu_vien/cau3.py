import matplotlib.pyplot as plt
import numpy as np

def dao_ham_pt_y(x):
    pt=x**4 - 2*x**2 - 3
    return pt
def dao_ham_pt_y1(x):
    pt1=4*x**3 - 4*x
    return pt1
def dao_ham_pt_y2(x):
    pt2 = 12*x**2 - 4
    return pt2
def dao_ham_pt_y3(x):
    pt3 = 24*x
    return pt3
fig, ax = plt.subplots()
x=np.linspace(-10,10,20)
y= dao_ham_pt_y(x)
ax.plot(x,y,'*-',ms=8, markeredgewidth=0.5,label=r'$y=x^{4}-2x^{2}-3$')
y1= dao_ham_pt_y1(x)
ax.plot(x,y1,'o-',ms=5,markeredgewidth=0.2, label=r"$y'=4x^{3}-4x$")
y2= dao_ham_pt_y2(x)
ax.plot(x,y2,'x-',ms=9,markeredgewidth=0.2,label=r"$y''=12x^{2}-4$")
y3= dao_ham_pt_y3(x)
ax.plot(x,y3,'+-',ms=9,markeredgewidth=0.2,label=r"$y'''=24x$")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
ax.legend()
plt.show()

