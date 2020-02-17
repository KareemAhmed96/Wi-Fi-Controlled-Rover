# Wi-Fi-Controlled-Rover
Developed using the ESP 8266 NodeMCU (IoT platform) with Python’s bootloader manually flashed on it. 
You need to setup a TCP socket server in order to establish a client/host communication between the PC and the Rover.

The TCP Server is going to be deployed on the PC/Laptop as the host.
Any device with the host's IP address can request to connect to it. Once the connection is established the PC can control the client through the keyboard keys.
