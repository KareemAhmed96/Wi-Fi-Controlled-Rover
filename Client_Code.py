import socket
import machine

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.43.182'
port = 333

clientsocket.connect((host, port))

Motor_L_ClockWise		= machine.Pin(5, machine.Pin.OUT)
Motor_L_C_ClockWise 	= machine.Pin(4, machine.Pin.OUT) 

Motor_R_ClockWise		= machine.Pin(0, machine.Pin.OUT)
Motor_R_C_ClockWise 	= machine.Pin(2, machine.Pin.OUT)

while True:
	message = clientsocket.recv(1024)
  	
	if(message.decode('utf-8') == 'up'):
		print(message.decode('utf-8'))
		Motor_L_ClockWise.value(1)
		Motor_L_C_ClockWise.value(0)
		Motor_R_ClockWise.value(0)
		Motor_R_C_ClockWise.value(1)
  		
  	if(message.decode('utf-8') == 'right'):
		print(message.decode('utf-8'))
		Motor_L_ClockWise.value(0)
		Motor_L_C_ClockWise.value(1)
		Motor_R_ClockWise.value(0)
		Motor_R_C_ClockWise.value(1)
  		
  	if(message.decode('utf-8') == 'left'):
  		print(message.decode('utf-8'))
		Motor_L_ClockWise.value(1)
		Motor_L_C_ClockWise.value(0)
		Motor_R_ClockWise.value(1)
		Motor_R_C_ClockWise.value(0)
  		
  	if(message.decode('utf-8') == 'down'):
  		print(message.decode('utf-8'))
		Motor_L_ClockWise.value(0)
		Motor_L_C_ClockWise.value(1)
		Motor_R_ClockWise.value(1)
		Motor_R_C_ClockWise.value(0)
  		
  	if(message.decode('utf-8') == 'key-up'):
  		print(message.decode('utf-8'))
		Motor_L_ClockWise.value(0)
		Motor_L_C_ClockWise.value(0)
		Motor_R_ClockWise.value(0)
		Motor_R_C_ClockWise.value(0)
		
	#clientsocket.close()