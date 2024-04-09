import socket
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import smbus
import time

# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)


 
   

command=''
lcd_init()
def Swarm_from_base_to_swarm():
    
    print('Waiting For Ground Station Connection to be Established... ')
    lcd_string("Wating ...      ",LCD_LINE_1)
    lcd_string("for connction   ",LCD_LINE_2)
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    
    client_socket = socket.socket()# instantiate
    
    client_socket.connect(('192.168.1.2', port))  # connect to the server
    print("Connection from Ground Station is  ✔ ")
    lcd_string("Connection  Done",LCD_LINE_1)
    lcd_string("  Successfully  ",LCD_LINE_2)
    print('Sending The Beacon...')
    Swarm_Beacon = 'The Swarm Satellite Beacon'  # take input
    client_socket.send(Swarm_Beacon.encode())
    print('The Beacon is Sent Successfully ✔ ')
    global command
    while True:
        print('Waiting For Ground Station Command...')
        lcd_string("Satellite  is   ",LCD_LINE_1)
        lcd_string("   Waiting ...  ",LCD_LINE_2)
        command = client_socket.recv(1048576).decode()
        print('Received Command From Ground Station Successfully ✔')
        lcd_string("Received Command",LCD_LINE_1)
        lcd_string("From Station    ",LCD_LINE_2)
        #ack=command[0:33]
        #ack=ack+'11111111'
        print('Sending The Swarm Satellite Acknowledge... ')
        
        #client_socket.send(' The Swarm Acknowledge'.encode())
        print('The Swarm Satellite Acknowledge Sent Successfully ✔')
        print('Establishing Connection With Satellite...')
        Data_Recevied_From_Satellite = Swarm_from_swarm_to_sat()
        print('Sending Data To Ground Station...')
        lcd_string("Sending Data",LCD_LINE_1)
        lcd_string("To Station  ",LCD_LINE_2)
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
    lcd_string("Connected to the",LCD_LINE_1)
    lcd_string("   Satellite    ",LCD_LINE_2)
    global noa
    host = socket.gethostname()   
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
    print('Ground Station Command  Successfully ✔')
    lcd_string("Command Sent    ",LCD_LINE_1)
    lcd_string("   Successfully ",LCD_LINE_2)
    print('Waiting For Satellite Acknowledge...')
    Satellite_Acknowledge  = conn.recv(1048576).decode()
    print('Received Acknowledge From Satellite Successfully ✔')
    print('Waiting For Data From Satellite...')
    if command[33:41] == '00001001':
        Satellite_Data_Response =''
    else:
        Satellite_Data_Response = conn.recv(1048576).decode()
    #print(Satellite_Data_Response)
        
    print('Data Recevied Successfully ✔')  
    return Satellite_Data_Response

    conn.close()  # close the connection

if __name__ == '__main__':
    Swarm_from_base_to_swarm()
