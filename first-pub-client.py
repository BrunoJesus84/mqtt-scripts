import paho.mqtt.client as mqtt #import the client1
#broker_address="192.168.1.73" 
broker_address = "broker.hivemq.com" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
print("connected to broker.")
message = input("Enter the message to publish: ")
topic = input("Enter the topic to publish: ")
print("Publishing to topic: ",topic)
client.publish("Bruno",message)#publish
print("message <", message, "> was published on topic <", topic, ">")