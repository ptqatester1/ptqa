from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.functions import WebviewTagFind2 as TF
from API.SquishSyntax import SquishSyntax
import object

class Webview(SquishObjectName):
    @property
    def _webview(self):
        return self.objName('.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.CDesktopApplet1.CBaseWorkstationCustomApp.m_customWebView.DOCUMENT.HTML1.BODY1')
    
    def click_id(self, id):
        Util().click(TF().findTagWithID(self._webview, id))
    
    def set_text_id(self, id, text):
        Util().setText(TF().findTagWithID(self._webview, id), text)
        
    def select_dropdown_option_id(self, id, option):
        dropdown = TF().findTagWithID(self._webview, id)
        options = dropdown.options()
        for i in range(options.length):
            if options.at(i).text == option:
                dropdown.setSelectedIndex(i)
                break
    
    def textCheckPoint(self, text, **args):
        Util().textCheckPoint(self._webview, text, **args)

class Broker(Webview, SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
        
    def on(self):
        None
    
    def off(self):
        None
    
    def username(self, username):
        self.set_text_id('inputUsername', username)
        
    def password(self, password):
        self.set_text_id('inputPassword', password)
    
    def addButton(self):
        self.click_id('btnAddUser')
    
    def addUser(self, username, password = None):
        self.username(username)
        if password:
            self.password(password)
        self.addButton()

    def removeButton(self):
        None


class ClientSubscriptions(Webview, SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def topic(self, topic_name):
        self.set_text_id('inputSubscribeTopic', topic_name)
    
    def subscribeButton(self):
        self.click_id('btnSubscribe')
    
    def topicDropdown(self, topic_name):
        self.select_dropdown_option_id('selectUnsubscribeTopic', topic_name)
    
    def unsubscribeButton(self):
        self.click_id('btnUnsubscribe')

    def subscribe(self, topic_name):
        self.topic(topic_name)
        self.subscribeButton()
    
    def unsubscribe(self, topic_name):
        self.topicDropdown(topic_name)
        self.unsubscribeButton()
    
class ClientPublish(Webview, SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def topic(self, topic_name):
        self.set_text_id('inputPublishTopic', topic_name)
    
    def payload(self, payload):
        self.set_text_id('inputPublishPayload', payload)
    
    def qos(self, qos):
        self.set_text_id('inputQoS', qos)

    def publishButton(self):
        self.click_id('btnPublish')
    
    def publish(self, topic, payload, qos):
        self.topic(topic)
        self.payload(payload)
        self.qos(qos)
        self.publishButton()

class Client(Webview, SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.subscriptions = ClientSubscriptions(self)
        self.publish = ClientPublish(self)
    
    def updateName(self, squishName):
        self.squishName = squishName
        self.subscriptions.updateName(self.squishName)
        self.publish.updateName(self.squishName)
    
    def brokerAddress(self, address):
        self.set_text_id('inputBrokerAddress', address)
    
    def username(self, username):
        self.set_text_id('inputUsername', username)
    
    def password(self, password):
        self.set_text_id('inputPassword', password)
    
    def connectButton(self):
        self.click_id('btnConnect')
    
    def connect(self, brokerAddress, username = None, password = None):
        self.brokerAddress(brokerAddress)
        if username:
            self.username(username)
        if password:
            self.password(password)
        self.connectButton()
    
    def disconnect(self):
        self.connectButton()

    def eventLog(self):
        None