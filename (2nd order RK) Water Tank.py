import math
from numpy import linspace,sin,pi,int16
import numpy as np
from pylab import plot,show,axis
from matplotlib import pyplot as plt

#Variables you can play with:
#Time:
t_step = 0.5 #s
n = 90 #number of steps
#Cylinder Tank:
rc = 2 #radius (m)
hc = 50 #height (m)
Pf = 100 #What % of the tank is full?
#Water:
vin = 1 #speed of water flowing in (m/s)
#Holes:
rin = 0.1 #inlet radius (m)
rout = 0.1 #outlet radius (m)
#Runge-Kutta:
a2 = 1/2 #can also be 2/3

#Other variables (that you cannot play with):
#Time:
t = np.linspace(0, (n*t_step), n*2) #generate x-axis values
t_step = t_step/2 #correct the time step to its initial value
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
a1 = 1 - a2
p1_q11 = 1/(2*a2)

# Consider a differential equation: dh / dt = ((Qin - Qout) / Ab)t
def dhdt(t, h):
    #Make sure that the numbers are within the cylinder's parameters:
    if h < 0:
        h = 0
    elif h > hc:
        h = hc
    vout = math.sqrt(2*9.81*h) #recalculate vout(h(n-1))
    Qout = Aout*vout #recalculate Qout with the new vout(h(n-1))
    return ((Qin-Qout)/Ab)*t

'''
2th Order Runge-Kutta:
Finds value of h for a given t by using step size t_step
and initial value h0 at t0.
'''
def rungeKutta2nd(t0, h, t_step, tn):
	# Count number of iterations using step size:
	n = round((tn - t0) / t_step)
    
    # Iterate for n number of iterations:
	for i in range(1, n + 1) :
		# Apply 2nd Order Runge-Kutta Formulas to find 
        # next value of h by using the dhdt() function:
		k1 = dhdt(t0, h)
		k2 = dhdt(t0 + p1_q11 * t_step, h + p1_q11 * k1 * t_step)
		# Update next value of h:
		h = h + t_step * (a1 * k1 + a2 * k2)
		# Update next value of t:
		t0 = t0 + t_step
    #return the new water height:
	return h


#2nd Order Runge-Kutta Loop:
for time in range(1, len(t)):
    previous_height = water_heights[time-1] #get h(n-1)
    #Use the rungeKutta2nd() function:
    current_water_height = rungeKutta2nd(0, previous_height, t_step, t[time])
    #Make sure that the numbers are within the cylinder's parameters:
    if current_water_height < 0:
        current_water_height = 0
    elif current_water_height > hc:
        current_water_height = hc
    water_heights.append(current_water_height) #add the value of the current height to the y-axis

#Displaying the graph:        
water_heights = np.array(water_heights)
plt.figure(dpi=300) 
plt.title(f"2nd Order Runge-Kutta (step={t_step*2})")
plt.xlabel("Time (m)")
plt.ylabel("Height (m)")
plt.plot(t, water_heights, color="blue")
plt.plot(t, np.zeros(len(t)) , color="gray")
plt.plot(t, [hc]*len(t) , color="gray")
plt.show()
