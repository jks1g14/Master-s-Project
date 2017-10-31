import numpy as np
from matplotlib import pyplot as plt
#from scipy import stats

'mu = mean, sigma = standard deviation'
mu = 5 #mean
sigma = 1.5 #standard deviation
trials = 100000

x_2_mean = mu**2 + sigma**2
x_3_mean = mu*(mu**2+3*sigma**2)

def f_x_2(x):
    return x**2

def f_x_3(x):
    return x**3

pd = np.random.normal(mu,sigma,trials)
print 'x'
print 'Simulation Value', sum(pd)/trials
print 'Expected Value', mu
print ''
print 'x^2'
print 'Simulation Value: ',sum(f_x_2(pd))/trials
print 'Expected Value: ', x_2_mean
print ''
print 'x^3'
print 'Simulation Value: ', sum(f_x_3(pd))/trials
print 'Expected Value: ', x_3_mean

plt.hist(pd,100)