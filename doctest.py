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
    python timelapse.py -c <conf.json> 

******************************************
"""

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
    """
    msg_time = datetime.now().strftime("%I:%M:%S%p")
    
    if typ == "I": mtype = colorama.Fore.GREEN + "[INFO - "
    elif typ == "W": mtype = colorama.Fore.YELLOW + "[WARNING - "
    elif typ == "A": mtype = colorama.Fore.RED +  "[ALARM - " 
    elif typ == "E": mtype = colorama.Fore.RED + "[ERROR - "
    elif typ == "C": mtype = colorama.Fore.YELLOW + "[CMD - "
    elif typ == "S": mtype = colorama.Fore.CYAN + "[NOTE - "
    else: mtype = "[UNKNOWN - "

    print (mtype + msg_time + "] " + msg +  colorama.Style.RESET_ALL)

def msg_out1(typ = "I", msg = "null"):
    """prints a formated message to the console
    depending on the type of message a color will be assigned
    when presenting the message
    
    Args:
    typ : {'I', 'W', 'A', 'E', 'C', 'S'}
        Message type
    msg : str
        Message contents
    Returns:
        Formatted message to the console
    """
    msg_time = datetime.now().strftime("%I:%M:%S%p")
    
    if typ == "I": mtype = colorama.Fore.GREEN + "[INFO - "
    elif typ == "W": mtype = colorama.Fore.YELLOW + "[WARNING - "
    elif typ == "A": mtype = colorama.Fore.RED +  "[ALARM - " 
    elif typ == "E": mtype = colorama.Fore.RED + "[ERROR - "
    elif typ == "C": mtype = colorama.Fore.YELLOW + "[CMD - "
    elif typ == "S": mtype = colorama.Fore.CYAN + "[NOTE - "
    else: mtype = "[UNKNOWN - "

    print (mtype + msg_time + "] " + msg +  colorama.Style.RESET_ALL)
