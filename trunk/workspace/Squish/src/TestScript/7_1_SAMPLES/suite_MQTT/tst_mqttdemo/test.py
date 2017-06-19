from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API import functions
from API.ComponentBox import ComponentBoxConst

from API.Device.Ioe.SBC import SBC
from API.Device.HomeGateway.HomeGateway import HomeGateway

util = Util()

home_gateway = HomeGateway(ComponentBoxConst.DeviceModel.HOME_GATEWAY, 165, 60, 'Home Gateway0')

broker = SBC('SBC-PT', 65, 180, 'MQTT Broker') 
client = SBC('SBC-PT', 270, 180, 'MQTT Client')

USERNAME = 'TESTER'
PASSWORD = 'test_password0'
TOPIC = 'myhome/bedroom/temp'

def main():
    open_sample('7.1/MQTT/mqttdemo.pkt')
    get_broker_ip()
    run_broker()
    add_user()
    run_client()
    connect_to_broker()
    disconnect_client()
    connect_to_broker()
    subscribe_to_topic()
    unsubscribe()
    subscribe_to_topic()
    publish_message()
    check_messages()
    

def open_sample(file_path):
    util.init()
    util.maximizePT()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()
    
def run_broker():
    broker.select()
    broker.clickDesktopTab()
    broker.desktop.applications.mqttBroker()

def add_user():
    broker.desktop.mqttBroker.addUser(USERNAME, PASSWORD)

def run_client():
    client.select()
    client.clickDesktopTab()
    client.desktop.applications.mqttClient()

def connect_to_broker():
    client.desktop.mqttClient.connect(broker.ip, USERNAME, PASSWORD)

def disconnect_client():
    client.desktop.mqttClient.disconnect()

def subscribe_to_topic():
    client.desktop.mqttClient.subscriptions.subscribe(TOPIC)

def unsubscribe():
    client.desktop.mqttClient.subscriptions.unsubscribe(TOPIC)

def publish_message():
    client.desktop.mqttClient.publish.publish(TOPIC, '70', '0')

def check_messages():
    client_msgs = [
            'Success: subscribed to myhome/bedroom/temp.',
            'Success: unsubscribed from myhome/bedroom/temp.',
            'Success: published 70 to myhome/bedroom/temp with QoS 0.'
            ]
    broker_msgs = [
                   'Success: added TESTER as an authorized user.',
                   '\{"cmd":"PUBLISH","client":"[0-9A-Za-z]+","qos":0,"dup":0,"topic":"myhome/bedroom/temp","payload":"70","retain":0\}'
                   ]
    for msg in client_msgs:
        client.desktop.mqttClient.textCheckPoint(msg)
    for msg in broker_msgs:
        broker.desktop.mqttBroker.textCheckPoint(msg)
    None
    
def get_broker_ip():
    broker.select()
    broker.clickConfigTab()
    broker.config.selectInterface('Wireless3')
    broker.ip = broker.config.interface.wireless.getIp()
    broker.close()
