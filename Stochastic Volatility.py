#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: jamesstephens
"""
import numpy as np
from matplotlib import pyplot as plt

#==============================================================================
# Stochastic Volatility
#==============================================================================

'Variables'
mu = 1
phi = 0.1
start_sig = 1
sigma_n = 1
trials = 500000 

'Arrays' 
sigma = []
y_t = []


'Function defining the logarithm of the sigma variable'
def ln_sigma_t(mu,phi,ln_sig_1,sig_n): 
    return mu+phi*(np.log(ln_sig_1)-mu)+np.random.normal(0,sig_n**2)

'Carry out the stochastic simulation over set number of trials'
for i in range(trials):
    if i == 0: #Random variable used for first sigma because no sigma_t-1
        sigma.append(np.exp(ln_sigma_t(mu,phi,start_sig,sigma_n)))
        y_t.append(sigma[0]*np.random.normal(0,1))
    else:
        sigma.append(np.exp(ln_sigma_t(mu,phi,sigma[i-1],sigma_n)))
        y_t.append(sigma[i]*np.random.normal(0,1))

'Create a time array'
t = np.arange(0,len(y_t),1)

'Create a ln sigma array'
ln_sigma = np.log(sigma)

'Only use values after a warm up period'
cut_off = int(0.2*trials)
y_t = y_t[cut_off:]
t = t[cut_off:]
ln_sigma = ln_sigma[cut_off:]

'Plot the data'
plt.plot(t,y_t) 
    
'Check data using mean and variance' 
theory_var = (sigma_n**2)/(1-(phi**2))
mean = np.mean(ln_sigma)
exp_var = np.var(ln_sigma)


print 'Theoretical Mean:', mu
print 'Experimental Mean:',np.mean(ln_sigma)
print 'Percentage Difference:', (abs(mean-mu)/mu)*100
print ''
print ''
print 'Theoretical Variance:', theory_var
print 'Experimental Variance:', exp_var
print 'Percentage Difference:', ((abs(theory_var-exp_var))/theory_var)*100
