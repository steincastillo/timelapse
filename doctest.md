<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="heading">

<tbody>

<tr bgcolor="#7799ee">

<td valign="bottom">   
<font color="#ffffff" face="helvetica, arial">   
<big><big>**doctest**</big></big></font></td>

<td align="right" valign="bottom"><font color="#ffffff" face="helvetica, arial">[index](.)  
[d:\users\stein\raspberry\git\timelapse\doctest.py](file:d%3A%5Cusers%5Cstein%5Craspberry%5Cgit%5Ctimelapse%5Cdoctest.py)</font></td>

</tr>

</tbody>

</table>

<tt>*****************************************  
Created on Sun Nov 5 10:22:44 2017  
Edited on   
@author: Stein Castillo  

*****************************************  
*           Lapse Image Camera          *  
*                 V1.0                  *  
*****************************************  

Requirements:  
    image magick installed and working  
    https://www.theurbanpenguin.com/image-manipulation-on-the-raspberry-pi-using-imagemagick/  

Usage:   
    python timelapse.py -c <conf.json>  
    python timelapse.py -c <conf.json>   

******************************************</tt>

<table width="100%" cellspacing="0" cellpadding="2" border="0" summary="section">

<tbody>

<tr bgcolor="#eeaa77">

<td colspan="3" valign="bottom">   
<font color="#ffffff" face="helvetica, arial"><big>**Functions**</big></font></td>

</tr>

<tr>

<td width="100%">

<dl>

<dt><a name="-msg_out">**msg_out**</a>(typ='I', msg='null')</dt>

<dd><tt>prints a formated message to the console  
depending on the type of message a color will be assigned  
when presenting the message  

Parameters  
----------  
typ : {'I', 'W', 'A', 'E', 'C', 'S'}  
    Message type  
msg : str  
    Message contents  
Returns  
-------  
    Formatted message to the console</tt></dd>

</dl>

<dl>

<dt><a name="-msg_out1">**msg_out1**</a>(typ='I', msg='null')</dt>

<dd><tt>prints a formated message to the console  
depending on the type of message a color will be assigned  
when presenting the message  

Args:  
typ : {'I', 'W', 'A', 'E', 'C', 'S'}  
    Message type  
msg : str  
    Message contents  
Returns:  
    Formatted message to the console</tt></dd>

</dl>

</td>

</tr>

</tbody>

</table>