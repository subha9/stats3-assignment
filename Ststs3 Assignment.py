
# coding: utf-8

# In[1]:


#  State the hypotheses

# The population mean is 100.
# Null Hypotheses            H0: μ= 100
# Alternate hypotheses       H1: μ > 100



# significance level not given in the problem so let’s assume it as 5% (0.05).
#  Compute the random chance probability using z score and z-table.

# Compute the random chance probability using z score and z-table.
# For this set of data: z= (108-100) / (15/√36)=3.20
import math

Z =  (108-100) / (15/math.sqrt(36))
Z


# In[ ]:


It is less than 0.05 so we will reject the Null hypothesis i.e. there is raw cornstarch effec
   


# In[ ]:


Problem #2

#In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple random sample of 100 voters are surveyed from each state.

#What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?


# In[ ]:



# P1 = The proportion of Republican voters in the first state = 0.52
# 1-P1 = The proportion of Democrats voters in the first state = 0.48
# P2 = The proportion of Republican voters in the second state = 0.47
# 1-P2 = The proportion of Democrats voters in the second state = 0.53
# p1 = The proportion of Republican voters in the sample from the first state
# p2 = The proportion of Republican voters in the sample from the second state
# The number of voters sampled from the first state (n1) = 100, 
# The number of voters sampled from the second state (n2) = 100


# In[5]:


n1, n2 = 100, 100
P1 = 0.52
P2 = 0.47 

a = n1*P1 
b = n1*(1 - P1) 
c = n2*P2  
d = n2*(1 - P2)  

print(a)
print(b)
print(c)
print(d)


# In[6]:


import math
# Find the standard deviation of the difference.
σd  = math.sqrt( (P1*(1 - P1) / n1 ) + ( P2*(1 - P2) / n2 ) )
 
round(σd, 5)


# In[ ]:


P(z <=0.7082) = 0.24

#Using Stat Trek's <a href ='https://stattrek.com/Tables/Normal.aspx
the probability of a z-score being -0.7082 or less is 0.24



Therefore, the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is 0.24.


# In[ ]:


#Problem 3
You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard
get_ipython().set_next_input('deviation is 209. How well did you score on the test compared to the average test taker');get_ipython().run_line_magic('pinfo', 'taker')


# In[7]:


x = 1100
μ = 1026
σ = 209

z = (x-μ) / σ
z


# In[ ]:


Look up your z-value in the z-table to see what percentage of test-takers scored below you. A z-score of .354 is .1368 + .5000* = .6368 or 63.68%

