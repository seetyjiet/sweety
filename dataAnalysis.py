import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

X = ['Group 1','Group 2','Group 4','Group 5','Group 6','Group 7','Group 8','Group 9','Group 10']

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
chemistry_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
physics_marks = [45, 76, 67, 56, 89, 76, 42, 54, 30, 35]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, math_marks, 0.4, label = 'Math')
plt.bar(X_axis + 0.2, chemistry_marks, 0.4, label = 'Chemistry')
plt.bar(X_axis + 0.2, physics_marks, 0.4, label = 'Physics')
  
plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.show()