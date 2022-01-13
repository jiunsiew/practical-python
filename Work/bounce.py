# bounce.py
#
# Exercise 1.5
height = 100 # meters
reboundRate = 0.6
nBounces = 10

for iB in range(nBounces):
    height = height*reboundRate
    print(round(height, 4))