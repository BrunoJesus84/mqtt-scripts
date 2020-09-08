import paho.mqtt.client as paho #import the client1
#broker_address="192.168.1.73" 
broker = "broker.hivemq.com" #use external broker
port = 1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")            #create client object
client1.on_publish = on_publish             #assign function to callback
client1.connect(broker,port)                #establish connection
cont = True
while(cont):
	message = input("Enter the message to publish: ")
	topic = input("Enter the topic to publish: ")
	qos = int(input("Enter the QoS level: "))
	qtdmsg = int(input("Enter the amount of messages to publish: "))
	rf = input("Retain message (1 True / 0 False) : ")
	for x in range(1,qtdmsg+1):
		if (rf == "1") :
			ret= client1.publish(topic,message,qos=qos,retain=True)  #publish
		else:
			ret= client1.publish(topic,message,qos=qos,retain=False)    #publish
		pass
	print("...")
	print("message <", message, "> was published on topic <", topic, ">")
	print("...")
	opc = input("Continue to Publishing (Y/n): ")
	if ((opc=="n") or (opc=="N")) :
		cont = False
		print("Connection finished.")
