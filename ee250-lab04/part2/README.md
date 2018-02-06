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

Question 1: What happens when you try to run both server scripts? Copy-paste the 
output into your lab answer sheet.

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
about pushing any of your changes. We'll do this manually using a text editor
on your rpi. Login to your rpi and clone this repository under the directory you 
have been using for the RIOT-EE250 labs. Remember, this step is important 
because the rpis may be used by someone else!

We want to send packets from our VMs over the local area network to the rpi . To
do this, we need the rpi to listen (or bind) to the LAN IPs. On your rpi, find
the LAN IP by typing `ifconfig` in the terminal. We will leave it as an exercise
to figure out which IPv4 address in the output is the LAN address. Write this
IP address down.

In both server scripts, set the `host` variable to the IPv4 address of the rpi.
Also, change the port numbers to be two different nubmers in the 9000s range. 
Once you are finished, run the first server, `python3 udpServer1.py`. In your VM,
open up another terminal and initiate another SSH session with your rpi. `cd`
into this directory and run `python3 udpServer2.py`.

On your VM, change the `host` variable to the IPv4 address of the VM. Use the 
same method you used for the rpi to find the VM's IP address. Note, this will 
NOT be a similar IP address because VirtualBox essentailly turns your host 
OS into another router. When virtual machines are turned on, your host acts like
a router plugged into our class's router (although this is over WiFi instead of
an ethernet cable). Run the `udpClient.py` script and see if you can send 
messages to your rpi.
