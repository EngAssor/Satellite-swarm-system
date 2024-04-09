import socket
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

send_g  = 2
rec_g = 3
send_s  = 22
rec_s = 17
conn = 27
#Send_g
#GPIO.setup(send_g,GPIO.OUT,initial=GPIO.LOW)
#REC_G
#GPIO.setup(rec_g,GPIO.OUT,initial=GPIO.LOW)
#SEND_S
GPIO.setup(send_s,GPIO.OUT,initial=GPIO.LOW)
#RECE_s
GPIO.setup(rec_s,GPIO.OUT,initial=GPIO.LOW)
#conn
GPIO.setup(conn,GPIO.OUT,initial=GPIO.LOW)

command=''
def Swarm_from_base_to_swarm():
    GPIO.output(conn, GPIO.LOW)
    print('Waiting For Ground Station Connection to be Established... ')
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    
    client_socket = socket.socket()# instantiate
    
    client_socket.connect(('192.168.1.2', port))  # connect to the server
    print("Connection from Ground Station is Established Successfully ✔ ")
    GPIO.output(conn, GPIO.HIGH)
    print('Sending The Beacon...')
    Swarm_Beacon = 'The Swarm Satellite Beacon'  # take input
    client_socket.send(Swarm_Beacon.encode())
    print('The Beacon is Sent Successfully ✔ ')
    global command
    while True:
        GPIO.output(send_g, GPIO.LOW)
        print('Waiting For Ground Station Command...')
        command = client_socket.recv(1048576).decode()
        print('Received Command From Ground Station Successfully ✔')
        GPIO.output(rec_g,GPIO.HIGH)
        time.sleep(0.5)
        #ack=command[0:33]
        #ack=ack+'11111111'
        print('Sending The Swarm Satellite Acknowledge... ')
        GPIO.output(rec_g, GPIO.LOW)
        #client_socket.send(' The Swarm Acknowledge'.encode())
        print('The Swarm Satellite Acknowledge Sent Successfully ✔')
        print('Establishing Connection With Satellite...')
        Data_Recevied_From_Satellite = Swarm_from_swarm_to_sat()
        print('Sending Data To Ground Station...')
        GPIO.output(rec_s, GPIO.LOW)  
        GPIO.output(send_g, GPIO.HIGH) 
        if command[33:41] == '00001001':
            pass
            #with open('newnew.jpg','wb') as bih:
            #   bih.write(Data_Recevied_From_Satellite)
            #with open('newnew.jpg','rb') as ic:
            #   pppp=ic.read()
            #size=len(pppp)
            #st=str(size)
            #client_socket.send(st.encode())
            #prime=[2,3,5,7]
            #done=bytearray(prime)
            #print(type(done))
            #client_socket.send(done)
            #client_socket.sendall(pppp)
            

        else:
            #print('sdijgoiegioewgh')

            client_socket.send(Data_Recevied_From_Satellite.encode())
        print('Data Sent Successfully ✔')

    client_socket.close()  # close the connection
noa=''

def Swarm_from_swarm_to_sat():
    # get the hostname
    global noa
    host = socket.gethostname()
    GPIO.output(send_s, GPIO.HIGH)   
    port = 1234  # initiate port no above 1024 
    server_socket = socket.socket()
    try:# look closely. The bind() function takes tuple as argument
        os.system('sudo kill -9 $(sudo lsof -t -i:1234)')
    except:
        pass# get instance
    
    os.system('sudo kill -9 $(sudo lsof -t -i:1234)')

    noa=server_socket.bind(('192.168.1.6', port))
    try:# look closely. The bind() function takes tuple as argument
        os.system('sudo kill -9 $(sudo lsof -t -i:1234)')
    except:
        pass
    if noa=='':
        try:
            os.system('sudo kill -9 $(sudo lsof -t -i:1234)')
            noa=server_socket.bind(('192.168.1.6', port))  # bind host address and port together
        except:
            pass
        while noa=='' :
            try:
                noa=server_socket.bind(('192.168.1.6', port))  # bind host address and port together
            except:
                pass
    else :
        pass
        # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection From Satellite is Established At : " + str(address))
    Satellite_Beacon = conn.recv(1048576).decode()
    print('Recevied Beacon From Swarm Satellite : '+Satellite_Beacon)
    #while True:

    #x = GUI()
    # receive data stream. it won't accept data packet greater than 1024 bytes
    print('Sending The Ground Station Command...')
    conn.send(command.encode())  # send data to the client
    print('Ground Station Command Sent Successfully ✔')
    print('Waiting For Satellite Acknowledge...')
    Satellite_Acknowledge  = conn.recv(1048576).decode()
    print('Received Acknowledge From Satellite Successfully ✔')
    print('Waiting For Data From Satellite...')
    if command[33:41] == '00001001':
        Satellite_Data_Response =''
    else:
        Satellite_Data_Response = conn.recv(1048576).decode()
    #print(Satellite_Data_Response)
        GPIO.output(send_s, GPIO.LOW)  
        GPIO.output(rec_s, GPIO.HIGH) 
    print('Data Recevied Successfully ✔')  
    return Satellite_Data_Response

    conn.close()  # close the connection

if __name__ == '__main__':
    Swarm_from_base_to_swarm()
