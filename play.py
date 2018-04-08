#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
 
import pygame

import Adafruit_TCS34725
import smbus
# Use BCM GPIO references
# instead of physical pin numbers

pygame.mixer.init()

toto = pygame.mixer.music.load("toto.mp3")

#pygame.mixer.music.play()




def CheckColor():
    tcs = Adafruit_TCS34725.TCS34725()
    tcs.set_interrupt(False)

    r, g, b, c = tcs.get_raw_data()

    color_temp = Adafruit_TCS34725.calculate_color_temperature(r, g, b)

    lux = Adafruit_TCS34725.calculate_lux(r, g, b)

    if color_temp is None:
        color_temp = 0
    
    tcs.set_interrupt(True)
    tcs.disable()
    return r, g, b, c, lux, color_temp

def DetermineColor():
    r, g, b, c, lux, color_temp = CheckColor()
    if color_temp > 0:
        return 0

    if r > g and r > b:
        return 1
    elif g > r and g > b:
        return 2
    else:
        return 2

    



GPIO.setmode(GPIO.BCM)
    
    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [14,23,24,25]
    
    # Set all pins as output
for pin in StepPins:
  #print "Setup pins"
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)    
    
    # Define advanced sequence
    # as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
       
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

x = 5
# Read wait time from command line
if x!=0:
    WaitTime = int(x)/float(1000)
else:
    WaitTime = 10/float(1000)

# Initialise variables
StepCounter = 0


muzakplaying = True
started = True


col = DetermineColor()


if muzakplaying:
    if muzakplaying and started:
        if col == 1:
            pygame.mixer.music.load("rick.mp3")
            pygame.mixer.music.play()
            print 'Now Playing: [ Rick Astley - "Never Gonna Give You Up" ]'
            started = True
        elif col == 2:
            pygame.mixer.music.load("toto.mp3")
            print 'Now Playing: [ Toto - "Africa" ]'
            pygame.mixer.music.play()
            started = True 
    if muzakplaying and started:
        pygame.mixer.unpause()
    else:
        col = 0
        pygame.mixer.pause()

while True:
    if col != 0:
        muzakplaying = True
        for pin in range(0,4):
          xpin=StepPins[pin]# Get GPIO
          if Seq[StepCounter][pin]!=0:
            #print " Enable GPIO %i" %(xpin)
            GPIO.output(xpin, True)
          else:
            GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (StepCounter>=StepCount):
          StepCounter = 0
        if (StepCounter<0):
          StepCounter = StepCount+StepDir

        # Wait before moving on
        time.sleep(WaitTime)