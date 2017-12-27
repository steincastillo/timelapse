
#TIMELAPSE

Timelapse Utility for Raspberry Pi Camera
---

##DESCRIPTION

Takes pictures at set intervals. Uses the SenseHat sensor to overlay
enviroment information (pressure, temperature and humidity) and
the SenseHat display as a flash for low light conditions.
    
**Requirements:**
* Raspberrry Pi 
* Raspberry pi Camera
* SenseHat (optional)
* [image magick](https://www.theurbanpenguin.com/image-manipulation-on-the-raspberry-pi-using-imagemagick/) installed and working 
    
**Usage:**
* python timelapse.py -c <conf.json>
* python timelapse.py --conf <conf.json> 

##TECHNICAL DOCUMENTATION

###CLASSES

class Sensor
Operates the Sensehat.

Attributes:  
* temperature: float 
* pressure: float 
* humidity: float 

Methods defined here:

__init__(self, hat=False)
Initializes the Sensor class.

Parameters:  
* hat : Bool 
* True: Use the Sensehat installed on the RPi 
* False: Use the emulator 

flashOff(self)
Turn the Sense Hat display OFF

flashOn(self, color='w')
Turn the Sense Hat display ON

Parameters:
* color: {"w", "r"}

Returns:
* None
.. Uses the Sensehat display as a flash to take pictures
.. 'w': White light (default)
.. 'r': Red light

update(self)
Read the SenseHat sensors
Temperature reading is corrected for CPU heat effect

###FUNCTIONS
msg_out(typ='I', msg='null')
prints a formated message to the console.

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
'I': Info - Green
'W': Warning - Yellow
'A': Alarm - Red
'E': Error - Red
'C': Command - Yellow
'N': Note - Cyan



