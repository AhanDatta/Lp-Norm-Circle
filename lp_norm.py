import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

#Plot constants
X_MIN = -1.0
X_MAX = 1.0
Y_MIN = -1.0
Y_MAX = 1.0
P_MIN = np.log(0.1)
P_MAX = np.log(10.0)
DOMAIN = np.linspace(X_MIN, X_MAX, 1000)
P_DOMAIN = np.linspace(P_MIN, P_MAX, int(100*(P_MAX-P_MIN)))

#Defines the l^p norm for a point
def lp_norm (x: np.ndarray, p: float):
    powers = np.power(x, p * np.ones(len(x)))
    return np.power(np.sum(powers), 1/p)

#Finds the points which satisfy the circle for a given norm and x domain
#y = (1 - x^p)^(1/p)
def find_circle(x: float, p: float):
    return np.power(1 - np.power(np.absolute(x),p), (1/p))

#Defines and produces animation for the plot
fig, ax = plt.subplots()
def init():
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(Y_MIN, Y_MAX)

#Draws the circle new for each frame with exponential growth in p
def update(frame):
    ax.cla()
    p = np.exp(frame)
    ax.set_title("Circle in an Lp norm of p = " + str(np.round(p, 2)))
    ax.set_aspect('equal')
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(Y_MIN, Y_MAX)
    ax.plot(DOMAIN, find_circle(DOMAIN, p), color="blue")
    ax.plot(DOMAIN, -find_circle(DOMAIN, p), color="blue")

ani = FuncAnimation(fig, update, frames=np.concatenate((P_DOMAIN, np.flip(P_DOMAIN))), init_func=init, interval = 2)

#ani.save("circle.gif", fps = 50)
plt.show()