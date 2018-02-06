## **EE 250L Spring 2018 Lab 04 Part 2**

In part 2, we will switch over to the UDP protocol and communicate between your
VM and your Raspberry Pi over the Wireless Local Area Network (WLAN) using
sockets. Every machine/device typically has a single IP address. To send packets 
to a specific process on a machine, you would have to use ports at the transport
layer (or L4). The example we will run here will illustrate how this works.

Read through the scripts in the directory. Open up two terminals in your VM and 
run both the server scripts, each in a different terminal:

    python3 udpServer1.py
    python3 udpServer2.py

Question 1: What happens when you run both server scripts?

Stop any running instances of the server scripts by clicking anywhere inside the
terminal window to bring it into focus and pressing `Ctrl+c`. This sends the 
SIGINT signal to the process to tell it to stop.

Edit the two server scripts to listen in on two different ports in the 9000 
range. This is an uncommon range of ports, so they should all be free. Run both 
server scripts. Then, open a third terminal and run the client script 
(`python3 udpClient.py`). In the terminal running the client script, send 
messages to the two different processes by varying the destination port for each
message.

Now, we'll run the code on two separate machines (your VM and rpi). Don't worry 
about pushing any of your changes. We'll do this manually. Login to your 
rpi and clone this repository under a directory with a lab partner's name 
(remember, this step is important because the rpis may be used by someone else!).
`cd` into this directory. Since we did NOT push our changes, you will have to
use a text editor to change the IP addresses and port numbers on the two 
different server scripts. To find the LAN IP addresses of your VM and 

Once you are finished, run the first server, `python3 udpServer1.py`. In your VM,
open up another terminal and initiate another SSH session with your rpi. `cd`
into this directory and `python3 udpServer2.py`.

On your VM:

 1)Open a terminal and run udpClient.py



