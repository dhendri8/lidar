# lidar

**GET TO A WORKING MODEL FIRST - THEN OPTIMIZE**

## Current Rabbit hole

- PNG is supposed to be really small if there are lines with only black.
    - Rob said a few bytes if its a pure black image. 
    - Trying to validate this. 
    - Note: this may be useless if we can't quickly convert raw to png
    - Idea to chase: Apply mask, convert to png, send resulting data. 
    - Research PNG compression, different compression speeds may impact performance

## MUST DO SOMETIME IN THE NEAR FUTURE
1. Figure out how to run the high speed raspiraw thingy
1. Implement a simple version of that guys Laser range finder / scanner dealydoo 


## TODO: 
- ~Figure out how to do the math involved with the range detection thingy~
- figure out how to do the angle detection from this site https://sites.google.com/site/todddanko/home/webcam_laser_ranger 
- Figure out how I can get angle values from my phones gyro into the computer (for doing math thingys)
- Design and build a more robust / more precise mount for the laser / camera. 
    - Mount the whole thing on a tripod
    - Take pics at 1 foot increments from 1 to 10 feet for calibration. 
    - make sure to take these at full size, not small. 