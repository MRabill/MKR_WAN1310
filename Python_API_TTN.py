import time
import ttn

app_id = "wlmtest"
access_key = "ttn-account-v2.dKPfvnaejn9H-ebz8eDXuwuLkFBjquePcQY0oRqV1bQ"

def uplink_callback(msg, client):
  #print("Received uplink from ", msg.dev_id)
  print(msg.payload_fields.field1)

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(100)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
#print(my_app)
my_devices = app_client.devices()
#print(my_devices)
