# Timelapse 

## What does it do?  
Configurable routine that takes pictures at fixed time intervals using the Raspberry Pi (RPi) camera module. 
Optionally, the SenseHat can be used to read the sensors and the display as a flash to iluminate the subject.

Most of the routine parameters are configurable via JSON file. There is no need to change the code. If the JSON file is not 
provided, default parameters will be used.

## What do you need? 
* Raspberry Pi (**Required**) 
* Camera Module (**Required**) 
* SenseHat (Optional) 
* Image Magick (**Required**) 

## How to execute it? 
`python3 timelapse.py --conf <conf.JSON>`
`python3 timelapse.py -c <conf.JSON>`

## JSON file parameters 
a JSOn file can be provided when executing the routine to control the overall behavior. The accepted parameters are:
* warmup_camera_time: 
* camera_resolution 
* timelapse: 
* sensehat: Bool -> True if sensehat is installed. False otherwise 
* xxx 
* xxx 
* xxx 

The <default.json> file provided with this library can be edited to accomodate different requirements.

## What are the defaults parameters? 
If no JSON file is provided when executing the routine, the following parameters will be used by default:
* camera rotation: 0 
* camera resolution: [960, 720] 
* camera_zoom": [0.0, 0.0, 1.0, 1.0] 
* camera_warmup_time": 2 
* path: cwd 
* file_root": "pic" 
* lapse: 10 


## What else do I need to know? 
* As the routine runs, it will display messages on the console to inform of the progress/status of the execution. 
* The routine will run on an infinite loop. to Stop execution pres ctrl+c 
* The images capture are saved on JPEG format 

## Legal stuff
Author: Stein Castillo (stein@americamail.com) 
Version: 1.5.0 
License: Check license.txt for details 
