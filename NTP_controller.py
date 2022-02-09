# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:06:06 2022

@author: David Giancola
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# enter desired set temperature #
#T_set = input(("Enter set Temperature in Celsius: ")) # in deg C
T_set = 373

# import sample data
filePath = './'
fileName = 'sample_temp_data.csv' ### this will be replaced with actual temp from arduino
df = pd.read_csv(filePath + fileName)

# extract actual temperature, time reading
T_actual = np.array(df['temp'])
time = np.array(df['time'])

# set prop, int, and deriv gains
Kp = .8
Ki = .25
Kd = .1

# set time step
dt = .1

# begin PID math
I = 0

error = T_set - T_actual
P = Kp * error
I = I + (error * Ki * dt)
D = (Kd / dt) * (error - error)

u = P + I + D

# plotting PID output vs time
plt.figure(figsize=(6,5), facecolor='white')
plt.plot(time,u,'bo')
plt.xlabel(r'time in sec')
plt.ylabel(r'PID output in K')

# extract actual servo location
filePath = './'
fileName = 'sample_servo_data.csv'
df = pd.read_csv(filePath + fileName)

X_actual = np.array(df['position'])

newPos = [60]

# define transfer function between K and deg
def kelvin2degree(u,X_actual):

    delPos = X_actual * .15;        # 15 percent change in current deflection
    
    if u > 0:
        newPos = X_actual - delPos
    elif u < 0:
        newPos = X_actual + delPos
    else:
        newPos = X_actual
        return newPos

# plotting TF output vs time
# plt.figure(figsize=(6,5), facecolor='white')
# plt.plot(time,newPos,'bo')
# plt.xlabel(r'time in sec')
# plt.ylabel(r'TF output in deg')        