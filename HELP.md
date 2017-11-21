
TIMELAPSE
===
timelapse utility for raspberry pi camera
---

# DESCRIPTION

Created on Sun Nov 5 10:22:44 2017 
@author: Stein Castillo
*****************************************
           Lapse Image Camera          
                 V1.0                  
*****************************************
    
**Requirements:** 
* [image magick](https://www.theurbanpenguin.com/image-manipulation-on-the-raspberry-pi-using-imagemagick/) installed and working 

**Usage:** 
* python timelapse.py -c <conf.json> 
* python timelapse.py --conf <conf.json> 

# CLASSES
Sensor

class Sensor
   Reads the SenseHat sensors and stores the values 
   in class attributes
       
   Attributes:
   -----------
   temperature: float 
   pressure: float
   humidity: float
   
   Methods defined here:
   
   __init__(self, hat=False)
   
   flashOff(self)
   Turn the Sense Hat display OFF
   
   flashOn(self, color='w')
   Turn the Sense Hat display ON
   
   Parameters:
   -----------
   color: {"w", "r"}
   
   Returns:
   --------
   None
   Uses the Sensehat display as a flash to take pictures
   in low light conditions.
   'w': White light (default)
   'r': Red light
   
   update(self)
   Read the SenseHat sensors
   Temperature reading is corrected for CPU heat effect

# FUNCTIONS
msg_out(typ='I', msg='null')
    prints a formated message to the console
    depending on the type of message a color will be assigned
    when presenting the message
    
Parameters
----------
typ : {'I', 'W', 'A', 'E', 'C', 'S'}
    Message type
msg : str
    Message contents
Returns
-------
Formatted message to the console
* 'I': Info - Green 
* 'W': Warning - Yellow 
* 'A': Alarm - Red 
* 'E': Error - Red 
* 'C': Command - Yellow 
* 'N': Note - Cyan 
    
