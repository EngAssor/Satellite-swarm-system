import socket
import os
import sys
#import schedule
import time

x=''
y=0
def client_program():
    global x
    global y
    if y==0:
        print('Waiting For Swarm Satellite Connection to be Established... ')
    #while True:

    host = socket.gethostname()  # as both code is running on same pc
    port = 7000  # socket server port number

    client_socket = socket.socket()  # instantiate
    try :
        x=client_socket.connect(('192.168.1.3', port))  # connect to the server
    except:
        pass
    while x=='':
        try:
            x = client_socket.connect(('192.168.1.3', port))  # connect to the server
        except:
            pass


    if x==None:
        try:

            message = 'The Satellite Beacon'

            client_socket.send(message.encode())
            command = client_socket.recv(1024).decode()
            print("Connection from Swarm Satellite is Established Successfully ✔ ")
            print('Sending The Satellite Beacon...')
            print('Satellite Beacon Sent Successfully ✔')
            print('Waiting For Command...')

            print('Received From Swarm Satellite : ' + command)# receive response
            #message = input(" -> ")  # again take input
            print('Sending Acknowledge...')
            ack=command[0:33]
            ack=ack+'11111111'
            client_socket.send(ack.encode())
            print('Acknowledge Sent Successfully ✔ ')
            print('Executing The Command...')
            #gg=get_Comannd_Sub()
            print('Command Executed Successfully ✔')
            print('Sending Data...')
            y+=1
            if command == 'koko':

                with open('newnew.jpg', 'rb') as rr:
                    s = rr.read()
                client_socket.send(s)
            else:
                client_socket.send(gg.encode())
            # show in terminal
            print('Data Sent Successfully ✔')
            print('Waiting For Swarm Satellite Connection to be Established...')
        except:
            pass
          # again take input
    client_socket.close()
    #client_socket.shutdown(client_program())
    #print('closeee')
    #x = client_socket.connect(('192.168.1.3', port))
#schedule.every(0.1).seconds.do(client_program)
while True:
    client_program()
    #time.sleep(1)

#client_socket.close()  # close the connection

#if __name__ == '__main__':
 #   client_program()
