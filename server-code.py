#TCP Server

import socket
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(1)

#creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#host = socket.gethostbyname()
host = '192.168.43.182'
port = 444

#binding to socket
serversocket.bind((host, port))

print('Waiting for Connection')
#Starting TCP listener
serversocket.listen(3)

#Starting the connection
clientsocket, address = serversocket.accept()
    
print('Recieved Connection from %s' % str(address))

while True:
    
    events = pygame.event.get()

    for event in events:
          
        if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_LEFT:
                    message="left"
                    print(message)
                    clientsocket.send(message.encode('utf-8'))

                if event.key ==  pygame.K_RIGHT:
                    message="right"
                    print(message)
                    clientsocket.send(message.encode('utf-8'))

                if event.key ==  pygame.K_UP:
                    message="up"
                    clientsocket.send(message.encode('utf-8'))
                    print(message)

                if event.key ==  pygame.K_DOWN:
                    message="down"
                    print(message)
                    clientsocket.send(message.encode('utf-8'))
                    
        if event.type == pygame.KEYUP:
            message='key-up'
            clientsocket.send(message.encode('utf-8'))
            print(message)
    #clientsocket.close()
