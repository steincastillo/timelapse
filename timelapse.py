#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*****************************************
Created on Sun Nov 5 10:22:44 2017
Edited on 
@author: Stein Castillo

*****************************************
*           Lapse Image Camera          *
*                 V1.0                  *
*****************************************

Requirements:
    image magick installed and working
    https://www.theurbanpenguin.com/image-manipulation-on-the-raspberry-pi-using-imagemagick/
    
Usage: 
    python timelapse.py -c <conf.json>
    python timelapse.py --conf <conf.json> 
*****************************************
"""

# Import libraries

import argparse
import json
import PIL
import pprint
import os
import colorama
from picamera import PiCamera
from datetime import datetime
from time import sleep

# Define classes

class Sensor():
    """Reads the SenseHat sensors and stores the values 
    in class attributes
        
        Attributes:
        -----------
        temperature: float 
        pressure: float
        humidity: float
    """
    def __init__(self, hat=False):
        self.__hat = hat
        self.temperature = 0
        self.pressure = 0
        self.humidity = 0
        # Determine if SenseHat or simulation will be used
        if self.__hat:
            from sense_hat import SenseHat
        else:
            from sense_emu import SenseHat

        # Inatanciate sensehat class
        self.sense = SenseHat()

        # Define sensor hat display colors
        __R = [255, 0, 0]         # Red
        __G = [0, 255, 0]         # Green
        __B = [0, 0, 255]         # Blue
        __W = [255, 255, 255]     # White
        __E = [0, 0, 0]           # Empty/Black

        self.WHITE_FLAG = [
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W,
        __W, __W, __W, __W, __W, __W, __W, __W]
        
        self.RED_FLAG = [
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R,
        __R, __R, __R, __R, __R, __R, __R, __R]
        
    def update(self):
        """
        Read the SenseHat sensors
        Temperature reading is corrected for CPU heat effect
        """
        # Get CPU temperature
        self.__tx = os.popen('/opt/vc/bin/vcgencmd measure_temp')
        self._cputemp = self.__tx.read()
        self.__cputemp = self.__cputemp.replace('temp=','')
        self.__cputemp = self.__cputemp.replace('\'C\n','')
        self.__cputemp = float(self.__cputemp)
        # Read SenseHat temperature sensors
        self.__temp1 = self.sense.get_temperature()
        self.__temp2 = self.sense.get_temperature_from_pressure()
        self.__temp3 = self.sense.get_temperature_from_humidity()
        # Compensate for CPU heat effect
        self.temperature = ((self.__temp1+self.__temp2+self.__temp3)/3)-(self.__cputemp/5)

        # Log humidity
        self.humidity = self.sense.get_humidity()

        # Log atmospheric pressure
        self.pressure = self.sense.get_pressure()
        
    def flashOn(self, color="w"):
        """Turn the Sense Hat display ON
        
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
        """
        self._color = color.lower()
        if self._color == "w":
            self.sense.set_pixels(self.WHITE_FLAG)
        elif self._color == "r":
            self.sense.set_pixels(self.RED_FLAG)

    def flashOff(self):
        """Turn the Sense Hat display OFF"""
        self.sense.clear()

# Define functions
   
def msg_out(typ = "I", msg = "null"):
    """prints a formated message to the console
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
    """
    msg_time = datetime.now().strftime("%I:%M:%S%p")
    
    if typ == "I": mtype = colorama.Fore.GREEN + "[INFO - "
    elif typ == "W": mtype = colorama.Fore.YELLOW + "[WARNING - "
    elif typ == "A": mtype = colorama.Fore.RED +  "[ALARM - " 
    elif typ == "E": mtype = colorama.Fore.RED + "[ERROR - "
    elif typ == "C": mtype = colorama.Fore.YELLOW + "[CMD - "
    elif typ == "N": mtype = colorama.Fore.CYAN + "[NOTE - "
    else: mtype = "[UNKNOWN - "
        
    print (mtype + msg_time + "] " + msg +  colorama.Style.RESET_ALL)

if __name__ == '__main__':
    #construct the command line argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--conf",
                    required=False,
                    help="usage: python3 timelapse.py --conf [file.json]")
    args = vars(ap.parse_args())
    
    if args["conf"] == None:  # Check if a configuration file was provided
        msg_out("I", "No Configuration file provided... Using default settings.")
        cwd = os.getcwd()+"/"
        conf = {"camera_rotation": 0,
                "camera_resolution": [960, 720],
                "camera_rotation": 0,
                "camera_zoom": [0.0, 0.0, 1.0, 1.0],
                "camera_warmup_time": 2,
                "path": cwd,
                "file_root": "pic",
                "lapse": 10}
    elif not os.path.isfile(args["conf"]): # Check if the configuration file exists
        msg_out("E", "Configuration file does not exist... Please verify.")
        exit(0)
    else:
        conf = json.load(open(args["conf"]))
    
    # Set date and time formats
    DATE_FORMAT = "%Y"+"-"+"%m"+"-"+"%d"+"_"+"%H"+":"+"%M"+":"+"%S" #2017-11-05_17:23:15
    TIME_FORMAT = "%H"+":"+"%M"+":"+"%S" #22:11:30
    
    # Instantiate classes
    sensors = Sensor(True)
    camera = PiCamera()
    pp = pprint.PrettyPrinter(indent = 1)
    
    # Main loop
    
    # Print routine header
    print (__doc__)
    print ("******** Settings ********")
    pp.pprint(conf)
    print ("**************************\n")
    
    # Validate path for images
    if not(os.path.isdir(conf["path"])):
        msg_out("E", "Image directory does not exists...")
        exit(0)
           
    # Camera settings
    camera.resolution = conf["camera_resolution"]
    camera.rotation = conf["camera_rotation"]
    camera.zoom = conf["camera_zoom"]
    
    # Initiate image capture loop
    msg_out("I", "Initiating image capture... ctrl+c to interrupt")
    
    while True:    
        
        # Read SenseHat sensors
        msg_out("I", "Reading SenseHat sensors...")
        sensors.update()
        print ("Temperature: {} Celsius".format(round(sensors.temperature, 1)))
        print ("Humidity: {} %".format(round(sensors.humidity, 1)))
        print ("Pressure: {} Hpa".format(round(sensors.pressure, 1)))
        print ("**********************")
        
        # Read system time
        msg_out("I", "Updating capture time...")
        time = datetime.now().strftime(DATE_FORMAT)
        #time = datetime.strftime(time, DATE_FORMAT)
        print (time)
        print ("**********************")
        
        # Capture the picture
        filename = conf["path"] + conf["file_root"] + "_" + time + ".jpg"
        msg_out("I", "Capturing picture: " + filename)
        sensors.flashOn("w")
        camera.start_preview()
        sleep (conf["camera_warmup_time"])
        camera.capture(filename)
        camera.stop_preview()
        sensors.flashOff()
        
        # Image post-processing
        msg_out("I", "Executing image post-processing...")
        # Prepare text overlay for post-processed image
        line1 = "Date : {}".format(time)
        line2 = "Temperature : {} Celsius".format(round(sensors.temperature),1)
        line3 = "Humidity: {}".format(round(sensors.humidity),1)
        line4 = "Pressure: {} Hpa".format(round(sensors.pressure),1)
        filename_out = conf["path"] + "S_" + conf["file_root"] + "_" + time + ".jpg"
        
        # Prepare the Image Magick utility command to add text overlay to the image
        cmd = "convert " + filename + " -background '#0008' -fill white -pointsize 15 "
        cmd = cmd + "-gravity Southwest label:"
        cmd = cmd + "\'"+line1+"\n"+line2+"\n"+line3+" \%"+"\n"+line4+"\' "
        cmd = cmd + "-compose over -composite " + filename_out
        # Add overlay text to the image
        os.popen(cmd)
        
        msg_out ("N", "Standing by for next image capture...")
        print ("**********************")
        sleep(conf["lapse"])
    




