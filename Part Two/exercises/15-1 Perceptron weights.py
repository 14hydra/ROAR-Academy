import numpy as np
import matplotlib.pyplot as plt


x1_intercept = -2
x2_intercept = 3


point1 = (x1_intercept, 0)  
point2 = (0, x2_intercept)


# For (x1, x2) = (-2, 0): -2*w1 + 0*w2 + w0 = 0 --> w0 = 2*w1
# For (x1, x2) = (0, 3): 0*w1 + 3*w2 + w0 = 0 --> w0 = -3*w2


# w0 = 2 * w1
# w0 = -3 * w2
# So: 2 * w1 = -3 * w2 --> w1 / w2 = -3 / 2


w2 = 2
w1 = -3
w0 = 2 * w1  

print("Computed weights:")
print(f"w1 = {w1}")
print(f"w2 = {w2}")
print(f"w0 = {w0}")


def decision_boundary(x1):
    return (-w1 * x1 - w0) / w2

x1_vals = np.linspace(-5, 5, 100)
x2_vals = decision_boundary(x1_vals)


plt.figure(figsize=(8, 6))
plt.plot(x1_vals, x2_vals, label='Decision Boundary', color='blue')
plt.plot(x1_intercept, 0, 'ro', label='x₁-intercept (-2, 0)')
plt.plot(0, x2_intercept, 'go', label='x₂-intercept (0, 3)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x₁')
plt.ylabel('x₂')

plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()



plt.show()
