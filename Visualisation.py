# Activity 1
import numpy as np
import matplotlib.pyplot as plt
x = [0,5,10,15,20,25,30]
y1 = [10,15,20,20,30,15,0]
y2 = [10,12,15,12,20,10,0]
plt.plot(x, y1, linestyle="dashed", marker="D")
plt.plot(x, y2, linestyle="dashed", marker="D")
plt.title("Velocity-Time Graph")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Time (s)")
plt.xlim(5,25)
plt.ylim(5,25)
plt.legend()
plt.show()

# Activity 2

x = np.arange(1,11,1)
y1 = (2*x) + 1
y2 = (2*x**2) + 2
plt.figure(figsize=(7,5))
plt.plot(x, y1, label="2*x + 1")
plt.plot(x, y2, label="2*x**2 + 2")
plt.legend(loc="upper left")
plt.show()
