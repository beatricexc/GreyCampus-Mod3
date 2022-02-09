#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt


# In[10]:


#creating 2 classes : estimate_coefficient ( logic argument) and plot_regression_line (formula for the logic)
# object oriented programming : class, function, methods

def estimate_coefficient(x,y):
#size of data set # then we call the mean of numpy # then we calculate the sum of square errors i.e. total observ y*x - n*means
#then we calculate the regression coefficient
    n = np.size(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y*x - n*mean_y*mean_x)
    SS_xx = np.sum(x*x - n*mean_x*mean_x)
    b1 = SS_xy / SS_xx
    b0 = mean_y - b1*mean_x
    return(b0, b1)



# Now plot the graph based on calculated values and create some random predicted values
def plot_regression_line(x,y,b):
    plt.scatter(x,y, color ='m', marker ="o")
    y_pred = b[0]+b[1]*x
    plt.plot(x,y_pred, color ='g')
    plt.xlabel('Size')
    plt.ylabel('Cost')
    plt.show()
    
# x = These are house sizes ranging from 1,000 sqft to 10k sqft
# y = the cost of house in multiple of 1000s
x = np.array([1,2,3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([300, 350, 500, 700, 800,850, 900, 900, 1000, 1200])

# now we estimate the coefficient
b = estimate_coefficient(x,y)
print("Estimated Coefficients: \nb0 = {} \nb1 = {}".format(b[0], b[1]))
plot_regression_line(x, y, b)


# In[ ]:




