# **EE 250L Spring 2018 Lab 04 Part 3**

In part 3, we will send sensor data from your rpi to your VM, and turn on and 
off a GrovePi LED connected to your rpi from your VM. In part 1 and 2, we 
covered enough material to give you the tools to accomplish this last task on
your own. 

## **Step 1**

`cd` into the GrovePi-EE250/Script/ folder and run

    sudo bash grovepi_python3_install.sh
    sudo bash install.sh

Then, `cd` to GrovePi-EE250/Software/Python/ and play with the 
`grove_ultrasonic.py` and `grove_led_blink.py` scripts to figure out how to 
interact with the GrovePi sensors.

## **Step 2**

Your challenge has two parts. Each part can be done using separate pairs of
processes. That is, it will be easier to have two processes running on your VM 
and two processes running on your rpi. We have provided 4 skeleton files for you.

#### The First Pair (UDP/Ultrasonic):

Stream the distance output from the ultrasonic sensor from your rpi to your 
VM every 100ms using UDP. We can use UDP here because we're not too worried 
about lost packets.

RangeFinder >>>> GrovePi >>>> Router >>>> VM

#### The Second Pair (TCP/LED):

Using a TCP socket to increase reliability, code an application where 
you can control an LED attached to the GrovePi from your VM. Your application 
should turn on the LED when you send the string "LED_ON" and turn off the LED 
when you send the string "LED_OFF" to the rpi. You will not be graded for error 
control, but it would be good practice to code the rpi to respond to each 
message indicating whether the LED has been turned on/off or the command was not
understood.

"LED_ON" >>>> Router >>>> GrovePi >>>> LED



