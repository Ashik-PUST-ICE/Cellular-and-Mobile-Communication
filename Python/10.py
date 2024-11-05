import math

# Given constants
R = 1.387  # Cell Radius in km
n = 4      # Number of cells
N = 60     # Total number of channels
area = round(2.5981 * R**2)  # Area covered per cell in sq km
C = N / n  # Number of channels per cell
A = 9      # Traffic intensity at C=15, GOS=0.05, Au=0.029

# Question (a)
Au = 0.029  # Traffic per user
U = A / Au  # Number of users
U_per = U / area  # Number of users per square km

print(f"(a) Number of users per square km: {int(U_per)} users/sq km\n")

# Question (b)
lamda = 1  # Lambda = 1 call/hour
H = (Au / lamda) * 3600  # Holding time in seconds
t = 10  # Time in seconds
Prb = math.exp(-(C - A) * t / H)  # Probability that a delayed call will wait more than t seconds

print(f"(b) The probability that a delayed call will have to wait: {Prb * 100:.2f}%\n")

# Question (c)
Prc = 0.05 * Prb  # Probability that a call is delayed more than 10 seconds
print(f"(c) The probability that a call will be delayed: {Prc * 100:.2f}%\n")



# Problem-10: A hexagonal cell within a 4-cell system has a radius of 1.387 km. A total of 
# 60 channels are used within the entire system. If the load per user is 0.029 Erlangs, and λ= 
# call/hour, compute the following for an Erlang C system that has a 5% probability of a 
# delayed call- 
# a) How many users per square kilometer will this system support? 
# b) What is the probability that a delayed call will have to wait for more than 10s? 
# c) What is the probability that a call will be delayed for more than 10 seconds?