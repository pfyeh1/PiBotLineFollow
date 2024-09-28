###############################
#  PiBot Line Following 
#  Davis MT
#  28.02.2020
###############################

# import libraries 
import RPi.GPIO as gpio
import time

# set pin mapping to BOARD
gpio.setmode(gpio.BOARD)

# turn off channel warnings messages
gpio.setwarnings(False)

# Set GPIO pins as output
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

# set GPIO pins as inputs
leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor, gpio.IN)
gpio.setup(rightSensor, gpio.IN)

# turn on left motor
def leftOn():
    gpio.output(15, 1)

# turn off left motor
def leftOff():
    gpio.output(15, 0)

# turn on right motor
def rightOn():
    gpio.output(13, 1)

# turn off right motor
def rightOff():
    gpio.output(13, 0)

# turn off all motors
def stopAll():
    gpio.output(13, 0)
    gpio.output(15, 0)

# main program loop
try:
    stopAll()  # ensure all motors are off at start
    
    while True:
        # Read sensor values
        left_val = gpio.input(leftSensor)
        right_val = gpio.input(rightSensor)
        
        # if left and right sensors are off, stop both motors
        if left_val == 0 and right_val == 0:
            stopAll()
        
        # if both sensors are on, turn both motors on
        elif left_val == 1 and right_val == 1:
            leftOn()
            rightOn()
        
        # if left sensor is on, pivot left
        elif left_val == 1 and right_val == 0:
            leftOn()
            rightOff()
        
        # if right sensor is on, pivot right
        elif left_val == 0 and right_val == 1:
            leftOff()
            rightOn()
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Program interrupted by user.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure motors are stopped and GPIO is cleaned up
    stopAll()
    gpio.cleanup()
    print("GPIO cleanup complete. Motors stopped.")
