import math
from numpy import linspace,sin,pi,int16
import numpy as np
from pylab import plot,show,axis
from matplotlib import pyplot as plt

#Variables you can play with:
#Time:
t_step = 1 #s
n = 300 #number of steps
#Cylinder Tank:
rc = 2 #radius (m)
hc = 30 #height (m)
Pf = 100 #What % of the tank is full?
#Water:
vin = 1 #speed of water flowing in (m/s)
#Holes:
rin = 0.1 #inlet radius (m)
rout = 0.2 #outlet radius (m)
#RK constants:
a2 = 1/2 #can also be 1/2

#Other variables (that you cannot play with):
#Time:
t = np.linspace(0, (n*t_step), n) #generate x-axis values
t_step=t_step #correct t_step back to initial value
#Cylinder
Ab = np.pi*(rc**2) #base area (m^2)
#Water Variables:
#Water:
h0 = hc*(Pf/100) #initial water level (m)
vout = math.sqrt(2*9.81*h0) #speed of water flowing out (m/s)
#Holes:
Ain = np.pi*(rin**2) #inlet cross-sectional area (m^2)
Aout = np.pi*(rout**2) #outlet cross-sectional area (m^2)
Qin = Ain*vin #rate of water flowing in (m^3/s)
Qout = Aout*vout #rate of water flowing out (m^3/s)
#Other:
water_heights = [] #heights values for the y-axis
water_heights.append(h0) #add initial water level
#Runge-Kutta:
a1 = 1-a2 #calculating a1
p1_q11 = 1/(2*a2) #calculating p1 = q11 = 1/(2*a2)

for time in range(1, len(t)):
    previous_height = water_heights[time-1] #get h(n-1)
    vout = math.sqrt(2*9.81*previous_height) #recalculate vout(h(n-1))
    Qout = Aout*vout #recalculate Qout with the new vout(h(n-1))
    k1 = (2*Qin)/Ab #calculating k1
    k2 = -(2*p1_q11*Qout)/Ab #calculating k2
    current_water_height = previous_height+(a1*k1+a2*k2)*t_step #h(n) = h(n-1) + (the change in height)*(time step)
    water_heights.append(current_water_height) #add the value of the current height to the y-axis

#Making sure that the numbers are within the cylinder's parameters:
    if water_heights[time] < 0:
        water_heights[time] = 0
    elif water_heights[time] > hc:
        water_heights[time] = hc
    
#Displaying the graph:
water_heights = np.array(water_heights)
plt.figure(dpi=300) 
plt.title(f"2nd order Runge-Kutta (step={t_step})")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.plot(t, water_heights, color="blue")
plt.plot(t, np.zeros(len(t)) , color="gray")
plt.plot(t, [hc]*len(t) , color="gray")
plt.show()
