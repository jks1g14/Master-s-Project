import numpy as np
from matplotlib import pyplot as plt

#==============================================================================
# Variables
#==============================================================================

samples = 100000   #Number of iterations
mu = 1 #Mean 
sigma = 1 #Variance
phi_i = -0.5 #Initial Phi Value
scale = 1 #Scale factor for theoretical


#==============================================================================
# MCMC
#==============================================================================

'Acceptance probability T_A'    
def T_A(phi_prop,phi):
    return np.sqrt(1-(phi_prop**2))/(np.sqrt(1-(phi**2)))

'Array of accepted values of phi'
phi_y = []

for i in range(samples):
        'Proposed phi'
        phi_prop = np.random.normal(mu,sigma)
        
        'Proposed phi if not between -1 or 1'
        while phi_prop < -1 or phi_prop > 1:
            phi_prop = np.random.normal(mu,sigma)
        
        'For first iteration when no phi(i-1) value'
        if i == 0:
            phi = phi_i
            t_accept = min(1,T_A(phi_prop,phi_i))
            
        else: 
            'Choose acceptance probability T_A'
            t_accept = min(1,T_A(phi_prop,phi))
            'Choose uniform random number'
            u = np.random.uniform()
        
        'Acceptance condition - proposed phi is accepted'
        if u < t_accept:
            phi = phi_prop
            phi_y.append(phi)
        
        else:
            'Rejection - previous phi is kept' 
            phi=phi
            phi_y.append(phi)
           
'Create a time array'                        
t = np.arange(0,len(phi_y),1) 

'Only look at values after a certain number of samples - warm up period'
cut_off = int(0.2*samples)
phi_y = phi_y[cut_off:]
t = t[cut_off:]

#==============================================================================
# Function check for comparison
#==============================================================================

'Function we want to test'
def P(phi,mu,sigma):
    return ((1-phi**2)**(0.5))*np.exp(-((phi-mu)**2)/(2*sigma**2))

'Arrays for the function plot' 
x_theory = []
phi_theory = []


'Create values for function plot'
for i in np.arange(-1,1,0.001):
    phi_theory.append(P(i,mu,sigma)*scale)
    x_theory.append(i)


#==============================================================================
# Graph of function 
#==============================================================================

#plt.subplot(2,1,1)
'Histogram of simulation'
plt.hist(phi_y,200,normed=True) #Note value is normalised

'Plot of expected function'
plt.plot(x_theory,phi_theory)


#plt.subplot()
#plt.xlim(55000,55200)
#plt.plot(t,phi_y)
#plt.plot(t,y)




