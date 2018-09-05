# **EE 250L Spring 2018 Lab 04 Part 3**

In part 3, we will send sensor data from your rpi to your VM, and turn on and 
off a GrovePi LED connected to your rpi from your VM. In part 1 and 2, we 
covered enough material to give you the tools to accomplish this last task with 
little instruction. 

## **Step 1**

The environment inside your rpi needs to be setup for the GrovePi board and the 
firmware in the Atmega328P on the GrovePi board needs to be updated to support
the ultrasonic sensor. Because GrovePi has created very specific scripts with
a lot of hardcoded paths, we will have to run the installation procedure using
their method. First, `cd` to the home directory in your rpi. Then, execute their
installation script:

    sudo curl -kL dexterindustries.com/update_grovepi | bash  

**Please read the output to check if everything was installed successfully 
before moving forward. As a developer, avoiding reading outputs and assuming 
things worked correctly is a bad practice.** The script above clones the main 
GrovePi repo to `~/Dexter/GrovePi/` (do you remember what the tilda means?). 
We'll use that directory to run the firmware update bash script. Change
directory to `~/Dexter/GrovePi/Firmware` and then execute the bash script.

    ./firmware_update.sh

## **Step 2**

Then, `cd` to `GrovePi-EE250/Software/Python/` and play with the 
`grove_ultrasonic.py` and `grove_led_blink.py` scripts to figure out how to 
interact with the GrovePi sensors.

## **Step 3**

Your challenge has two parts. We have provided 4 skeleton files for you.

#### First Program Pair (Ultrasonic Sensor and UDP):

Write a script in the `ultrasonicClient.py` and `ultrasonicServer.py` files
provided to stream the distance output from the ultrasonic sensor connected to 
your rpi to your VM every 110ms using UDP packets. *Note: the firmware loaded 
into the Atmega328P and grovepi.py library has a total call time of 110ms so
you do not need to add any `time.sleep()` calls.* We can use UDP here because 
we're not too worried about lost packets. See below to determine where to run 
each script.

On your VM:

    python3 ultrasonicServer.py

On your RPi:

    python3 ultrasonicClient.py

#### Second Program Pair (LED and TCP):

Using a TCP socket to increase reliability, code an application inside the 
`ledServer.py` and `ledClient.py` files so you can control a Grove LED attached
to the GrovePi from your VM. 

On your RPi:

    python3 ultrasonicServer.py

On your VM:

    python3 ultrasonicClient.py

Your application should turn on the LED when you send the string "LED_ON" from 
your VM to the RPi and turn off the LED when you send the string "LED_OFF" from 
your VM to your rpi. 

Optional: it is always a good practice to insert a feedback mechanism to your 
code to help debug. In this case, having the rpi reply to every message with a 
message such as "LED_ON Success" or "Command not Recognized" will help you see
if your code is working.

**Question 4**: When you submit your assignment, please upload the four python 
scripts in part 4. Additionally, there will be a section to paste a link to
your Github repository.

**Question 5**: DEMO - You will demo both script pairs working simulatenously to
an instructor.
