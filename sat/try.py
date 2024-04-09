import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
send_g  = 2
rec_g = 3
send_s  = 22
rec_s = 17
conn = 27
#Send_g
GPIO.setup(2,GPIO.OUT,initial=GPIO.LOW)
#REC_G
GPIO.setup(3,GPIO.OUT,initial=GPIO.LOW)
#SEND_S
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)
#RECE_s
GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)
#conn
GPIO.setup(27,GPIO.OUT,initial=GPIO.LOW)
while True :
   time.sleep(1)
   GPIO.output(send_g, GPIO.LOW)
   GPIO.output(conn, GPIO.HIGH)
   time.sleep(1)
   GPIO.output(rec_g,GPIO.HIGH)
   time.sleep(2)
   GPIO.output(rec_g, GPIO.LOW)
   time.sleep(1)
   GPIO.output(send_s, GPIO.HIGH)   
   time.sleep(2)
   GPIO.output(send_s, GPIO.LOW)  
   GPIO.output(rec_s, GPIO.HIGH) 
   time.sleep(2)
   GPIO.output(rec_s, GPIO.LOW)  
   GPIO.output(send_g, GPIO.HIGH)
    
