# Cardboard Player 3000 #

## Motivation ##

This is an entry for CreatED 2018 Hardware Hackathon in Edinburgh. I had two goals with it - introduce hackathons and programming to my girlfriend and play with basic sensors and modules available for Rasberry Pi. The record player was simple enough to make while still having multiple very different parts to play around with.

## Parts ##

* Adafruit TCS34725 RGB Sensor
* 5 V Stepper Motor
* Motor Driver 
* Jumper Wires
* Raspberry Pi 3B 
* Cardboard

## Hardware Set-Up ##

~~~ Diagram Here ~~~ 

## Software Set-Up ##

    Libraries used:
    """
    adafruit_tcs34725
    pygame
    smbus
    """ 

smbus and pygame should already be in a Raspbian install, therefore all we need is:

    """
    pip install adafruit_tcs34725
    """

then to test if the sensor is correctly connected (point it at something with a clear color preferably):

    """
    python testsensor.py
    """

test motor (it just spins it):

    """
    testmotor.py
    """

observe the LEDs flashing as they indicate the sequence the commands are being passed in. If they do not go in order, some GPIOs might be mismatched.

Before running play.py, make sure to provide your own toto.mp3 and rick.mp3, as I am not allowed to share these in the repository for obvious reasons.

## Improvement TODOs ##

* Script runs constantly (No need to restart)
* Color checks after song started (React to "needle" being moved away from the "record")
* More realistic "record" behaviour: wind-up, alternating speeds of audio, scratch sound when removing needle
* Continue the song where it left off if needle was moved and placed back on the same color
* Detect more colors
* Physical buttons
* Streaming current music choice to a web app (Websockets?)
* Speakers
* Tidier design

