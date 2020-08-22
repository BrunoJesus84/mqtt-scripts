import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
#broker_address="192.168.1.73" 
cont = True
while(cont):	
	broker_address="broker.hivemq.com"
	print("creating new instance")
	client = mqtt.Client("B1") #create new instance
	client.on_message = on_message #attach function to callback
	print("connecting to broker")
	client.connect(broker_address) #connect to broker
	print("...")
	topic = input("Enter the topic to subscribe: " )
	client.loop_start() #start the loop
	print("Subscribing to topic:",topic)
	client.subscribe(topic)
	print("...")
	#print("Publishing message to topic",topic)
	#client.publish(topic,"Temperature X")
	time.sleep(10) # wait
	client.loop_stop() #stop the loop
	opc = input("Continue to Subscribing (Y/n): ")
	if ((opc=="n") or (opc=="N")):
		cont = False
		print("Connection finished.")
