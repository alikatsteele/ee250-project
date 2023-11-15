import sys
import time
import requests
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *


grovepi.set_bus("RPI_1")

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    Temp_Humid = 4   # D4, temperature and humidity sensor
    LightSens = 0 #A0, light sensor
    SoundSens = 1 #A1, sound sensor

    url = 'https://172.233.154.180:3000'

    grovepi.pinMode(Temp_Humid, "INPUT") #setting sensor to an input
    grovepi.pinMode(LightSens, "INPUT") #setting sensor to an input
    grovepi.pinMode(SoundSens, "INPUT") #setting sensor to an input
    time.sleep(1) #pause to give the grovepi a secd

    while True:
        #So we do not poll the sensors too quickly
        #sleep for a reasonable time of 500ms between each iteration.
        time.sleep(0.5)

        #get temperature and humidity measurement
        [temp,humidity] = grovepi.dht(Temp_Humid,0)

        #get light sensor value
        light = grovepi.analogRead(LightSens)

        #get sound sensor value
        sound = grovepi.analogRead(SoundSens)

        myobj = {'temperature': temp, 'humidity': humidity, 'light':light, 'sound':sound}

        x = requests.post(url, json = myobj)





        
