import numpy as np
from scipy.optimize import minimize

# Algorithm(1)
def objective1(w, u, q):
    return -np.dot(u, w) + q * np.sqrt(np.dot(w, w))

def constraint1(w):
    return np.sum(w) - 1

def constraint2(w, w_bar, zeta):
    return w - w_bar - zeta

u = np.array([1, 2, 3])  # Example values
q = 1  # Example value
w_bar = np.array([0.5, 0.5, 0.5])
zeta = 0.1

con1 = {'type': 'eq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': lambda w: constraint2(w, w_bar, zeta)}

w0 = np.ones(3) / 3
result1 = minimize(objective1, w0, args=(u, q), constraints=[con1, con2])
print("Algorithm(1) result:", result1.x)

# Algorithm(2)
def objective2(w):
    return np.dot(w, w)

def constraint3(w, u, r_min):
    return np.dot(u, w) - r_min

r_min = 1  # Example value
con3 = {'type': 'ineq', 'fun': lambda w: constraint3(w, u, r_min)}

result2 = minimize(objective2, w0, constraints=[con1, con3])
print("Algorithm(2) result:", result2.x)

# Algorithm(3)
def objective3(x, u, q):
    w = x[:-1]
    t = x[-1]
    return np.dot(np.array([-u, q]), np.array([w, t]))

def constraint4(x, n):
    w = x[:-1]
    return np.sqrt(np.dot(w, w)) - x[-1]

x0 = np.ones(4)
con4 = {'type': 'ineq', 'fun': lambda x: constraint4(x, 3)}

result3 = minimize(objective3, x0, args=(u, q), constraints=[con1, con4])
print("Algorithm(3) result:", result3.x)
