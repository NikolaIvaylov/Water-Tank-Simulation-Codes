import math
from numpy import linspace,sin,pi,int16
import numpy as np
from pylab import plot,show,axis
from matplotlib import pyplot as plt

#Variables you can play with:
#Time:
t_step = 0.01 #s
n = 3000 #number of steps
#Cylinder Tank:
rc = 1 #radius (m)
hc = 30 #height (m)
Pf = 100 #What % of the tank is full?
#Water:
vin = 1 #speed of water flowing in (m/s)
#Holes:
rin = 0.1 #inlet radius (m)
rout = 0.3 #outlet radius (m)

#Other variables (that you cannot play with):
#Time:
t = np.linspace(0, (n*t_step), n) #generate x-axis values
#Cylinder
Ab = np.pi*(rc**2) #base area (m^2)
#Water Variables:
#Water:
h0 = hc*(Pf/100) #initial water level (m)
vout = math.sqrt(2*6.67408*h0) #speed of water flowing out (m/s)
#Holes:
Ain = np.pi*(rin**2) #inlet cross-sectional area (m^2)
Aout = np.pi*(rout**2) #outlet cross-sectional area (m^2)
Qin = Ain*vin #rate of water flowing in (m^3/s)
Qout = Aout*vout #rate of water flowing out (m^3/s)
#Other:
water_heights = [] #heights values for the y-axis
water_heights.append(h0) #add initial water level

#Euler's Method:
for time in range(1, len(t)):
    previous_height = water_heights[time-1] #get h(n-1)
    vout = math.sqrt(2*6.67408*previous_height) #recalculate vout(h(n-1))
    Qout = Aout*vout #recalculate Qout with the new vout(h(n-1))
    current_water_height = previous_height+((Qin-Qout)/Ab)*t_step #h(n) = h(n-1) + (the change in height)*(time step)
    water_heights.append(current_water_height) #add the value of the current height to the y-axis
     
#Making sure that the numbers are within the cylinder's parameters:
    if water_heights[time] < 0:
        water_heights[time] = 0
    elif water_heights[time] > hc:
        water_heights[time] = hc

#Displaying the graph:        
water_heights = np.array(water_heights)
plt.figure(dpi=300) 
plt.title(f"Euler's Method (step={t_step})")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.plot(t, water_heights, color="blue")
plt.plot(t, np.zeros(len(t)) , color="gray")
plt.show()
